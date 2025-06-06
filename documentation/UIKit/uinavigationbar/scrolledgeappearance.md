# scrollEdgeAppearance

**Framework**: UIKit  
**Kind**: property

The appearance settings for the navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.

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

When a navigation controller contains a navigation bar and a scroll view, part of the scroll view’s content appears underneath the navigation bar. If the edge of the scrolled content reaches that bar, UIKit applies the appearance settings in this property.

If the value of this property is `nil`, UIKit uses the settings found in the [`standardAppearance`](uinavigationbar/standardappearance.md) property, modified to use a transparent background. If no navigation controller manages your navigation bar, UIKit ignores this property and uses the standard appearance of the navigation bar.

When running on apps that use iOS 14 or earlier, this property applies to navigation bars with large titles. In iOS 15, this property applies to all navigation bars.

## See Also

- [var prefersLargeTitles: Bool](uinavigationbar/preferslargetitles.md)
  A Boolean value that indicates whether the title displays in a large format.
- [var standardAppearance: UINavigationBarAppearance](uinavigationbar/standardappearance.md)
  The appearance settings for a standard-height navigation bar.
- [var compactAppearance: UINavigationBarAppearance?](uinavigationbar/compactappearance.md)
  The appearance settings for a compact-height navigation bar.
- [var compactScrollEdgeAppearance: UINavigationBarAppearance?](uinavigationbar/compactscrolledgeappearance.md)
  The appearance settings for a compact-height navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.
- [var isTranslucent: Bool](uinavigationbar/istranslucent.md)
  A Boolean value that indicates whether the navigation bar is translucent.
- [Legacy customizations](uinavigationbar-legacy-customizations.md)
  Customize appearance information directly on the navigation bar object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/scrolledgeappearance)*