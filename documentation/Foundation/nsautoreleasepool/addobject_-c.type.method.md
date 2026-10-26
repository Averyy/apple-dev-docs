# addObject:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Adds a given object to the active autorelease pool in the current thread.

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
+ (void) addObject:(id) anObject;
```

#### Discussion

The same object may be added several times to the active pool and, when the pool is deallocated, it will receive a [`release`](../../ObjectiveC/nsobject-c.protocol/release.md) message for each time it was added.

Normally you don’t invoke this method directly—you send [`autorelease`](../../ObjectiveC/nsobject-c.protocol/autorelease.md) to `object` instead.

## Parameters

- `anObject`: The object to add to the active autorelease pool in the current thread.

## See Also

### Adding an Object to a Pool
- [- addObject:](./addobject_-c.method.md)
  Adds a given object to the receiver


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsautoreleasepool/addobject:-c.type.method)*