# cancel()

**Framework**: Dispatch  
**Kind**: method

Cancels the current work item asynchronously.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst ?+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func cancel()
```

#### Discussion

Cancellation causes future attempts to execute the work item to return immediately. Cancellation does not affect the execution of a work item that has already begun.

Release of any resources associated with the block object is delayed until execution of the block object is next attempted (or any execution already in progress completes).

> **Note**:  Take care to ensure that a work item does not capture any resources that require execution of the block body in order to be released, such as memory allocated with `malloc(3)` on which the block body calls `free(3)`. Such resources are leaked if the block body is never executed due to cancellation.

 Take care to ensure that a work item does not capture any resources that require execution of the block body in order to be released, such as memory allocated with `malloc(3)` on which the block body calls `free(3)`. Such resources are leaked if the block body is never executed due to cancellation.

## See Also

- [var isCancelled: Bool](dispatchworkitem/iscancelled.md)
  A Boolean value indicating whether the work item has been canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchworkitem/cancel())*