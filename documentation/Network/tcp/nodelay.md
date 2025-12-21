# noDelay(_:)

**Framework**: Network  
**Kind**: method

Disable Nagle’s algorithm.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func noDelay(_ noDelay: Bool) -> TCP
```

#### Discussion

A boolean indicating that TCP should disable Nagle’s algorithm (`TCP_NODELAY`).

## Parameters

- `noDelay`: True to disable Nagle’s algorithm, false otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/tcp/nodelay(_:))*