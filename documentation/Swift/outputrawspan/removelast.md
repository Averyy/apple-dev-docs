# removeLast(_:)

**Framework**: Swift  
**Kind**: method

Remove the last n bytes from this span, returning the memory they occupy to the uninitialized state.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 5.2+

## Declaration

```swift
mutating func removeLast(_ n: Int)
```

#### Discussion

`n` must not be greater than `byteCount`.

## Parameters

- `n`: The number of bytes to remove. `n` must not be negative or greater than `byteCount`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/outputrawspan/removelast(_:))*