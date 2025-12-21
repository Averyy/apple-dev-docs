# TN3123: Refactoring your storyboard

**Framework**: Technotes

Learn strategies and techniques for refactoring a single storyboard into multiple storyboards.

#### Overview

A storyboard is used to graphically lay out your app’s user interface. You use Xcode’s Interface Builder to specify your interface using scenes, segues between scenes, and controls used to trigger the segues. At design time, you configure the content of your view controllers visually, and Xcode saves the data needed to recreate that interface in a storyboard file in your app’s bundle.

Over time, as your application’s UI evolves into a larger set of view controller scenes, it may become a challenge to manage and maintain that storyboard. This can be a further challenge when you need to design it with multiple team members. Two team members modifying the same storyboard could potentially cause source control problems. Improve the storyboard management process by separating your single storyboard file into individual storyboards. Storyboards are connected together using storyboard references.

#### Benefits of Using Multiple Storyboards

When a storyboard is refactored, you gain three benefits:

1. Improved readability - View controller connections become more explicit and the segue connections are easier to trace.
2. Reuse - A separate storyboard containing a view controller scene can be referenced and re-used in multiple parts of the app.
3. Easier to manage - A large team may work more efficiently when each member manages their own UI. Dividing your storyboard can help avoid merge conflicts when you use a source code version control system like Git.

#### Connect Two Storyboards Using a Storyboard Reference

A view controller is connected to another by using a segue and a storyboard reference. This involves three stages.

1. Create a separate storyboard containing an individual view controller and give that view controller a unique identifier.
2. Back in the app’s Main storyboard, create a storyboard reference and set its storyboard and identifier created in step 1.
3. Create a segue from the source view controller and connect it to the storyboard reference.

#### Automatically Refactor a Storyboard Using Xcode

For some UI elements Xcode helps refactor a single storyboard into multiple storyboards automatically.

