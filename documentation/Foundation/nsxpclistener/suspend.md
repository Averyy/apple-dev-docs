# suspend()

**Framework**: Foundation  
**Kind**: method

Suspends the listener.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func suspend()
```

#### Discussion

As you cannot invalidate a suspended listener, every call to [`suspend()`](nsxpclistener/suspend().md) that you make must be balanced by a call to [`resume()`](nsxpclistener/resume().md).

## See Also

- [func activate()](nsxpclistener/activate.md)
  Activates the listener.
- [func resume()](nsxpclistener/resume.md)
  Starts processing of incoming requests.
- [func invalidate()](nsxpclistener/invalidate.md)
  Invalidates the listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpclistener/suspend())*