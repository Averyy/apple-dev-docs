# NSMakeCollectable

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Makes a newly allocated Core Foundation object eligible for collection.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

> **Deprecated**: Garbage collection is deprecated in OS X v10.8; instead,you should use AutomaticReference Counting—see [Transitioning to ARC Release Notes](https://developer.apple.com/library/archive/releasenotes/ObjectiveC/RN-TransitioningToARC/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011226).

## Declaration

```c
static idNSMakeCollectable(CFTypeRef cf);
```

## Discussion

This function is a wrapper for [`CFMakeCollectable`](../CoreFoundation/cfmakecollectable.md), but its return type is `id`—avoiding the need for casting when using Cocoa objects.

This function may be useful when returning Core Foundation objects in code that must support both garbage-collected and non-garbage-collected environments, as illustrated in the following example.

```objc
- (CFDateRef)foo {
    CFDateRef aCFDate;
    // ...
    return [NSMakeCollectable(aCFDate) autorelease];
}
```

CFTypeRef style objects are garbage collected, yet only sometime after the last [`CFRelease`](../CoreFoundation/cfrelease.md) is performed. Particularly for fully-bridged CFTypeRef objects such as CFStrings and collections (such as CFDictionary), you must call either `CFMakeCollectable` or the more type safe `NSMakeCollectable`, preferably right upon allocation.

## See Also

### Legacy
- [NSGarbageCollector](./nsgarbagecollector.md)
  A convenient interface to the garbage collection system.
- [NSAllocateCollectable](./nsallocatecollectable.md)
  Allocates collectable memory.
- [NSReallocateCollectable](./nsreallocatecollectable.md)
  Reallocates collectable memory.
- [Memory Allocation Options](./api-1539826-memory-allocation-options.md)
  Constants used to control behavior when allocating or reallocating collectible memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmakecollectable)*