# activate()

**Framework**: Dispatch  
**Kind**: method  
**Role**: Instance Method

Activates the dispatch object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func activate()
```

```c
extern void dispatch_activate(dispatch_object_t object);
```

## Discussion

Once a dispatch object has been activated, it cannot change its target queue.

## See Also

### Activating, Suspending, and Resuming
- [func resume()](./resume%28%29.md)
  Resumes the invocation of block objects on a dispatch object.
- [func suspend()](./suspend%28%29.md)
  Suspends the invocation of block objects on a dispatch object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchobject/activate())*