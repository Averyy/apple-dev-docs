# supportsAlternateIcons

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the app is allowed to change its icon.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
var supportsAlternateIcons: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL supportsAlternateIcons;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) only when the system allows you to change the icon of your app. To declare your app’s alternate icons, include them in the [`CFBundleIcons`](../../BundleResources/information-property-list/cfbundleicons.md) key of your app’s `Info.plist` file.

The value of this property is always [`false`](../../Swift/false.md) for apps built using the visionOS SDK.

## See Also

### Managing the app’s icon
- [var alternateIconName: String?](./alternateiconname.md)
  The name of the icon the system displays for the app.
- [func setAlternateIconName(String?, completionHandler: (((any Error)?) -> Void)?)](./setalternateiconname%28_,completionhandler%29.md)
  Changes the icon the system displays for the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/supportsalternateicons)*