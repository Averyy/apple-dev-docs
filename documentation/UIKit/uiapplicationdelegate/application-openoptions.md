# application(_:open:options:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate to open a resource specified by a URL, and provides a dictionary of launch options.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool
```

## Mentions

- [Enabling document sharing](enabling-document-sharing.md)

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the delegate successfully handled the request or [`false`](https://developer.apple.com/documentation/Swift/false) if the attempt to open the URL resource failed.

#### Discussion

This method is not called if your implementations return [`false`](https://developer.apple.com/documentation/Swift/false) from both the [`application(_:willFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:willfinishlaunchingwithoptions:).md) and [`application(_:didFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md) methods. (If only one of the two methods is implemented, its return value determines whether this method is called.) If your app implements the [`applicationDidFinishLaunching(_:)`](uiapplicationdelegate/applicationdidfinishlaunching(_:).md) method instead of [`application(_:didFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md), this method is called to open the specified URL after the app has been initialized.

If a URL arrives while your app is suspended or running in the background, the system moves your app to the foreground prior to calling this method.

There is no equivalent notification for this delegation method.

## Parameters

- `app`: Your singleton app object.
- `url`: The URL resource to open. This resource can be a network resource or a file. For information about the Apple-registered URL schemes, see  .
- `options`: A dictionary of URL handling options. For information about the possible keys in this dictionary and how to handle them, see  . By default, the value of this parameter is an empty dictionary.

## See Also

- [UIApplication.OpenURLOptionsKey](uiapplication/openurloptionskey.md)
  Keys you use to access values in the options dictionary when opening a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:open:options:))*