# AlignmentOptions

**Framework**: Foundation  
**Kind**: struct

Values representing alignment operations.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct AlignmentOptions
```

#### Overview

These constants are used by the [`NSIntegralRectWithOptions(_:_:)`](nsintegralrectwithoptions(_:_:).md) function and other related methods, such as [`backingAlignedRect(_:options:)`](https://developer.apple.com/documentation/AppKit/NSView/backingAlignedRect(_:options:)).

## Topics

### Constants
- [static var alignMinXInward: AlignmentOptions](alignmentoptions/alignminxinward.md)
  Specifies that alignment of the minimum X coordinate should be to the nearest inward integral value.
- [static var alignMinYInward: AlignmentOptions](alignmentoptions/alignminyinward.md)
  Specifies that alignment of the minimum Y coordinate should be to the nearest inward integral value.
- [static var alignMaxXInward: AlignmentOptions](alignmentoptions/alignmaxxinward.md)
  Specifies that alignment of the maximum X coordinate should be to the nearest inward integral value.
- [static var alignMaxYInward: AlignmentOptions](alignmentoptions/alignmaxyinward.md)
  Specifies that alignment of the maximum X coordinate should be to the nearest inward integral value.
- [static var alignWidthInward: AlignmentOptions](alignmentoptions/alignwidthinward.md)
  Specifies that alignment of the width should be to the nearest inward integral value.
- [static var alignHeightInward: AlignmentOptions](alignmentoptions/alignheightinward.md)
  Specifies that alignment of the height should be to the nearest inward integral value.
- [static var alignMinXOutward: AlignmentOptions](alignmentoptions/alignminxoutward.md)
  Specifies that alignment of the minimum X coordinate should be to the nearest outward integral value.
- [static var alignMinYOutward: AlignmentOptions](alignmentoptions/alignminyoutward.md)
  Specifies that alignment of the minimum Y coordinate should be to the nearest outward integral value.
- [static var alignMaxXOutward: AlignmentOptions](alignmentoptions/alignmaxxoutward.md)
  Specifies that alignment of the maximum X coordinate should be to the nearest outward integral value.
- [static var alignMaxYOutward: AlignmentOptions](alignmentoptions/alignmaxyoutward.md)
  Specifies that alignment of the maximum Y coordinate should be to the nearest outward integral value.
- [static var alignWidthOutward: AlignmentOptions](alignmentoptions/alignwidthoutward.md)
  Specifies that alignment of the width should be to the nearest outward integral value.
- [static var alignHeightOutward: AlignmentOptions](alignmentoptions/alignheightoutward.md)
  Specifies that alignment of the height should be to the nearest outward integral value.
- [static var alignMinXNearest: AlignmentOptions](alignmentoptions/alignminxnearest.md)
  Specifies that alignment of the minimum X coordinate should be to the nearest integral value.
- [static var alignMinYNearest: AlignmentOptions](alignmentoptions/alignminynearest.md)
  Specifies that alignment of the minimum Y coordinate should be to the nearest integral value.
- [static var alignMaxXNearest: AlignmentOptions](alignmentoptions/alignmaxxnearest.md)
  Specifies that alignment of the maximum X coordinate should be to the nearest integral value.
- [static var alignMaxYNearest: AlignmentOptions](alignmentoptions/alignmaxynearest.md)
  Specifies that alignment of the maximum Y coordinate should be to the nearest integral value.
- [static var alignWidthNearest: AlignmentOptions](alignmentoptions/alignwidthnearest.md)
  Specifies that alignment of the width should be to the nearest integral value.
- [static var alignHeightNearest: AlignmentOptions](alignmentoptions/alignheightnearest.md)
  Specifies that alignment of the height should be to the nearest integral value.
- [static var alignRectFlipped: AlignmentOptions](alignmentoptions/alignrectflipped.md)
  This option should be included  if the rectangle is in a flipped coordinate system. This allows 0.5 to be treated in a visually consistent way.
- [static var alignAllEdgesInward: AlignmentOptions](alignmentoptions/alignalledgesinward.md)
  Aligns all edges inward. This is the same as `NSAlignMinXInward|NSAlignMaxXInward|NSAlignMinYInward|NSAlignMaxYInward`.
- [static var alignAllEdgesOutward: AlignmentOptions](alignmentoptions/alignalledgesoutward.md)
  Aligns all edges outwards. This is the same as `NSAlignMinXOutward|NSAlignMaxXOutward|NSAlignMinYOutward|NSAlignMaxYOutward`.
- [static var alignAllEdgesNearest: AlignmentOptions](alignmentoptions/alignalledgesnearest.md)
  Aligns all edges to the nearest value. This is the same as `NSAlignMinXNearest|NSAlignMaxXNearest|NSAlignMinYNearest|NSAlignMaxYNearest`.
- [static var alignMinXInward: AlignmentOptions](alignmentoptions/alignminxinward.md)
  Specifies that alignment of the minimum X coordinate should be to the nearest inward integral value.
- [static var alignMinYInward: AlignmentOptions](alignmentoptions/alignminyinward.md)
  Specifies that alignment of the minimum Y coordinate should be to the nearest inward integral value.
- [static var alignMaxXInward: AlignmentOptions](alignmentoptions/alignmaxxinward.md)
  Specifies that alignment of the maximum X coordinate should be to the nearest inward integral value.
- [static var alignMaxYInward: AlignmentOptions](alignmentoptions/alignmaxyinward.md)
  Specifies that alignment of the maximum X coordinate should be to the nearest inward integral value.
- [static var alignWidthInward: AlignmentOptions](alignmentoptions/alignwidthinward.md)
  Specifies that alignment of the width should be to the nearest inward integral value.
- [static var alignHeightInward: AlignmentOptions](alignmentoptions/alignheightinward.md)
  Specifies that alignment of the height should be to the nearest inward integral value.
- [static var alignMinXOutward: AlignmentOptions](alignmentoptions/alignminxoutward.md)
  Specifies that alignment of the minimum X coordinate should be to the nearest outward integral value.
- [static var alignMinYOutward: AlignmentOptions](alignmentoptions/alignminyoutward.md)
  Specifies that alignment of the minimum Y coordinate should be to the nearest outward integral value.
- [static var alignMaxXOutward: AlignmentOptions](alignmentoptions/alignmaxxoutward.md)
  Specifies that alignment of the maximum X coordinate should be to the nearest outward integral value.
- [static var alignMaxYOutward: AlignmentOptions](alignmentoptions/alignmaxyoutward.md)
  Specifies that alignment of the maximum Y coordinate should be to the nearest outward integral value.
- [static var alignWidthOutward: AlignmentOptions](alignmentoptions/alignwidthoutward.md)
  Specifies that alignment of the width should be to the nearest outward integral value.
- [static var alignHeightOutward: AlignmentOptions](alignmentoptions/alignheightoutward.md)
  Specifies that alignment of the height should be to the nearest outward integral value.
- [static var alignMinXNearest: AlignmentOptions](alignmentoptions/alignminxnearest.md)
  Specifies that alignment of the minimum X coordinate should be to the nearest integral value.
- [static var alignMinYNearest: AlignmentOptions](alignmentoptions/alignminynearest.md)
  Specifies that alignment of the minimum Y coordinate should be to the nearest integral value.
- [static var alignMaxXNearest: AlignmentOptions](alignmentoptions/alignmaxxnearest.md)
  Specifies that alignment of the maximum X coordinate should be to the nearest integral value.
- [static var alignMaxYNearest: AlignmentOptions](alignmentoptions/alignmaxynearest.md)
  Specifies that alignment of the maximum Y coordinate should be to the nearest integral value.
- [static var alignWidthNearest: AlignmentOptions](alignmentoptions/alignwidthnearest.md)
  Specifies that alignment of the width should be to the nearest integral value.
- [static var alignHeightNearest: AlignmentOptions](alignmentoptions/alignheightnearest.md)
  Specifies that alignment of the height should be to the nearest integral value.
- [static var alignRectFlipped: AlignmentOptions](alignmentoptions/alignrectflipped.md)
  This option should be included  if the rectangle is in a flipped coordinate system. This allows 0.5 to be treated in a visually consistent way.
- [static var alignAllEdgesInward: AlignmentOptions](alignmentoptions/alignalledgesinward.md)
  Aligns all edges inward. This is the same as `NSAlignMinXInward|NSAlignMaxXInward|NSAlignMinYInward|NSAlignMaxYInward`.
- [static var alignAllEdgesOutward: AlignmentOptions](alignmentoptions/alignalledgesoutward.md)
  Aligns all edges outwards. This is the same as `NSAlignMinXOutward|NSAlignMaxXOutward|NSAlignMinYOutward|NSAlignMaxYOutward`.
- [static var alignAllEdgesNearest: AlignmentOptions](alignmentoptions/alignalledgesnearest.md)
  Aligns all edges to the nearest value. This is the same as `NSAlignMinXNearest|NSAlignMaxXNearest|NSAlignMinYNearest|NSAlignMaxYNearest`.
### Initializers
- [init(rawValue: UInt64)](alignmentoptions/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [enum NSRectEdge](nsrectedge.md)
- [typealias NSRectArray](nsrectarray.md)
  Type indicating a parameter is array of `NSRect` structures.
- [typealias NSRectPointer](nsrectpointer.md)
  Type indicating a parameter is a pointer to an `NSRect` structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/alignmentoptions)*