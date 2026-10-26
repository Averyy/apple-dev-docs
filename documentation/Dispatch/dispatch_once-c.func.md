# dispatch_once

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Executes a block object only once for the lifetime of an application.

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
extern void dispatch_once(dispatch_once_t *predicate, dispatch_block_t block);
```

#### Discussion

This function is useful for initialization of global data (singletons) in an application. Always call this function before using or testing any variables that are initialized by the block.

If called simultaneously from multiple threads, this function waits synchronously until the block has completed.

The predicate must point to a variable stored in global or static scope. The result of using a predicate with automatic or dynamic storage (including Objective-C instance variables) is undefined.

## Parameters

- `predicate`: A pointer to a [`dispatch_once_t`](./dispatch_once_t.md) structure that is used to test whether the block has completed or not.
- `block`: The block object to execute once.

## See Also

### Executing a Task Only Once
- [dispatch_once_f](./dispatch_once_f-c.func.md)
  Executes an application-defined function only once for the lifetime of an application.
- [dispatch_once_t](./dispatch_once_t.md)
  A predicate for use with the `dispatch_once` function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_once-c.func)*