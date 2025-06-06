# setAlternateIconName(_:completionHandler:)

**Framework**: Uikit  
**Kind**: method

Changes the icon the system displays for the app.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setAlternateIconName(_ alternateIconName: String?) async throws
```

#### Discussion

Use this method to change your app’s icon to its primary icon or to one of its alternate icons. You can change the icon only if the value of the [`supportsAlternateIcons`](uiapplication/supportsalternateicons.md) property is [`true`](https://developer.apple.com/documentation/swift/true).

You must configure your app’s primary icon asset in the “App Icons and Launch Images” section of the General pane or set it directly using the “Primary App Icon Set Name” build setting. You specify the names of additional icon assets available to your app using the “Alternate App Icon Sets” build setting. Xcode uses these setting to generate the entries for [`CFBundlePrimaryIcon`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleIcons/CFBundlePrimaryIcon) and [`CFBundleAlternateIcons`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleIcons/CFBundleAlternateIcons) under the top-level key [`CFBundleIcons`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleIcons). For more information, see [`Build settings reference`](https://developer.apple.com/documentation/Xcode/build-settings-reference) and [`Configuring your app icon`](https://developer.apple.com/documentation/Xcode/configuring-your-app-icon).

> **Note**:  This method still sets the alternate icon in compatible iPad and iPhone apps running in visionOS. Support for alternate icons is unavailable in apps you build using the visionOS SDK, and calling this method has no effect.

## Parameters

- `alternateIconName`: The name of the alternate icon, as declared in the   key of your app’s   file. Specify   if you want to display the app’s primary icon, which you declare using the   key. Both keys are subentries of the   key in your app’s   file.
- `completionHandler`: The handler to execute with the results. After attempting to change your app’s icon, the system reports the results by calling your handler. The handler executes on a UIKit-provided queue, and not necessarily on your app’s main queue. The handler has no return value and takes the following parameter:

## See Also

- [var supportsAlternateIcons: Bool](uiapplication/supportsalternateicons.md)
  A Boolean value that indicates whether the app is allowed to change its icon.
- [var alternateIconName: String?](uiapplication/alternateiconname.md)
  The name of the icon the system displays for the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/setalternateiconname(_:completionhandler:))*