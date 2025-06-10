# NSHashTableOptions

**Framework**: Foundation  
**Kind**: typealias

Components in a bit-field to specify the behavior of elements in an [`NSHashTable`](nshashtable.md) object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
typealias NSHashTableOptions = Int
```

## Topics

### Constants
- [let NSHashTableStrongMemory: NSPointerFunctions.Options](nshashtablestrongmemory.md)
  Equal to [`strongMemory`](nspointerfunctions/options/strongmemory.md).
- [let NSHashTableCopyIn: NSPointerFunctions.Options](nshashtablecopyin.md)
  Equal to [`copyIn`](nspointerfunctions/options/copyin.md).
- [let NSHashTableObjectPointerPersonality: NSPointerFunctions.Options](nshashtableobjectpointerpersonality.md)
  Equal to [`objectPointerPersonality`](nspointerfunctions/options/objectpointerpersonality.md).
- [let NSHashTableWeakMemory: NSPointerFunctions.Options](nshashtableweakmemory.md)
  Equal to [`weakMemory`](nspointerfunctions/options/weakmemory.md). Uses weak read and write barriers appropriate for ARC or GC. Using [`weakMemory`](nspointerfunctions/options/weakmemory.md) object references will turn to `NULL` on last release.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshashtableoptions)*