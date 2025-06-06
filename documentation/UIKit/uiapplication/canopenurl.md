# canOpenURL(_:)

**Framework**: UIKit  
**Kind**: method

Returns a Boolean value that indicates whether an app is available to handle a URL scheme.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func canOpenURL(_ url: URL) -> Bool
```

#### Return Value

[`false`](https://developer.apple.com/documentation/swift/false) if the device doesn’t have an installed app registered to handle the URL’s scheme, or if you haven’t declared the URL’s scheme in your `Info.plist` file; otherwise, [`true`](https://developer.apple.com/documentation/swift/true).

#### Discussion

When this method returns [`true`](https://developer.apple.com/documentation/swift/true), iOS guarantees subsequent calls to the [`open(_:options:completionHandler:)`](uiapplication/open(_:options:completionhandler:).md) method with the same URL will successfully launch an app that can handle the URL. The return value doesn’t indicate the validity of the URL, whether the specified resource exists, or, in the case of a universal link, whether the device has an installed app registered to respond to the universal link.

You can call this method safely on a thread that isn’t the main thread.

> ❗ **Important**:  If you link your app on or after iOS 9.0, you must declare the URL schemes you pass to this method by adding the `LSApplicationQueriesSchemes` key to your app’s `Info.plist` file. This method always returns [`false`](https://developer.apple.com/documentation/swift/false) for undeclared schemes, even if the device doesn’t have a registered app installed. Apps linked on or after iOS 15 are limited to a maximum of 50 entries in the `LSApplicationQueriesSchemes` key. To learn more about the key, see [`LSApplicationQueriesSchemes`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/plist/info/LSApplicationQueriesSchemes).

 If you link your app on or after iOS 9.0, you must declare the URL schemes you pass to this method by adding the `LSApplicationQueriesSchemes` key to your app’s `Info.plist` file. This method always returns [`false`](https://developer.apple.com/documentation/swift/false) for undeclared schemes, even if the device doesn’t have a registered app installed. Apps linked on or after iOS 15 are limited to a maximum of 50 entries in the `LSApplicationQueriesSchemes` key. To learn more about the key, see [`LSApplicationQueriesSchemes`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/plist/info/LSApplicationQueriesSchemes).

If you link your app against an earlier version of iOS but it is running in iOS 9.0 or later, you can call this method up to 50 times. After reaching that limit, subsequent calls always return [`false`](https://developer.apple.com/documentation/swift/false). If the user reinstalls or upgrades the app, iOS resets the limit.

Unlike this method, the [`open(_:options:completionHandler:)`](uiapplication/open(_:options:completionhandler:).md) method isn’t constrained by the `LSApplicationQueriesSchemes` requirement. If an app is available to handle the URL, the system will launch it, even if you haven’t declared the scheme.

Using universal links instead of custom URL schemes removes the need to use this method to validate target links; if no app is available to handle a universal link, iOS routes it to the person’s default browser, allowing the associated website to respond. For more information on universal links, see [`Allowing apps and websites to link to your content`](https://developer.apple.com/documentation/Xcode/allowing-apps-and-websites-to-link-to-your-content).

## Parameters

- `url`: The URL can have a common scheme such as  ,  ,  , or  , or a custom scheme. For information about supported schemes, see  .

## See Also

- [func openURL(URL) -> Bool](uiapplication/openurl(_:).md)
  Attempts to open the resource at the specified URL.
- [func open(URL, options: [UIApplication.OpenExternalURLOptionsKey : Any], completionHandler: ((Bool) -> Void)?)](uiapplication/open(_:options:completionhandler:).md)
  Attempts to asynchronously open the resource at the specified URL.
- [UIApplication.OpenExternalURLOptionsKey](uiapplication/openexternalurloptionskey.md)
  Options for opening a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/canopenurl(_:))*