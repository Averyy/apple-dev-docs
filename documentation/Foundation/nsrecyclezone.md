# NSRecycleZone

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Frees memory in a zone.

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
extern void NSRecycleZone(NSZone *zone);
```

## Discussion

Frees `zone` after adding any of its pointers still in use to the default zone. (This strategy prevents retained objects from being inadvertently destroyed.)

## See Also

### Managing Zones
- [NSCreateZone](./nscreatezone.md)
  Creates a new zone.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsrecyclezone)*