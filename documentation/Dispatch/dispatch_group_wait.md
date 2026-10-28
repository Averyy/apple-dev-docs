# dispatch_group_wait

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Waits synchronously for the previously submitted block objects to finish; returns if the blocks do not complete before the specified timeout period has elapsed.

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
extern intptr_t dispatch_group_wait(dispatch_group_t group, dispatch_time_t timeout);
```

## Return Value

Returns zero on success (all blocks associated with the group completed before the specified timeout) or non-zero on error (timeout occurred).

## Discussion

This function waits for the completion of the blocks associated with the given dispatch group and returns when either all blocks have completed or the specified timeout has elapsed. When a timeout occurs, the group is restored to its original state.

This function returns immediately if the dispatch group is empty (there are no blocks associated with the group).

After the successful return of this function, the dispatch group is empty, and can be reused for additional blocks. See [`dispatch_group_async`](./dispatch_group_async.md) for more information.

If your app isn’t using ARC, you should call [`dispatch_release`](./dispatch_release.md) on a dispatch group when it’s no longer needed.

## Parameters

- `group`: The dispatch group to wait on. This parameter cannot be `NULL`.
- `timeout`: When to timeout (see [`dispatch_time`](./dispatch_time.md)). The [`DISPATCH_TIME_NOW`](./dispatch_time_now.md) and [`DISPATCH_TIME_FOREVER`](./dispatch_time_forever.md) constants are provided as a convenience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_group_wait)*