To separate out a [`UITabBarController`](https://developer.apple.com/documentation/UIKit/UITabBarController) in iOS:

1. Open the storyboard.
2. Select the `UITabBarController` scene.
3. Select Menu: Editor > Refactor to Storyboard…
4. Name and save the new storyboard file to your project.

The new storyboard file will contain the `UITabBarController`. The child view controllers are separated and linked through storyboard references using unique identifiers. Storyboard references link one storyboard to another.

To separate out a [`NSTabViewController`](https://developer.apple.com/documentation/AppKit/NSTabViewController) in macOS:

1. Open the storyboard.
2. Select the `NSTabViewController` scene.
3. Select Menu: Editor > Refactor to Storyboard…
4. Name and save the new storyboard file to your project.

The new storyboard file will contain the `NSTabViewController`. The child view controllers are separated and linked through storyboard references using unique identifiers.

#### Manually Refactor a Storyboard

If you choose to refactor your storyboard yourself, for example if one [`UIViewController`](https://developer.apple.com/documentation/UIKit/UIViewController) (VC1) presents another (VC2), do the following:

1. Open the app’s Main storyboard file.
2. Select the view controller scene you want to present, and copy it.
3. Create new storyboard file: File > New > File… - choose Storyboard, name and save it “VC2”.
4. With the VC2 storyboard open, paste the copied view controller.
5. Select the copied view controller and select its Identify Inspector.
6. Name its Storyboard ID as “VC2_identifier”.
7. Go back to the Main storyboard.
8. Remove the view controller scene you previously copied.
9. Select Menu > Show Library
10. Drag and drop a new Storyboard Reference from the Library window into the Main storyboard.
11. Select the dropped Storyboard Reference and select its Attributes Inspector.
12. Set the Storyboard to “VC2”.
13. Set the Referenced ID “VC2_identifier”.
14. Connect this Storyboard Reference via segue from VC1.

![The storyboard reference attributes inspector.](https://docs-assets.developer.apple.com/published/81640c312c6c750ce7f3424edeb0286a/tn3123-storyboardref%402x.png) ![The storyboard segue.](https://docs-assets.developer.apple.com/published/99079be614c0ad5aeac61d7561feeab2/tn3123-segue%402x.png)

#### Load Storyboards Programmatically

Segues connecting two view controller scenes within the same storyboard load the view controller automatically. When a single storyboard is refactored into separate storyboards, storyboard references load them automatically as well. You can, however, load view controller scenes manually using code. You use  to do that. Storyboard instances come in two flavors: [`NSStoryboard`](https://developer.apple.com/documentation/AppKit/NSStoryboard) for macOS, and [`UIStoryboard`](https://developer.apple.com/documentation/UIKit/UIStoryboard) for iOS. These APIs on both platforms are similar.

#### Load and Open an Nswindowcontroller Programmatically with Macos

In macOS, an [`NSViewController`](https://developer.apple.com/documentation/AppKit/NSViewController) is loaded separately, or through its [`NSWindowController`](https://developer.apple.com/documentation/AppKit/NSWindowController).

```swift
let storyboard = NSStoryboard(name: "InspectorWindow", bundle: Bundle.main)
if let windController = storyboard.instantiateInitialController() as? NSWindowController {
    windController.window!.makeKeyAndOrderFront(self)
}
```

The window controller inside the “InspectorWindow” storyboard is to be set at the initial controller via “Is Initial Controller”.

![The window as the initial controller.](https://docs-assets.developer.apple.com/published/93b94a87ce3772eb0dc66aec035661ae/tn3123-initialController%402x.png)

#### Load and Present a Uiviewcontroller Programmatically with Ios

Load by identifier:

```swift
let mainStoryboard: UIStoryboard = UIStoryboard(name: "DetailViewController", bundle: nil)
let viewController = mainStoryboard.instantiateViewController(withIdentifier: "DetailViewControllerID") as! UIViewController
self.present(viewController, animated: true, completion: nil)
```

Load by initial view controller:

```swift
let mainStoryboard: UIStoryboard = UIStoryboard(name: "DetailViewController", bundle: nil)
if let viewController = mainStoryboard.instantiateInitialViewController() {
    present(viewController, animated: true, completion: nil)
}
```

The view controller inside the “DetailViewController” storyboard is to be set at the initial controller via “Is Initial Controller”.

#### Load and Present a Uiviewcontroller Programmatically with Swiftui

If you are developing a SwiftUI app, and you want to integrate an existing `UIViewController` subclass and its storyboard:

```swift
struct DetailView: View {
    var body: some View {
        DetailViewControllerRepresentable()
    }
}

final class DetailViewControllerRepresentable: UIViewControllerRepresentable {
    typealias UIViewControllerType = DetailViewController

    func makeUIViewController(context: Context) -> DetailViewController {
        let storyboard = UIStoryboard(name: "DetailViewController", bundle: nil)
        return storyboard.instantiateInitialViewController() as! DetailViewController
    }

    func updateUIViewController(_ uiViewController: DetailViewController, context: Context) { }
    func makeCoordinator() -> Coordinator { Coordinator(self) }

    class Coordinator: NSObject {
        private let parent: DetailViewControllerRepresentable
        init(_ parent: DetailViewControllerRepresentable) {
            self.parent = parent
        }
    }
}

class DetailViewController: UIViewController { }
```

#### Revision History

-  First published.

## See Also

- [TN3190: USB audio device design considerations](tn3190-usb-audio-device-design-considerations.md)
  Learn the best techniques for designing devices that conform to the USB Audio Device Class specifications.
- [TN3194: Handling account deletions and revoking tokens for Sign in with Apple](tn3194-handling-account-deletions-and-revoking-tokens-for-sign-in-with-apple.md)
  Learn the best techniques for managing Sign in with Apple user sessions and responding to account deletion requests.
- [TN3193: Managing the on-device foundation model’s context window](tn3193-managing-the-on-device-foundation-model-s-context-window.md)
  Learn how to budget for the context window limit of Apple’s on-device foundation model and handle the error when reaching the limit.
- [TN3115: Bluetooth State Restoration app relaunch rules](tn3115-bluetooth-state-restoration-app-relaunch-rules.md)
  Learn about the conditions under which an iOS app will be relaunched by Bluetooth State Restoration.
- [TN3192: Migrating your iPad app from the deprecated UIRequiresFullScreen key](tn3192-migrating-your-app-from-the-deprecated-uirequiresfullscreen-key.md)
  Support iPad multitasking and dynamic resizing while updating your app to remove the deprecated full-screen compatibility mode.
- [TN3151: Choosing the right networking API](tn3151-choosing-the-right-networking-api.md)
  Learn which networking API is best for you.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3191: IMAP extensions supported by Mail for iOS, iPadOS, and visionOS](tn3191-imap-extensions-supported-by-mail.md)
  Learn which extensions to the RFC 3501 IMAP protocol are supported by Mail for iOS, iPadOS, and visionOS.
- [TN3134: Network Extension provider deployment](tn3134-network-extension-provider-deployment.md)
  Explore the platforms, packaging, OS versions, and device configurations for Network Extension provider deployment.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3123-refactoring-your-storyboard)*