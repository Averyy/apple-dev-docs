# Displaying the app extensions available to your app

**Framework**: ExtensionKit

Show the app extensions available to your app, so that people can approve, enable, or disable them.

#### Overview

Host apps can retrieve the list of currently available app extensions programmatically, but the person using the app might also need to see those extensions. The system automatically disables any app extensions that ship separately from their host app, and reenabling them requires manual intervention from the owner of the device. On macOS, a person can enable and disable extensions from the Settings app. However, [`ExtensionKit`](ExtensionKit.md) also provides a custom interface that you can show directly from your app.

When designing your app’s interface, consider the workflow for managing any app extensions. Include UI for enabling and disabling extensions in a readily accessible part of your app. For example, present this information in your app’s settings so that people can get to it at any time. When showing this type of content, always use the system-provided interface instead of trying to gather the information yourself. The system interface provide the only comprehensive list of app extensions on the device, along with the controls to enable or disable them correctly.

##### Display the App Extension Browser

To display a list of app extensions associated with your app, include an [`EXAppExtensionBrowserViewController`](exappextensionbrowserviewcontroller.md) in your app’s interface. This view controller displays the extensions for all of your app’s extension points. In addition to the name of each extension, the interface displays controls to enable or disable each one.

In a UIKit- or AppKit-based app, you can present an [`EXAppExtensionBrowserViewController`](exappextensionbrowserviewcontroller.md) object as you would any other view controller. For example, you can add it to a navigation stack or integrate it into your app’s settings interface. In a SwiftUI app, create a type that adopts the [`UIViewControllerRepresentable`](https://developer.apple.com/documentation/SwiftUI/UIViewControllerRepresentable) or [`NSViewControllerRepresentable`](https://developer.apple.com/documentation/SwiftUI/NSViewControllerRepresentable) protocol, and present that type from your interface. The following example shows a typical implementation of this type for a SwiftUI interface in macOS:

```swift
import SwiftUI
import ExtensionKit
import ExtensionFoundation

struct ExtensionBrowserView: NSViewControllerRepresentable {
    typealias NSViewControllerType = EXAppExtensionBrowserViewController
        
    func makeNSViewController(context: Context) -> EXAppExtensionBrowserViewController {
        let viewController = EXAppExtensionBrowserViewController()
        return viewController
    }
    
    func updateNSViewController(_ uiViewController: EXAppExtensionBrowserViewController, context: Context) {
    }
}
```

The interface of the [`EXAppExtensionBrowserViewController`](exappextensionbrowserviewcontroller.md) type runs out of process, and the type itself doesn’t notify your app of any changes. When someone enables or disables an extension from this interface, the system notifies your app through its [`AppExtensionPoint.Monitor`](https://developer.apple.com/documentation/ExtensionFoundation/AppExtensionPoint/Monitor) type. For more information about receiving updates from this type, see [`Discovering app extensions from your app`](https://developer.apple.com/documentation/ExtensionFoundation/discovering-app-extensions-from-your-app).

##### Notify People When Unapproved Extensions Are Waiting

In addition to providing details about the available extensions, the [`AppExtensionPoint.Monitor`](https://developer.apple.com/documentation/ExtensionFoundation/AppExtensionPoint/Monitor) type also reports the number of disabled and unapproved app extensions for your app. To get this information, fetch the value of your monitor’s [`state`](https://developer.apple.com/documentation/ExtensionFoundation/AppExtensionPoint/Monitor/state-swift.property) property. If the number of unapproved app extensions is greater than zero, consider alerting the person to this fact from your interface. Someone using your app might not know that app extensions are waiting for approval. A badge in the appropriate part of your interface, or a one-time notification can alert people to this information without being too invasive.

## See Also

- [class EXHostViewController](exhostviewcontroller.md)
  A view controller that hosts remote views provided by an app extension.
- [class EXAppExtensionBrowserViewController](exappextensionbrowserviewcontroller.md)
  A view controller that displays an interface to enable or disable the host app’s extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/displaying-the-app-extensions-available-to-your-app)*