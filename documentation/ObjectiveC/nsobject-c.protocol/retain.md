# retain

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Increments the receiver’s reference count.

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
- (instancetype) retain;
```

## Return Value

`self`.

## Discussion

You send an object a [`retain`](./retain.md) message when you want to prevent it from being deallocated until you have finished using it.

An object is deallocated automatically when its reference count reaches `0`. [`retain`](./retain.md) messages increment the reference count, and [`release`](./release.md) messages decrement it. For more information on this mechanism, see [Advanced Memory Management Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/MemoryMgmt.html#//apple_ref/doc/uid/10000011i).

As a convenience, [`retain`](./retain.md) returns `self` because it may be used in nested expressions.

You would implement this method only if you were defining your own reference-counting scheme. Such implementations must return `self` and should not invoke the inherited method by sending a [`retain`](./retain.md) message to `super`.

### Special Considerations

Instead of using manual reference counting, you should adopt ARC—see [Transitioning to ARC Release Notes](https://developer.apple.com/library/archive/releasenotes/ObjectiveC/RN-TransitioningToARC/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011226).

## See Also

### Obsolete Methods
- [- release](./release.md)
  Decrements the receiver’s reference count.
- [- autorelease](./autorelease.md)
  Decrements the receiver’s retain count at the end of the current autorelease pool block.
- [- retainCount](./retaincount.md)
  Do not use this method.
- [- zone](./zone.md)
  Zones are deprecated and ignored by most classes that have it as a parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-c.protocol/retain)*