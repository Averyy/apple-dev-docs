# NSLayoutManager.TypesetterBehavior

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that determine the layout manager’s behavior during layout.

**Availability**:
- macOS

## Declaration

```swift
enum TypesetterBehavior
```

```c
enum NSTypesetterBehavior : NSInteger;
```

## Overview

These constants define the behavior of `NSLayoutManager` and `NSTypesetter` when laying out lines. They are used by [`typesetterBehavior`](./typesetterbehavior-swift.property.md) to control the compatibility level of the typesetter.

## Topics

### Behaviors
- [NSLayoutManager.TypesetterBehavior.latestBehavior](./typesetterbehavior-swift.enum/latestbehavior.md)
  The current typesetter behavior in the current operating system.
- [NSLayoutManager.TypesetterBehavior.originalBehavior](./typesetterbehavior-swift.enum/originalbehavior.md)
  The original typesetter behavior, as shipped with macOS 10.1 and earlier.
- [NSLayoutManager.TypesetterBehavior.behavior_10_2_WithCompatibility](./typesetterbehavior-swift.enum/behavior_10_2_withcompatibility.md)
  The macOS 10.2 typesetting behavior that is still compatible with the original typesetter behavior.
- [NSLayoutManager.TypesetterBehavior.behavior_10_2](./typesetterbehavior-swift.enum/behavior_10_2.md)
  The typesetter behavior introduced in macOS 10.2.
- [NSLayoutManager.TypesetterBehavior.behavior_10_3](./typesetterbehavior-swift.enum/behavior_10_3.md)
  The typesetter behavior introduced in macOS 10.3.
- [NSLayoutManager.TypesetterBehavior.behavior_10_4](./typesetterbehavior-swift.enum/behavior_10_4.md)
  The typesetter behavior introduced in macOS 10.4.
### Initializers
- [init?(rawValue: Int)](./typesetterbehavior-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing the typesetter
- [var typesetter: NSTypesetter](./typesetter.md)
  The current typesetter.
- [var typesetterBehavior: NSLayoutManager.TypesetterBehavior](./typesetterbehavior-swift.property.md)
  The default typesetter behavior.
- [func defaultLineHeight(for: NSFont) -> CGFloat](./defaultlineheight%28for%29.md)
  Returns the default line height for a line of text that uses a specified font.
- [func defaultBaselineOffset(for: NSFont) -> CGFloat](./defaultbaselineoffset%28for%29.md)
  Returns the default baseline offset that the layout manager’s typesetter uses for the specified font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/typesetterbehavior-swift.enum)*