# dataWithLength:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns an mutable data object containing a given number of zeroed bytes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) dataWithLength:(NSUInteger) length;
```

## Return Value

A new `NSMutableData` object of `length` bytes, filled with zeros. The returned object has the same memory alignment guarantees as `malloc(_:)`.

## Parameters

- `length`: The number of bytes the new data object initially contains.

## See Also

### Creating Mutable Data
- [+ dataWithCapacity:](./datawithcapacity_.md)
  Creates and returns a mutable data object capable of holding the specified number of bytes.
- [init?(capacity: Int)](./init%28capacity%29.md)
  Returns an initialized mutable data object capable of holding the specified number of bytes.
- [init?(length: Int)](./init%28length%29.md)
  Initializes and returns a mutable data object containing a given number of zeroed bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledata/datawithlength:)*