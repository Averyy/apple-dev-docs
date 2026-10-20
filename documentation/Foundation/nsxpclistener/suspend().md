# suspend()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) suspend;
```

#### Discussion

As you cannot invalidate a suspended listener, every call to [`suspend()`](./suspend%28%29.md) that you make must be balanced by a call to [`resume()`](./resume%28%29.md).

## See Also

### Managing connection state
- [func activate()](./activate%28%29.md)
  Activates the listener.
- [func resume()](./resume%28%29.md)
  Starts processing of incoming requests.
- [func invalidate()](./invalidate%28%29.md)
  Invalidates the listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpclistener/suspend())*