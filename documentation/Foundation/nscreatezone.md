# NSCreateZone

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Creates a new zone.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

> **Deprecated**: Zones are ignored on iOS and 64-bit runtime in macOS. You should not use zones in current development.

## Declaration

```c
extern NSZone *NSCreateZone(NSUInteger startSize, NSUInteger granularity, BOOL canFree);
```

#### Return Value

A pointer to a new zone of `startSize` bytes, which will grow and shrink by `granularity` bytes. If `canFree` is 0, the allocator will never free memory, and `malloc` will be fast. Returns `NULL` if a new zone could not be created.

## See Also

### Managing Zones
- [NSRecycleZone](./nsrecyclezone.md)
  Frees memory in a zone.
- [NSSetZoneName](./nssetzonename.md)
  Sets the name of the specified zone.
- [NSZoneCalloc](./nszonecalloc.md)
  Allocates memory in a zone.
- [NSZoneFree](./nszonefree.md)
  Deallocates a block of memory in the specified zone.
- [NSZoneFromPointer](./nszonefrompointer.md)
  Gets the zone for a given block of memory.
- [NSZoneMalloc](./nszonemalloc.md)
  Allocates memory in a zone.
- [NSZoneName](./nszonename.md)
  Returns the name of the specified zone.
- [NSZoneRealloc](./nszonerealloc.md)
  Allocates memory in a zone.
- [NSDefaultMallocZone](./nsdefaultmalloczone.md)
  Returns the default zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscreatezone)*