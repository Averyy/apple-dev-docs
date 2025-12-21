# NSHashTableWeakMemory

**Framework**: Foundation  
**Kind**: var

Equal to [`weakMemory`](nspointerfunctions/options/weakmemory.md). Uses weak read and write barriers appropriate for ARC or GC. Using [`weakMemory`](nspointerfunctions/options/weakmemory.md) object references will turn to `NULL` on last release.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let NSHashTableWeakMemory: NSPointerFunctions.Options
```

## See Also

- [let NSHashTableStrongMemory: NSPointerFunctions.Options](nshashtablestrongmemory.md)
  Equal to [`strongMemory`](nspointerfunctions/options/strongmemory.md).
- [let NSHashTableCopyIn: NSPointerFunctions.Options](nshashtablecopyin.md)
  Equal to [`copyIn`](nspointerfunctions/options/copyin.md).
- [let NSHashTableObjectPointerPersonality: NSPointerFunctions.Options](nshashtableobjectpointerpersonality.md)
  Equal to [`objectPointerPersonality`](nspointerfunctions/options/objectpointerpersonality.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshashtableweakmemory)*