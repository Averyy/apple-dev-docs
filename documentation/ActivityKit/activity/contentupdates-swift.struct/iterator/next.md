# next()

**Framework**: ActivityKit  
**Kind**: method

Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.

**Availability**:
- iOS 16.2+
- iPadOS 16.2+

## Declaration

```swift
func next() async -> Activity<Attributes>.ContentUpdates.Element?
```

#### Return Value

The next element, if it exists, or `nil` to signal the end of the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/contentupdates-swift.struct/iterator/next())*