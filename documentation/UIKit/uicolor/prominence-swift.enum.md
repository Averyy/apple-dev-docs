# UIColor.Prominence

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UIColorProminence : NSInteger;
```

## Overview

Interface elements, such as text labels, can have a different level of prominence in the UI. For example, a title label appears more prominently than a subtitle or caption. When you specify a label’s color, you can pass one of the [`UIColor.Prominence`](./prominence-swift.enum.md) constants to [`withProminence(_:)`](./withprominence%28_%29.md) to communicate how prominently to display that color in the UI.

The following code creates a label with a secondary, vibrant red color:

```swift
let label = UILabel()
label.preferredVibrancy = .automatic
label.textColor = .systemRed.withProminence(.secondary) 
```

## Topics

### Constants
- [UIColor.Prominence.primary](./prominence-swift.enum/primary.md)
  A color with a primary prominence, the most prominent in the interface.
- [UIColor.Prominence.secondary](./prominence-swift.enum/secondary.md)
  A color with a secondary prominence.
- [UIColor.Prominence.tertiary](./prominence-swift.enum/tertiary.md)
  A color with a tertiary prominence.
- [UIColor.Prominence.quaternary](./prominence-swift.enum/quaternary.md)
  A color with a quaternary prominence, the least prominent in the interface.
### Initializers
- [init?(rawValue: Int)](./prominence-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Working with color prominence
- [var prominence: UIColor.Prominence](./prominence-swift.property.md)
- [func withProminence(UIColor.Prominence) -> UIColor](./withprominence%28_%29.md)
  Returns the version of the current color that results from applying the specified prominence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/prominence-swift.enum)*