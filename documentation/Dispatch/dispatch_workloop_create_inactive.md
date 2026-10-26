# dispatch_workloop_create_inactive

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Creates a new inactive workloop with the specified label.

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
extern dispatch_workloop_tdispatch_workloop_create_inactive(const char *label);
```

#### Return Value

The newly created workloop.

#### Discussion

Use this function when you want to change the default behavior of the workloop before activating it. For example, use this method if you call [`dispatch_set_qos_class_floor`](./dispatch_set_qos_class_floor.md) to configure the minimum quality of service level.

After configuring the workloop, you must call [`activate()`](./dispatchobject/activate%28%29.md) before submitting any blocks to it. If you submit blocks to an inactive workloop, the system terminates the current process.

## Parameters

- `label`: A string label to attach to the queue to uniquely identify it in debugging tools such as Instruments, `sample`, stackshots, and crash reports.  Because apps, libraries, and frameworks can all create their own dispatch queues, a reverse-DNS naming style (`com.example.myqueue`) is recommended. This parameter is optional and can be `NULL`.

## See Also

### Creating a Dispatch Workloop
- [dispatch_workloop_create](./dispatch_workloop_create.md)
  Creates a new workloop with the specified label.
- [typealias dispatch_workloop_t](./dispatch_workloop_t.md)
  A dispatch queue that prioritizes the execution of tasks based on their quality-of-service level.
- [OS_dispatch_workloop](./os_dispatch_workloop.md)
  A dispatch queue that prioritizes the execution of tasks based on their quality-of-service level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_workloop_create_inactive)*