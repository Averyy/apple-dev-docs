# next()

**Framework**: ARKit  
**Kind**: method

Asynchronously retrieve the next anchor update.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
mutating func next() async -> AnchorUpdateSequence<AnchorType>.Iterator<TypeOfAnchor>.Element?
```

#### Return Value

The next anchor update if one has occurred since the last call to this function. Otherwise suspends the caller until a new anchor update has occurred. Returns `nil` (signals end of the sequence) if the provider has been stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/anchorupdatesequence/iterator/next())*