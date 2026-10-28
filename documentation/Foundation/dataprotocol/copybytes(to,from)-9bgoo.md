# copyBytes(to:from:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Copies a range of the bytes from the type into a typed memory buffer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@discardableResult
func copyBytes<DestinationType, R>(to ptr: UnsafeMutableBufferPointer<DestinationType>, from range: R) -> Int where R : RangeExpression, Self.Index == R.Bound
```

## Return Value

The number of bytes copied.

## Parameters

- `ptr`: A typed pointer to the buffer you want to copy the bytes into.
- `range`: The range of bytes to copy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dataprotocol/copybytes(to:from:)-9bgoo)*