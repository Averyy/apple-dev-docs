# next()

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

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
mutating func next() async -> ChildTaskResult?
```

## See Also

### Accessing Individual Results
- [func next(isolation: isolated (any Actor)?) async -> ChildTaskResult?](./next%28isolation%29.md)
  Waits for the next child task to complete, and returns the value it returned.
- [var isEmpty: Bool](./isempty.md)
  A Boolean value that indicates whether the group has any remaining tasks.
- [func waitForAll() async](./waitforall%28%29.md)
  Wait for all of the group’s remaining tasks to complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/taskgroup/next())*