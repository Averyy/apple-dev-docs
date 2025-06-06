# next()

**Framework**: Group Activities  
**Kind**: method

Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
mutating func next() async -> SystemCoordinator.ParticipantStates.Element?
```

#### Return Value

The next element, if it exists, or `nil` to signal the end of the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/systemcoordinator/participantstates/iterator/next())*