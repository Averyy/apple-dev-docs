# dispatch_source_testcancel

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Tests whether the given dispatch source has been canceled.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern intptr_t dispatch_source_testcancel(dispatch_source_t source);
```

#### Return Value

Non-zero if canceled and zero if not canceled.

#### Discussion

Your application can use this function to test whether a dispatch source object has been canceled by a call to [`dispatch_source_cancel`](./dispatch_source_cancel.md). The result of this function is non-zero immediately after [`dispatch_source_cancel`](./dispatch_source_cancel.md) has been called.

## Parameters

- `source`: The dispatch source to be tested. This parameter cannot be `NULL`.

## See Also

### Canceling a Dispatch Source
- [dispatch_source_cancel](./dispatch_source_cancel.md)
  Asynchronously cancels the dispatch source, preventing any further invocation of its event handler block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_source_testcancel)*