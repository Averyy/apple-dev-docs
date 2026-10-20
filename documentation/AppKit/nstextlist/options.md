# NSTextList.Options

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Values that available options for text list items.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct Options
```

```c
enum NSTextListOptions : NSUInteger;
```

## Topics

### Options
- [static var prependEnclosingMarker: NSTextList.Options](./options/prependenclosingmarker.md)
  Specifies that a nested list should include the marker for its enclosing superlist before its own marker.
### Initializers
- [init(rawValue: UInt)](./options/init%28rawvalue%29.md)
  Returns a new set of text list options using the raw value you specify.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Getting list options
- [var isOrdered: Bool](./isordered.md)
- [var listOptions: NSTextList.Options](./listoptions.md)
  Returns the list options mask value of the receiver.
- [class var includesTextListMarkers: Bool](./includestextlistmarkers.md)
  A Boolean value that indicates whether TextKit includes text list markers in the contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlist/options)*