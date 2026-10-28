# activate()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) activate;
```

## Discussion

Connections start in an inactive state. You must call [`activate()`](./activate%28%29.md) on a connection before it can send or receive any messages.

Calling [`activate()`](./activate%28%29.md) on an active connection has no effect.

For backward compatibility reasons, calling [`resume()`](./resume%28%29.md) on an inactive and otherwise not suspended [`NSXPCListener`](../nsxpclistener.md) has the same effect as calling [`activate()`](./activate%28%29.md). For new code, prefer [`activate()`](./activate%28%29.md).

## See Also

### Managing connection state
- [func resume()](./resume%28%29.md)
  Starts processing of incoming requests.
- [func invalidate()](./invalidate%28%29.md)
  Invalidates the listener.
- [func suspend()](./suspend%28%29.md)
  Suspends the listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpclistener/activate())*