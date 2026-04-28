# Restoring your app’s state with AppKit

**Framework**: AppKit

Provide continuity for people using your app by preserving current activities on macOS.

**Availability**:
- macOS 12.5+
- Xcode 14.2+

#### Overview

This sample app demonstrates how to preserve your app’s state information and restore the app to that previous state on subsequent launches. During a subsequent launch, restoring your interface to the previous interaction point provides continuity for your app, and lets people finish active tasks quickly.

When using your app, people perform actions that update and alter the user interface. For example, someone might view a specific page of information, and after they leave the app, the operating system might terminate it to free up the resources it holds. The person should be able to return to where they left off—and window state restoration is a core part of making that experience seamless.

This sample app demonstrates the use of state preservation and restoration for a macOS app. The sample app manages a set of products. Each product has a title, an image, and other metadata you can view and edit. The project shows how to preserve and restore product selection, tab state, editor state, and multiple windows using the [`NSWindowRestoration`](nswindowrestoration.md) protocol in AppKit.

The state restoration system in AppKit uses three key mechanisms working together:

- Window registration with a restoration class.
- Encoding state into an [`NSCoder`](https://developer.apple.com/documentation/Foundation/NSCoder) archive.
- Restoring windows on relaunch through the
[`restoreWindow(withIdentifier:state:completionHandler:)`](nswindowrestoration/restorewindow(withidentifier:state:completionhandler:).md) protocol method.

To learn how to adopt state restoration in your iOS app, see [`Restoring your app’s state`](https://developer.apple.com/documentation/UIKit/restoring-your-app-s-state). For state restoration in your SwiftUI app, see [`Restoring your app’s state with SwiftUI`](https://developer.apple.com/documentation/SwiftUI/restoring-your-app-s-state-with-swiftui).

#### Configure the Sample Code Project

In Xcode, select your development team on the macOS target’s Signing & Capabilities tab.

#### Enable Window State Restoration

To enable window state restoration, each window must be configured with a unique identifier, a frame autosave name, and a restoration class. The restoration class conforms to the [`NSWindowRestoration`](nswindowrestoration.md) protocol and is responsible for recreating the window during restoration.

```swift
window.identifier = NSUserInterfaceItemIdentifier("MainWindow")
window.setFrameAutosaveName("MainWindow")
window.restorationClass = WindowRestorationHandler.self
window.isRestorable = true
```

The app delegate must also declare support for secure restorable state:

```swift
func applicationSupportsSecureRestorableState(_ app: NSApplication) -> Bool {
    return true
}
```

#### Restore Windows with the Nswindowrestoration Protocol

The `WindowRestorationHandler` class conforms to [`NSWindowRestoration`](nswindowrestoration.md) and implements the static [`restoreWindow(withIdentifier:state:completionHandler:)`](nswindowrestoration/restorewindow(withidentifier:state:completionhandler:).md) method. AppKit calls this method at launch for each window that was open when the app last quit. The method creates the appropriate window controller based on the window identifier and passes the window back through the completion handler; otherwise, ignores the window and any errors by passing `nil`.

```swift
@MainActor
class WindowRestorationHandler: NSObject, NSWindowRestoration {
    static func restoreWindow(
        withIdentifier identifier: NSUserInterfaceItemIdentifier,
        state: NSCoder,
        completionHandler: @escaping (NSWindow?, Error?) -> Void
    ) {
        guard let appDelegate = NSApplication.shared.delegate as? AppDelegate else {
            completionHandler(nil, nil)
            return
        }

        switch identifier.rawValue {
        case WindowIdentifiers.mainWindow:
            // Create the main window for restoration.
            let controller = MainWindowController()
            appDelegate.mainWindowController = controller
            completionHandler(controller.window, nil)
        case WindowIdentifiers.imageWindow:
            // Create the image window for restoration.
            let controller = ImageWindowController()
            appDelegate.imageWindowControllers.append(controller)
            completionHandler(controller.window, nil)
        default:
            // Ignore the window creation without error to skip restoration. 
            completionHandler(nil, nil)
        }
    }
}
```

After AppKit creates each window through this method, it calls [`restoreState(with:)`](NSResponder/restoreState(with:).md) on the window controller to decode the saved state.

#### Encode and Decode Window State

Each window controller overrides [`encodeRestorableState(with:)`](NSResponder/encodeRestorableState(with:).md) to save its state, and `restoreState(with:)` to read it back. The main window controller encodes the selected product identifier, the active tab index, and whether the editor sheet was presented with its field values:

```swift
override func encodeRestorableState(with coder: NSCoder) {
    super.encodeRestorableState(with: coder)

    if let product = splitViewController?.selectedProduct {
        coder.encode(product.identifier.uuidString, forKey: RestorationKeys.productIdentifier)
    }
    if let tabIndex = splitViewController?.selectedTabIndex {
        coder.encode(tabIndex, forKey: RestorationKeys.selectedTab)
    }
    if let editorState = splitViewController?.editorState {
        coder.encode(true, forKey: RestorationKeys.presentedEditor)
        coder.encode(editorState.title, forKey: RestorationKeys.editorTitle)
        coder.encode(editorState.price, forKey: RestorationKeys.editorPrice)
        coder.encode(editorState.year, forKey: RestorationKeys.editorYear)
    } else {
        coder.encode(false, forKey: RestorationKeys.presentedEditor)
    }
}
```

The corresponding `restoreState(with:)` decodes these values and reconfigures the user interface:

```swift
override func restoreState(with coder: NSCoder) {
    super.restoreState(with: coder)

    if let productId = coder.decodeObject(forKey: RestorationKeys.productIdentifier) as? String,
       let product = DataModelManager.sharedInstance.product(fromIdentifier: productId) {
        splitViewController?.selectProduct(product)
    }
    let tabIndex = coder.decodeInteger(forKey: RestorationKeys.selectedTab)
    splitViewController?.restoreTabIndex(tabIndex)

    if coder.decodeBool(forKey: RestorationKeys.presentedEditor) {
        let title = coder.decodeObject(forKey: RestorationKeys.editorTitle) as? String
        let price = coder.decodeObject(forKey: RestorationKeys.editorPrice) as? String
        let year = coder.decodeObject(forKey: RestorationKeys.editorYear) as? String
        splitViewController?.restoreEditor(title: title, price: price, year: year)
    }
}
```

#### Invalidate Restorable State on Changes

Whenever someone makes a change that should be preserved—selecting a product, switching tabs, or editing fields—the window controller calls [`invalidateRestorableState()`](nsresponder/invalidaterestorablestate().md). This tells AppKit that the saved state is out of date and needs to be re-encoded before the app terminates.

```swift
splitViewController.onProductSelected = { [weak self] product in
    self?.invalidateRestorableState()
}
splitViewController.onTabChanged = { [weak self] in
    self?.invalidateRestorableState()
}
```

#### Restore Multiple Windows

The sample app supports multiple windows. The main window displays a split view with a product collection in the sidebar and a detail pane. Additional standalone image windows can be opened for any product. Each window type has its own window controller and encodes its own state independently.

Image window controllers encode only the product identifier:

```swift
override func encodeRestorableState(with coder: NSCoder) {
    super.encodeRestorableState(with: coder)
    if let product = product {
        coder.encode(product.identifier.uuidString, forKey: RestorationKeys.productIdentifier)
    }
}
```

AppKit restores all open windows on relaunch. The `WindowRestorationHandler` class routes each window to the correct controller based on its identifier.

#### Test State Restoration

This sample app restores the following user interface:

- Main Window Product Selection — Click a product in the sidebar collection view to display its detail information. The app restores the selected product and the active tab (Detail or Photo).
- Main Window Edit State — Click the Edit toolbar button to present the editor sheet. The app restores the sheet and its field values, even if the edit was in progress.
- Image Windows — Control-click a product in the sidebar and select Open in New Window, or click the Open Image toolbar button. The app restores all open image windows and the products they display.

To test state restoration, quit the app normally (Command-Q or through the app menu). Do not force quit the app, as macOS discards saved state when a person force quits. Relaunch the app, and AppKit initiates the window restoration process, recreating each window in its previous state.

## See Also

- [protocol NSWindowRestoration](nswindowrestoration.md)
  A set of methods that restoration classes must implement to handle the recreation of windows.
- [protocol NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
  A set of methods used to associate a unique identifier with objects in your user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/restoring-your-app-s-state-with-appkit)*