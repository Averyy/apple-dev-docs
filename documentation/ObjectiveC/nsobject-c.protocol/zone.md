# zone

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Zones are deprecated and ignored by most classes that have it as a parameter.

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
- (struct _NSZone *) zone;
```

## Return Value

A pointer to the zone from which the receiver was allocated.

## See Also

### Obsolete Methods
- [- retain](./retain.md)
  Increments the receiver’s reference count.
- [- release](./release.md)
  Decrements the receiver’s reference count.
- [- autorelease](./autorelease.md)
  Decrements the receiver’s retain count at the end of the current autorelease pool block.
- [- retainCount](./retaincount.md)
  Do not use this method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-c.protocol/zone)*