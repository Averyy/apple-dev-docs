# connect()

**Framework**: Combine  
**Kind**: method

Connects to the publisher, allowing it to produce elements, and returns an instance with which to cancel publishing.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func connect() -> any Cancellable
```

#### Return Value

A [`Cancellable`](cancellable.md) instance that you use to cancel publishing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/makeconnectable/connect())*