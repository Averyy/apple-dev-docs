# copyBytes(to:count:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Copies the provided number of bytes from the start of the type into a raw memory buffer.

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
func copyBytes(to ptr: UnsafeMutableRawBufferPointer, count: Int) -> Int
```

#### Return Value

The number of bytes copied.

## Parameters

- `ptr`: A pointer to the raw memory buffer you want to copy the bytes into.
- `count`: The number of bytes to copy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dataprotocol/copybytes(to:count:)-45x1l)*