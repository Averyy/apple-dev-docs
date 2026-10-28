# standardAppearance

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The appearance settings for a standard-height navigation bar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var standardAppearance: UINavigationBarAppearance? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) UINavigationBarAppearance * standardAppearance;
```

## Discussion

When the navigation bar displays the current navigation item, the appearance settings in this property override the settings provided by the [`standardAppearance`](../uinavigationbar/standardappearance.md) property of [`UINavigationBar`](../uinavigationbar.md).

Use this property to apply appearance settings to the navigation bar based on the navigation item stored in the [`topItem`](../uinavigationbar/topitem.md) property. If the top item’s [`standardAppearance`](./standardappearance.md) property is `nil`, UIKit uses the navigation bar’s appearance.

## See Also

### Overriding the navigation bar’s appearance settings
- [var compactAppearance: UINavigationBarAppearance?](./compactappearance.md)
  The appearance settings for a compact-height navigation bar.
- [var scrollEdgeAppearance: UINavigationBarAppearance?](./scrolledgeappearance.md)
  The appearance settings for a standard-height navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.
- [var compactScrollEdgeAppearance: UINavigationBarAppearance?](./compactscrolledgeappearance.md)
  The appearance settings for a compact-height navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/standardappearance)*