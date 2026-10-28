# NSDefaultMallocZone

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Returns the default zone.

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
extern NSZone *NSDefaultMallocZone();
```

## Return Value

The default zone, which is created automatically at startup.

## Discussion

This zone is used by the standard C function `malloc`.

## See Also

### Managing Zones
- [NSCreateZone](./nscreatezone.md)
  Creates a new zone.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdefaultmalloczone)*