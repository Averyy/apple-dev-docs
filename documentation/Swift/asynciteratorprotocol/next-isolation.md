# next(isolation:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
mutating func next(isolation actor: isolated (any Actor)?) async throws(Self.Failure) -> Self.Element?
```

#### Return Value

The next element, if it exists, or `nil` to signal the end of the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asynciteratorprotocol/next(isolation:))*