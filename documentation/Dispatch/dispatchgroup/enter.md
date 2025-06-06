# enter()

**Framework**: Dispatch  
**Kind**: method

Explicitly indicates that a block has entered the group.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func enter()
```

#### Discussion

Calling this function in Objective-C increments the current count of outstanding tasks in the group. Using this function (with [`leave()`](dispatchgroup/leave().md)) allows your application to properly manage the task reference count if it explicitly adds and removes tasks from the group by a means other than using the [`dispatch_group_async`](dispatch_group_async.md) function. A call to this function must be balanced with a call to [`leave()`](dispatchgroup/leave().md). You can use this function to associate a block with more than one group at the same time.

## See Also

- [func leave()](dispatchgroup/leave.md)
  Explicitly indicates that a block in the group finished executing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchgroup/enter())*