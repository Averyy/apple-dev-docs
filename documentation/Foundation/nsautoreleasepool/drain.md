# drain

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

In a reference-counted environment, releases and pops the receiver; in a garbage-collected environment, triggers garbage collection if the memory allocated since the last collection is greater than the current threshold.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
- (void) drain;
```

## Discussion

In a reference-counted environment, this method behaves the same as [`release`](../../ObjectiveC/nsobject-c.protocol/release.md). Since an autorelease pool cannot be retained (see [`NSAutoreleasePool`](../nsautoreleasepool.md)), this therefore causes the receiver to be deallocated. When an autorelease pool is deallocated, it sends a [`release`](../../ObjectiveC/nsobject-c.protocol/release.md) message to all its autoreleased objects. If an object is added several times to the same pool, when the pool is deallocated it receives a [`release`](../../ObjectiveC/nsobject-c.protocol/release.md) message for each time it was added.

### Special Considerations

In a garbage-collected environment, `release` is a no-op, so unless you do not want to give the collector a hint it is important to use [`drain`](./drain.md) in any code that may be compiled for a garbage-collected environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsautoreleasepool/drain)*