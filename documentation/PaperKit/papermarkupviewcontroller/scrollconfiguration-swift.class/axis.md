# PaperMarkupViewController.ScrollConfiguration.Axis

**Framework**: PaperKit  
**Kind**: struct  
**Role**: Structure

The axes you use to specify scroll view behavior.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Axis
```

#### Overview

This struct mirrors UIKit’s `UIAxis` type for cross-platform compatibility.

## Topics

### Choosing an axis
- [static let horizontal: PaperMarkupViewController.ScrollConfiguration.Axis](./axis/horizontal.md)
  The horizontal axis.
- [static let vertical: PaperMarkupViewController.ScrollConfiguration.Axis](./axis/vertical.md)
  The vertical axis.
- [static let both: PaperMarkupViewController.ScrollConfiguration.Axis](./axis/both.md)
  The combined horizontal and vertical axes.
### Initializers
- [init(rawValue: Int)](./axis/init%28rawvalue%29.md)
  Creates a new set of axes from the given raw value.
### Instance Properties
- [let rawValue: Int](./axis/rawvalue.md)
  The raw bitmask that represents this set of axes.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../../Swift/optionset.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [SetAlgebra](../../../Swift/setalgebra.md)

## See Also

### Configuring scroll indicators
- [var visibleScrollIndicators: PaperMarkupViewController.ScrollConfiguration.Axis](./visiblescrollindicators.md)
  The axes for which scroll indicators are visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/scrollconfiguration-swift.class/axis)*