# release

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Decrements the receiver’s reference count.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```objc
- (void) release;
```

## Discussion

The receiver is sent a [`dealloc`](../nsobject-swift.class/dealloc.md) message when its reference count reaches `0`.

You would only implement this method to define your own reference-counting scheme. Such implementations should not invoke the inherited method; that is, they should not include a release message to `super`.

For more information on the reference counting mechanism, see [Advanced Memory Management Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/MemoryMgmt.html#//apple_ref/doc/uid/10000011i).

### Special Considerations

Instead of using manual reference counting, you should adopt ARC—see [Transitioning to ARC Release Notes](https://developer.apple.com/library/archive/releasenotes/ObjectiveC/RN-TransitioningToARC/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011226).

## See Also

### Obsolete Methods
- [- retain](./retain.md)
  Increments the receiver’s reference count.
- [- autorelease](./autorelease.md)
  Decrements the receiver’s retain count at the end of the current autorelease pool block.
- [- retainCount](./retaincount.md)
  Do not use this method.
- [- zone](./zone.md)
  Zones are deprecated and ignored by most classes that have it as a parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-c.protocol/release)*