# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a publisher to emit the value of the optional, or to finish immediately if the optional doesn’t have a value.

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
init(_ output: Optional<Wrapped>.Publisher.Output?)
```

## Parameters

- `output`: The result to deliver to each subscriber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/publisher-swift.struct/init(_:))*