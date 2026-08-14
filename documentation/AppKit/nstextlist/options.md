# NSTextList.Options

**Framework**: AppKit  
**Kind**: struct

Values that available options for text list items.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct Options
```

## Topics

### Options
- [static var prependEnclosingMarker: NSTextList.Options](nstextlist/options/prependenclosingmarker.md)
  Specifies that a nested list should include the marker for its enclosing superlist before its own marker.
### Initializers
- [init(rawValue: UInt)](nstextlist/options/init(rawvalue:).md)
  Returns a new set of text list options using the raw value you specify.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [var isOrdered: Bool](nstextlist/isordered.md)
- [var listOptions: NSTextList.Options](nstextlist/listoptions.md)
  Returns the list options mask value of the receiver.
- [class var includesTextListMarkers: Bool](nstextlist/includestextlistmarkers.md)
  A Boolean value that indicates whether TextKit includes text list markers in the contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlist/options)*