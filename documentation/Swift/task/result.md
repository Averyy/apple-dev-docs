# result

**Framework**: Swift  
**Kind**: property

The result or error from a throwing task, after it completes.

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
var result: Result<Success, Failure> { get async }
```

#### Return Value

If the task succeeded, `.success` with the task’s result as the associated value; otherwise, `.failure` with the error as the associated value.

#### Discussion

If the task hasn’t completed, accessing this property waits for it to complete and its priority increases to that of the current task. Note that this might not be as effective as creating the task with the correct priority, depending on the executor’s scheduling details.

## See Also

- [var value: Success](task/value-60t02.md)
  The result from a throwing task, after it completes.
- [var value: Success](task/value-40dtq.md)
  The result from a nonthrowing task, after it completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/result)*