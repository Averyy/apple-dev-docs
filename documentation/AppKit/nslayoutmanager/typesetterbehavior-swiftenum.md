# NSLayoutManager.TypesetterBehavior

**Framework**: AppKit  
**Kind**: enum

Constants that determine the layout manager’s behavior during layout.

**Availability**:
- macOS ?+

## Declaration

```swift
enum TypesetterBehavior
```

#### Overview

These constants define the behavior of `NSLayoutManager` and `NSTypesetter` when laying out lines. They are used by [`typesetterBehavior`](nslayoutmanager/typesetterbehavior-swift.property.md) to control the compatibility level of the typesetter.

## Topics

### Behaviors
- [NSLayoutManager.TypesetterBehavior.latestBehavior](nslayoutmanager/typesetterbehavior-swift.enum/latestbehavior.md)
  The current typesetter behavior in the current operating system.
- [NSLayoutManager.TypesetterBehavior.originalBehavior](nslayoutmanager/typesetterbehavior-swift.enum/originalbehavior.md)
  The original typesetter behavior, as shipped with macOS 10.1 and earlier.
- [NSLayoutManager.TypesetterBehavior.behavior_10_2_WithCompatibility](nslayoutmanager/typesetterbehavior-swift.enum/behavior_10_2_withcompatibility.md)
  The macOS 10.2 typesetting behavior that is still compatible with the original typesetter behavior.
- [NSLayoutManager.TypesetterBehavior.behavior_10_2](nslayoutmanager/typesetterbehavior-swift.enum/behavior_10_2.md)
  The typesetter behavior introduced in macOS 10.2.
- [NSLayoutManager.TypesetterBehavior.behavior_10_3](nslayoutmanager/typesetterbehavior-swift.enum/behavior_10_3.md)
  The typesetter behavior introduced in macOS 10.3.
- [NSLayoutManager.TypesetterBehavior.behavior_10_4](nslayoutmanager/typesetterbehavior-swift.enum/behavior_10_4.md)
  The typesetter behavior introduced in macOS 10.4.
### Initializers
- [init?(rawValue: Int)](nslayoutmanager/typesetterbehavior-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var typesetter: NSTypesetter](nslayoutmanager/typesetter.md)
  The current typesetter.
- [var typesetterBehavior: NSLayoutManager.TypesetterBehavior](nslayoutmanager/typesetterbehavior-swift.property.md)
  The default typesetter behavior.
- [func defaultLineHeight(for: NSFont) -> CGFloat](nslayoutmanager/defaultlineheight(for:).md)
  Returns the default line height for a line of text that uses a specified font.
- [func defaultBaselineOffset(for: NSFont) -> CGFloat](nslayoutmanager/defaultbaselineoffset(for:).md)
  Returns the default baseline offset that the layout manager’s typesetter uses for the specified font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/typesetterbehavior-swift.enum)*