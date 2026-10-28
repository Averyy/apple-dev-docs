# resume()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) resume;
```

## Discussion

All listeners start suspended and must be resumed before they begin processing incoming requests.

If called on the [`service()`](./service%28%29.md) object, this method never returns. Therefore, you should call it as the last step inside the XPC service’s `main` function after setting up any desired initial state and configuring the listener itself.

If called on any other [`NSXPCListener`](../nsxpclistener.md), the connection is resumed, and the method returns immediately.

## See Also

### Managing connection state
- [func activate()](./activate%28%29.md)
  Activates the listener.
- [func invalidate()](./invalidate%28%29.md)
  Invalidates the listener.
- [func suspend()](./suspend%28%29.md)
  Suspends the listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpclistener/resume())*