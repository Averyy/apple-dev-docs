# PaperMarkupViewController.ScrollConfiguration.Axis

**Framework**: PaperKit  
**Kind**: struct

The axes you use to specify scroll view behavior.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Axis
```

#### Overview

This struct mirrors UIKit’s `UIAxis` type for cross-platform compatibility.

## Topics

### Choosing an axis
- [static let horizontal: PaperMarkupViewController.ScrollConfiguration.Axis](papermarkupviewcontroller/scrollconfiguration-swift.class/axis/horizontal.md)
  The horizontal axis.
- [static let vertical: PaperMarkupViewController.ScrollConfiguration.Axis](papermarkupviewcontroller/scrollconfiguration-swift.class/axis/vertical.md)
  The vertical axis.
- [static let both: PaperMarkupViewController.ScrollConfiguration.Axis](papermarkupviewcontroller/scrollconfiguration-swift.class/axis/both.md)
  The combined horizontal and vertical axes.
### Initializers
- [init(rawValue: Int)](papermarkupviewcontroller/scrollconfiguration-swift.class/axis/init(rawvalue:).md)
  Creates a new set of axes from the given raw value.
### Instance Properties
- [let rawValue: Int](papermarkupviewcontroller/scrollconfiguration-swift.class/axis/rawvalue.md)
  The raw bitmask that represents this set of axes.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [var visibleScrollIndicators: PaperMarkupViewController.ScrollConfiguration.Axis](papermarkupviewcontroller/scrollconfiguration-swift.class/visiblescrollindicators.md)
  The axes for which scroll indicators are visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/scrollconfiguration-swift.class/axis)*