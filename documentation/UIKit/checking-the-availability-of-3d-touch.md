# Checking the availability of 3D Touch

**Framework**: UIKit

Check whether a device supports 3D Touch before enabling features that use it.

#### Overview

To determine if 3D Touch is available on a device, check the [`forceTouchCapability`](uitraitcollection/forcetouchcapability.md) property of any object — such as your app’s views and view controllers — that adopts the [`UITraitEnvironment`](uitraitenvironment.md) protocol. The following code shows how you might use this property to enable or disable features at load time from your view controller. Use the [`traitCollectionDidChange(_:)`](uitraitenvironment/traitcollectiondidchange(_:).md) method to detect changes to 3D Touch availability while your app is running.

```swift
class ViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
 
        // Check the trait collection to see if force is available.
        if self.traitCollection.forceTouchCapability == .available {
            // Enable 3D Touch features
        } else {
            // Fall back to other non 3D Touch features.
        }
    }
 
    override func traitCollectionDidChange(_ previousTraitCollection: UITraitCollection?) {
        // Update the app's 3D Touch support.
        if self.traitCollection.forceTouchCapability == .available {
            // Enable 3D Touch features
        } else {
            // Fall back to other non 3D Touch features.
        }
    }
}
```

For guidance on how to implement your app both with and without 3D Touch support, see [`iOS Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/ios/human-interface-guidelines/).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/checking-the-availability-of-3d-touch)*