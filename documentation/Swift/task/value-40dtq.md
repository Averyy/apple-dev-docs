# value

**Framework**: Swift  
**Kind**: property

The result from a nonthrowing task, after it completes.

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
var value: Success { get async }
```

#### Discussion

If the task hasn’t completed yet, accessing this property waits for it to complete and its priority increases to that of the current task. Note that this might not be as effective as creating the task with the correct priority, depending on the executor’s scheduling details.

Tasks that never throw an error can still check for cancellation, but they need to use an approach like returning `nil` instead of throwing an error.

## See Also

- [var value: Success](task/value-60t02.md)
  The result from a throwing task, after it completes.
- [var result: Result<Success, Failure>](task/result.md)
  The result or error from a throwing task, after it completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/value-40dtq)*