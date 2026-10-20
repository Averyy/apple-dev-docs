# next()

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.

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
mutating func next() async throws -> Self.Element?
```

#### Return Value

The next element, if it exists, or `nil` to signal the end of the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asynciteratorprotocol/next())*