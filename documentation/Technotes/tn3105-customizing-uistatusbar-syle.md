# TN3105: Customizing the UIKit status bar style

**Framework**: Technotes

Configure the device’s status bar style to work well with your app’s user interface.

#### Overview

Status bar content elements must be readable or visible to the user. Your app’s status bar style or [`UIStatusBarStyle`](https://developer.apple.comhttps://developer.apple.com/documentation/uikit/uistatusbarstyle) should be set to a value that’s compatible with your app’s background color: [`lightContent`](https://developer.apple.comhttps://developer.apple.com/documentation/uikit/uistatusbarstyle/lightcontent) or [`darkContent`](https://developer.apple.comhttps://developer.apple.com/documentation/uikit/uistatusbarstyle/darkcontent).

You control the `UIStatusBarStyle` at the app level or view controller level. At the app level choose a single `UIStatusBarStyle` that works well with its overall background color scheme. At the view controller level choose a `UIStatusBarStyle` that is most compatible with its specific background color.

If you find that your status bar elements aren’t visible, the problem might be that its background color is the same color as its content color (black elements on black background or white elements on white background). Users may also have a difficult time recognizing the status bar content when the background color is dark gray and its `UIStatusBarStyle` set to `darkContent`.

If you have a dark colored background, set the `UIStatusBarStyle` to `lightContent`. If you have a light colored background, set the `UIStatusBarStyle` to `darkContent`.

#### Set a Style for the Entire App

For a single status bar style throughout your app, add [`UIViewControllerBasedStatusBarAppearance`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information_property_list/uiviewcontrollerbasedstatusbarappearance) with a value of `false` to your `Info.plist`. Then add `UIStatusBarStyle` with the specific style. For example, to set a light content status bar, use the following:

```None
<key>UIStatusBarStyle</key>
<string>UIStatusBarStyleLightContent</string>

<key>UIViewControllerBasedStatusBarAppearance</key>
<false/>
```

#### Set a Style for Each View Controller

To allow individual view controllers to determine their status bar style, set `UIViewControllerBasedStatusBarAppearance` to `true`.

First, add the `UIViewControllerBasedStatusBarAppearance` property to the `Info.plist`:

```None
<key>UIViewControllerBasedStatusBarAppearance</key>
<true/>
```

Second, if your initial root view controller’s status bar style is light content, add the following to the `Info.plist`. This will make your initial view controller’s status bar style match up with the launch screen status bar style:

```None
<key>UIStatusBarStyle</key>
<string>UIStatusBarStyleLightContent</string>
```

Third, override each view controller’s [`preferredStatusBarStyle()`](https://developer.apple.comhttps://developer.apple.com/documentation/uikit/uiviewcontroller/1621416-preferredstatusbarstyle) method. For example, to set the status bar’s content intended for use on dark backgrounds:

```swift

class ViewController: UIViewController {
	//..
    override var preferredStatusBarStyle: UIStatusBarStyle {
        return .lightContent
    }
    //..
}
```

If a particular view controller is embedded as a child or resides inside a [`UINavigationController`](https://developer.apple.comhttps://developer.apple.com/documentation/uikit/uinavigationcontroller) stack, its parent or navigation controller determines the status bar style. If you want the containing view controller to give control of the status bar style to its children, override the [`childForStatusBarStyle`](https://developer.apple.comhttps://developer.apple.com/documentation/uikit/uiviewcontroller/1621433-childforstatusbarstyle) property. For example:

```swift
class MyNavigationController: UINavigationController {
    // Return the visible child view controller which determines the status bar style.
    override var childForStatusBarStyle: UIViewController? { return visibleViewController }
}
```

For every `UINavigationController` defined in your storyboard that wants to give status bar style control over to its children, be sure to set its Custom Class name to match the `UINavigationController` subclass name on the Identity inspector.

It is not necessary to override the `childForStatusBarStyle` property when using [`UITabBarController`](https://developer.apple.comhttps://developer.apple.com/documentation/uikit/uitabbarcontroller). `UITabBarController` automatically forwards status bar style requests to its children.

When using this approach, any child view controller determines the status bar style that will match up with its color scheme or customization it uses with [`UINavigationBarAppearance`](https://developer.apple.comhttps://developer.apple.com/documentation/uikit/uinavigationbarappearance/). If you return `nil` or do not override this method, the status bar style for `self` is used. If the return value from this method changes, call the `setNeedsStatusBarAppearanceUpdate()` method.

#### Revision History

- **2022-03-01** First published.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3105-customizing-uistatusbar-syle)*