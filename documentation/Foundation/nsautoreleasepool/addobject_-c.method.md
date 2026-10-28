# addObject:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Adds a given object to the receiver

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
- (void) addObject:(id) anObject;
```

## Discussion

The same object may be added several times to the same pool; when the pool is deallocated, the object will receive a [`release`](../../ObjectiveC/nsobject-c.protocol/release.md) message for each time it was added.

Normally you don’t invoke this method directly—you send [`autorelease`](../../ObjectiveC/nsobject-c.protocol/autorelease.md) to `object` instead.

## Parameters

- `anObject`: The object to add to the receiver.

## See Also

### Adding an Object to a Pool
- [+ addObject:](./addobject_-c.type.method.md)
  Adds a given object to the active autorelease pool in the current thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsautoreleasepool/addobject:-c.method)*