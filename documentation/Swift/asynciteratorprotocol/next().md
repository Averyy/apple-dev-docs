# next()

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method  
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

## Return Value

The next element, if it exists, or `nil` to signal the end of the sequence.

## Default Implementations

### AsyncIteratorProtocol Implementations
- [func next() async throws(Self.Failure) -> Self.Element?](./next%28%29-4a3d9.md)
  Default implementation of `next()` in terms of `next(isolation:)`, which is required to maintain backward compatibility with existing async iterators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asynciteratorprotocol/next())*