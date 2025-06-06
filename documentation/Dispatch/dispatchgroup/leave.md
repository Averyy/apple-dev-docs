# leave()

**Framework**: Dispatch  
**Kind**: method

Explicitly indicates that a block in the group finished executing.

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
func leave()
```

#### Discussion

Calling this function decrements the current count of outstanding tasks in the group. Using this function (with [`enter()`](dispatchgroup/enter().md)) allows your application to properly manage the task reference count if it explicitly adds and removes tasks from the group by a means other than using the [`dispatch_group_async`](dispatch_group_async.md) function.

A call to this function must balance a call to [`enter()`](dispatchgroup/enter().md). It is invalid to call it more times than [`enter()`](dispatchgroup/enter().md), which would result in a negative count.

## See Also

- [func enter()](dispatchgroup/enter.md)
  Explicitly indicates that a block has entered the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchgroup/leave())*