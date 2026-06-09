# getValue(_:size:)

**Framework**: Foundation  
**Kind**: method

Copies the value into the specified buffer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func getValue(_ value: UnsafeMutableRawPointer, size: Int)
```

## Parameters

- `value`: A buffer into which to copy the value. The buffer must be large enough to hold the value.
- `size`: The number of bytes to copy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue/getvalue(_:size:))*