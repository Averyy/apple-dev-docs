# resume()

**Framework**: Foundation  
**Kind**: method

Starts processing of incoming requests.

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
func resume()
```

#### Discussion

All listeners start suspended and must be resumed before they begin processing incoming requests.

If called on the [`service()`](nsxpclistener/service().md) object, this method never returns. Therefore, you should call it as the last step inside the XPC service’s `main` function after setting up any desired initial state and configuring the listener itself.

If called on any other [`NSXPCListener`](nsxpclistener.md), the connection is resumed, and the method returns immediately.

## See Also

- [func activate()](nsxpclistener/activate.md)
  Activates the listener.
- [func invalidate()](nsxpclistener/invalidate.md)
  Invalidates the listener.
- [func suspend()](nsxpclistener/suspend.md)
  Suspends the listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpclistener/resume())*