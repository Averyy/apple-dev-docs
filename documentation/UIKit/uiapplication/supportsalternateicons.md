# supportsAlternateIcons

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the app is allowed to change its icon.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var supportsAlternateIcons: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) only when the system allows you to change the icon of your app. To declare your app’s alternate icons, include them in the [`CFBundleIcons`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleIcons) key of your app’s `Info.plist` file.

The value of this property is always [`false`](https://developer.apple.com/documentation/swift/false) for apps built using the visionOS SDK.

## See Also

- [var alternateIconName: String?](uiapplication/alternateiconname.md)
  The name of the icon the system displays for the app.
- [func setAlternateIconName(String?, completionHandler: (((any Error)?) -> Void)?)](uiapplication/setalternateiconname(_:completionhandler:).md)
  Changes the icon the system displays for the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/supportsalternateicons)*