# NSData.SearchOptions

**Framework**: Foundation  
**Kind**: struct

Options for method used to search data objects.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct SearchOptions
```

#### Overview

These options are used with the [`range(of:options:in:)`](nsdata/range(of:options:in:).md) method.

## Topics

### Initializers
- [init(rawValue: UInt)](nsdata/searchoptions/init(rawvalue:).md)
### Constants
- [static var backwards: NSData.SearchOptions](nsdata/searchoptions/backwards.md)
  Search from the end of the data object.
- [static var anchored: NSData.SearchOptions](nsdata/searchoptions/anchored.md)
  Search is limited to start (or end, if searching backwards) of the data object.

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

- [func subdata(with: NSRange) -> Data](nsdata/subdata(with:).md)
  Returns a new data object containing the data object’s bytes that fall within the limits specified by a given range.
- [func range(of: Data, options: NSData.SearchOptions, in: NSRange) -> NSRange](nsdata/range(of:options:in:).md)
  Finds and returns the range of the first occurrence of the given data, within the given range, subject to given options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/searchoptions)*