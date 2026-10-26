# resetBytes(in:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Replaces the contents of the data buffer with zeros for the provided range.

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
mutating func resetBytes<R>(in range: R) where R : RangeExpression, Self.Index == R.Bound
```

## Parameters

- `range`: The range of bytes to replace with zeros.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/mutabledataprotocol/resetbytes(in:)-9ix6g)*