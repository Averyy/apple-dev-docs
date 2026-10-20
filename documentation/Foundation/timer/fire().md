# fire()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Causes the timer’s message to be sent to its target.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func fire()
```

```objc
- (void) fire;
```

#### Discussion

You can use this method to fire a repeating timer without interrupting its regular firing schedule. If the timer is non-repeating, it is automatically invalidated after firing, even if its scheduled fire date has not arrived.

## See Also

### Related Documentation
- [func invalidate()](./invalidate%28%29.md)
  Stops the timer from ever firing again and requests its removal from its run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/timer/fire())*