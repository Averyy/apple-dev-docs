# UIColor.Prominence

**Framework**: UIKit  
**Kind**: enum

A type that indicates the prominence of a color in the interface.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
enum Prominence
```

#### Overview

Interface elements, such as text labels, can have a different level of prominence in the UI. For example, a title label appears more prominently than a subtitle or caption. When you specify a label’s color, you can pass one of the [`UIColor.Prominence`](uicolor/prominence-swift.enum.md) constants to [`withProminence(_:)`](uicolor/withprominence(_:).md) to communicate how prominently to display that color in the UI.

The following code creates a label with a secondary, vibrant red color:

```swift
let label = UILabel()
label.preferredVibrancy = .automatic
label.textColor = .systemRed.withProminence(.secondary) 
```

## Topics

### Constants
- [UIColor.Prominence.primary](uicolor/prominence-swift.enum/primary.md)
  A color with a primary prominence, the most prominent in the interface.
- [UIColor.Prominence.secondary](uicolor/prominence-swift.enum/secondary.md)
  A color with a secondary prominence.
- [UIColor.Prominence.tertiary](uicolor/prominence-swift.enum/tertiary.md)
  A color with a tertiary prominence.
- [UIColor.Prominence.quaternary](uicolor/prominence-swift.enum/quaternary.md)
  A color with a quaternary prominence, the least prominent in the interface.
### Initializers
- [init?(rawValue: Int)](uicolor/prominence-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var prominence: UIColor.Prominence](uicolor/prominence-swift.property.md)
- [func withProminence(UIColor.Prominence) -> UIColor](uicolor/withprominence(_:).md)
  Returns the version of the current color that results from applying the specified prominence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/prominence-swift.enum)*