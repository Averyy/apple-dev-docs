# compactAppearance

**Framework**: UIKit  
**Kind**: property

The appearance settings for a compact-height navigation bar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var compactAppearance: UINavigationBarAppearance? { get set }
```

#### Discussion

If the value of this property is `nil`, UIKit uses the [`standardAppearance`](uinavigationitem/standardappearance.md) of the item stored in the [`topItem`](uinavigationbar/topitem.md) property. You can customize the compact appearance for specific navigation items with the [`compactAppearance`](uinavigationitem/compactappearance.md) property of [`UINavigationItem`](uinavigationitem.md).

## See Also

- [var prefersLargeTitles: Bool](uinavigationbar/preferslargetitles.md)
  A Boolean value that indicates whether the title displays in a large format.
- [var standardAppearance: UINavigationBarAppearance](uinavigationbar/standardappearance.md)
  The appearance settings for a standard-height navigation bar.
- [var scrollEdgeAppearance: UINavigationBarAppearance?](uinavigationbar/scrolledgeappearance.md)
  The appearance settings for the navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.
- [var compactScrollEdgeAppearance: UINavigationBarAppearance?](uinavigationbar/compactscrolledgeappearance.md)
  The appearance settings for a compact-height navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.
- [var isTranslucent: Bool](uinavigationbar/istranslucent.md)
  A Boolean value that indicates whether the navigation bar is translucent.
- [Legacy customizations](uinavigationbar-legacy-customizations.md)
  Customize appearance information directly on the navigation bar object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/compactappearance)*