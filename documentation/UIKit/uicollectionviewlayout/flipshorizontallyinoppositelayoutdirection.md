# flipsHorizontallyInOppositeLayoutDirection

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the horizontal coordinate system is automatically flipped at appropriate times.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var flipsHorizontallyInOppositeLayoutDirection: Bool { get }
```

#### Discussion

The language you use during development naturally affects the decisions you make when configuring your layout object. When you develop using a left-to-right language, your layout information automatically matches the collection view’s natural coordinate system. However, when the user’s language has a right-to-left orientation, the layout information you provide is still based on the collection view’s natural coordinate system. This discrepancy can cause layout issues for languages using the opposite orientation. When this property is set to [`true`](https://developer.apple.com/documentation/Swift/true), the collection view automatically flips the orientation of its horizontal coordinate system to match the leading edge of the current language. (The [`developmentLayoutDirection`](uicollectionviewlayout/developmentlayoutdirection.md) property specifies the layout direction used to design the layout.) Flipping the horizontal coordinate system effectively flips your existing layout information, which should result in a better looking layout.

The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var developmentLayoutDirection: UIUserInterfaceLayoutDirection](uicollectionviewlayout/developmentlayoutdirection.md)
  The direction of the language you used when designing your custom layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/flipshorizontallyinoppositelayoutdirection)*