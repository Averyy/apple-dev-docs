# isEmpty

**Framework**: Swift  
**Kind**: property

A Boolean value that indicates whether the group has any remaining tasks.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var isEmpty: Bool { get }
```

#### Return Value

`true` if the group has no pending tasks; otherwise `false`.

#### Discussion

At the start of the body of a `withThrowingDiscardingTaskGroup(returning:body:)` call, the task group is always empty.

It’s guaranteed to be empty when returning from that body because a task group waits for all child tasks to complete before returning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/throwingdiscardingtaskgroup/isempty)*