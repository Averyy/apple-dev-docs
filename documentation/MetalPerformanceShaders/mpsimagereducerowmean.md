# MPSImageReduceRowMean

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A filter that returns the mean value for each row in an image.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSImageReduceRowMean
```

```objc
@interface MPSImageReduceRowMean : MPSImageReduceUnary
```

## Topics

### Initializers
- [init(device: any MTLDevice)](./mpsimagereducerowmean/init%28device%29.md)

## Relationships

### Inherits From
- [MPSImageReduceUnary](./mpsimagereduceunary.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Image Reduction Filters
- [class MPSImageReduceRowMax](./mpsimagereducerowmax.md)
  A filter that returns the maximum value for each row in an image.
- [class MPSImageReduceRowMin](./mpsimagereducerowmin.md)
  A filter that returns the minimum value for each row in an image.
- [class MPSImageReduceRowSum](./mpsimagereducerowsum.md)
  A filter that returns the sum of all values for a row in an image.
- [class MPSImageReduceColumnMax](./mpsimagereducecolumnmax.md)
  A filter that returns the maximum value for each column in an image.
- [class MPSImageReduceColumnMin](./mpsimagereducecolumnmin.md)
  A filter that returns the minimum value for each column in an image.
- [class MPSImageReduceColumnSum](./mpsimagereducecolumnsum.md)
  A filter that returns the sum of all values for a column in an image.
- [class MPSImageReduceColumnMean](./mpsimagereducecolumnmean.md)
  A filter that returns the mean value for each column in an image.
- [class MPSImageReduceUnary](./mpsimagereduceunary.md)
  The base class for reduction filters that take a single source as input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagereducerowmean)*