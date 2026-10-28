# current

**Framework**: Swift Testing  
**Kind**: property  
**Role**: Type Property

The test that is running on the current task, if any.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
static var current: Test? { get }
```

## Discussion

If the current task is running a test, or is a subtask of another task that is running a test, the value of this property describes that test. If no test is currently running, the value of this property is `nil`.

If the current task is detached from a task that started running a test, or if the current thread was created without using Swift concurrency (e.g. by using [Thread.detachNewThread(_:)](../../Foundation/thread/detachnewthread%28_%29.md) or [DispatchQueue.async(execute:)](../../Dispatch/dispatchqueue/async%28execute%29.md)), the value of this property may be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/test/current)*