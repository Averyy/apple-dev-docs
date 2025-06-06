# compactScrollEdgeAppearance

**Framework**: UIKit  
**Kind**: property

The appearance settings for a compact-height navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var compactScrollEdgeAppearance: UINavigationBarAppearance? { get set }
```

#### Discussion

When a compact-height navigation bar displays the top navigation item, the appearance setting in this property overrides the settings in the [`compactScrollEdgeAppearance`](uinavigationbar/compactscrolledgeappearance.md) property of [`UINavigationBar`](uinavigationbar.md).

Use this property to apply appearance settings to the navigation bar based on the navigation item stored in the [`topItem`](uinavigationbar/topitem.md) property. If the top item’s [`compactScrollEdgeAppearance`](uinavigationitem/compactscrolledgeappearance.md) property is `nil`, UIKit uses the navigation bar’s compact scroll edge appearance.

## See Also

- [var standardAppearance: UINavigationBarAppearance?](uinavigationitem/standardappearance.md)
  The appearance settings for a standard-height navigation bar.
- [var compactAppearance: UINavigationBarAppearance?](uinavigationitem/compactappearance.md)
  The appearance settings for a compact-height navigation bar.
- [var scrollEdgeAppearance: UINavigationBarAppearance?](uinavigationitem/scrolledgeappearance.md)
  The appearance settings for a standard-height navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/compactscrolledgeappearance)*