# objectZone

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

This method is present for historical reasons and has no effect.

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
- (NSZone *) objectZone;
```

#### Discussion

`NSCoder`’s implementation returns the default memory zone, as given by `NSDefaultMallocZone()`.

## See Also

### Managing Zones
- [- setObjectZone:](./setobjectzone_.md)
  This method is present for historical reasons and has no effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/objectzone)*