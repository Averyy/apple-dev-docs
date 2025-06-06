# scrollEdgeAppearance

**Framework**: UIKit  
**Kind**: property

The appearance settings for a standard-height navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var scrollEdgeAppearance: UINavigationBarAppearance? { get set }
```

#### Discussion

When the navigation bar displays the top navigation item, the appearance settings in this property override the settings provided by the [`scrollEdgeAppearance`](uinavigationbar/scrolledgeappearance.md) property of [`UINavigationBar`](uinavigationbar.md).

Use this property to apply appearance settings to the navigation bar based on the navigation item stored in the [`topItem`](uinavigationbar/topitem.md) property. If the top item’s [`scrollEdgeAppearance`](uitabbaritem/scrolledgeappearance.md) property is `nil`, UIKit uses the navigation bar’s scroll edge appearance.

When running on apps that use iOS 14 or earlier, this property applies to navigation bars with large titles. In iOS 15, this property applies to all navigation bars.

## See Also

- [var standardAppearance: UINavigationBarAppearance?](uinavigationitem/standardappearance.md)
  The appearance settings for a standard-height navigation bar.
- [var compactAppearance: UINavigationBarAppearance?](uinavigationitem/compactappearance.md)
  The appearance settings for a compact-height navigation bar.
- [var compactScrollEdgeAppearance: UINavigationBarAppearance?](uinavigationitem/compactscrolledgeappearance.md)
  The appearance settings for a compact-height navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/scrolledgeappearance)*