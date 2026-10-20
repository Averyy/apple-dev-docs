# invalidate()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Invalidates the listener.

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
func invalidate()
```

```objc
- (void) invalidate;
```

#### Discussion

After calling this method, no more connections are created. Once a listener is invalidated it may not be resumed or suspended.

## See Also

### Managing connection state
- [func activate()](./activate%28%29.md)
  Activates the listener.
- [func resume()](./resume%28%29.md)
  Starts processing of incoming requests.
- [func suspend()](./suspend%28%29.md)
  Suspends the listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpclistener/invalidate())*