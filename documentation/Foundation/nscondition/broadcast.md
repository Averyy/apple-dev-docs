# broadcast()

**Framework**: Foundation  
**Kind**: method

Signals the condition, waking up all threads waiting on it.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func broadcast()
```

#### Discussion

If no threads are waiting on the condition, this method does nothing.

To avoid race conditions, you should invoke this method only while the receiver is locked.

## See Also

- [func signal()](nscondition/signal.md)
  Signals the condition, waking up one thread waiting on it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscondition/broadcast())*