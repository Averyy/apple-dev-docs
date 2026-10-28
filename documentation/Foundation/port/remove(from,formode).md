# remove(from:forMode:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

This method should be implemented by a subclass to stop monitoring of a port when removed from a give run loop in a given input mode.

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
func remove(from runLoop: RunLoop, forMode mode: RunLoop.Mode)
```

```objc
- (void) removeFromRunLoop:(NSRunLoop *) runLoop forMode:(NSRunLoopMode) mode;
```

## Discussion

This method should not be called directly.

## Parameters

- `runLoop`: The run loop from which to remove the receiver.
- `mode`: The run loop mode from which to remove the receiver

## See Also

### Port monitoring
- [func schedule(in: RunLoop, forMode: RunLoop.Mode)](./schedule%28in,formode%29.md)
  This method should be implemented by a subclass to set up monitoring of a port when added to a given run loop in a given input mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/port/remove(from:formode:))*