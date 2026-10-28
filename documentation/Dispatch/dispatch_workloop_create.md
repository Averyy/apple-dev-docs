# dispatch_workloop_create

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Creates a new workloop with the specified label.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```c
extern dispatch_workloop_tdispatch_workloop_create(const char *label);
```

## Return Value

The newly created workloop.

## Discussion

The returned workloop is active, and you may submit blocks to it immediately.

## Parameters

- `label`: A string label to attach to the queue to uniquely identify it in debugging tools such as Instruments, `sample`, stackshots, and crash reports.  Because apps, libraries, and frameworks can all create their own dispatch queues, a reverse-DNS naming style (`com.example.myqueue`) is recommended.  This parameter is optional and can be `NULL`.

## See Also

### Creating a Dispatch Workloop
- [dispatch_workloop_create_inactive](./dispatch_workloop_create_inactive.md)
  Creates a new inactive workloop with the specified label.
- [typealias dispatch_workloop_t](./dispatch_workloop_t.md)
  A dispatch queue that prioritizes the execution of tasks based on their quality-of-service level.
- [OS_dispatch_workloop](./os_dispatch_workloop.md)
  A dispatch queue that prioritizes the execution of tasks based on their quality-of-service level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_workloop_create)*