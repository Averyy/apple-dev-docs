# NSZoneFromPointer

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Gets the zone for a given block of memory.

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
extern NSZone *NSZoneFromPointer(void *ptr);
```

#### Return Value

The zone for the block of memory indicated by `pointer`, or `NULL` if the block was not allocated from a zone.

#### Discussion

`pointer` must be one that was returned by a prior call to an allocation function.

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
- [NSZoneMalloc](./nszonemalloc.md)
  Allocates memory in a zone.
- [NSZoneName](./nszonename.md)
  Returns the name of the specified zone.
- [NSZoneRealloc](./nszonerealloc.md)
  Allocates memory in a zone.
- [NSDefaultMallocZone](./nsdefaultmalloczone.md)
  Returns the default zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nszonefrompointer)*