# init(length:)

**Framework**: Foundation  
**Kind**: init

Initializes and returns a mutable data object containing a given number of zeroed bytes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(length: Int)
```

#### Return Value

An initialized `NSMutableData` object containing `length` zeroed bytes. The returned object has the same memory alignment guarantees as `malloc(_:)`.

## Parameters

- `length`: The number of bytes the object initially contains.

## See Also

- [init?(capacity: Int)](nsmutabledata/init(capacity:).md)
  Returns an initialized mutable data object capable of holding the specified number of bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledata/init(length:))*