# next()

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Asynchronously retrieve the next Event.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
mutating func next() async -> ARKitSession.Events.Element?
```

## Return Value

The next Event if one has occurred since the last call to this function. Otherwise suspends the caller until a new Event has occurred. Returns `nil` (signals end of the sequence) if the session has been stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitsession/events-swift.struct/iterator/next())*