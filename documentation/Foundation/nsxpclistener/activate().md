# activate()

**Framework**: Foundation  
**Kind**: method

Activates the listener.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func activate()
```

#### Discussion

Connections start in an inactive state. You must call [`activate()`](nsxpclistener/activate().md) on a connection before it can send or receive any messages.

Calling [`activate()`](nsxpclistener/activate().md) on an active connection has no effect.

For backward compatibility reasons, calling [`resume()`](nsxpclistener/resume().md) on an inactive and otherwise not suspended [`NSXPCListener`](nsxpclistener.md) has the same effect as calling [`activate()`](nsxpclistener/activate().md). For new code, prefer [`activate()`](nsxpclistener/activate().md).

## See Also

- [func resume()](nsxpclistener/resume.md)
  Starts processing of incoming requests.
- [func invalidate()](nsxpclistener/invalidate.md)
  Invalidates the listener.
- [func suspend()](nsxpclistener/suspend.md)
  Suspends the listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpclistener/activate())*