# next()

**Framework**: ActivityKit  
**Kind**: method

Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
func next() async -> Activity<Attributes>.PushTokenUpdates.Element?
```

#### Return Value

The next element, if it exists, or `nil` to signal the end of the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/pushtokenupdates-swift.struct/iterator/next())*