# NSData.SearchOptions

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum NSDataSearchOptions : NSUInteger;
```

#### Overview

These options are used with the [`range(of:options:in:)`](./range%28of,options,in%29.md) method.

## Topics

### Initializers
- [init(rawValue: UInt)](./searchoptions/init%28rawvalue%29.md)
### Constants
- [static var backwards: NSData.SearchOptions](./searchoptions/backwards.md)
  Search from the end of the data object.
- [static var anchored: NSData.SearchOptions](./searchoptions/anchored.md)
  Search is limited to start (or end, if searching backwards) of the data object.

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

### Finding Data
- [func subdata(with: NSRange) -> Data](./subdata%28with%29.md)
  Returns a new data object containing the data object’s bytes that fall within the limits specified by a given range.
- [func range(of: Data, options: NSData.SearchOptions, in: NSRange) -> NSRange](./range%28of,options,in%29.md)
  Finds and returns the range of the first occurrence of the given data, within the given range, subject to given options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/searchoptions)*