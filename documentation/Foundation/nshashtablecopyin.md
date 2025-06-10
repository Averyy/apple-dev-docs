# NSHashTableCopyIn

**Framework**: Foundation  
**Kind**: var

Equal to [`copyIn`](nspointerfunctions/options/copyin.md).

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let NSHashTableCopyIn: NSPointerFunctions.Options
```

## See Also

- [let NSHashTableStrongMemory: NSPointerFunctions.Options](nshashtablestrongmemory.md)
  Equal to [`strongMemory`](nspointerfunctions/options/strongmemory.md).
- [let NSHashTableObjectPointerPersonality: NSPointerFunctions.Options](nshashtableobjectpointerpersonality.md)
  Equal to [`objectPointerPersonality`](nspointerfunctions/options/objectpointerpersonality.md).
- [let NSHashTableWeakMemory: NSPointerFunctions.Options](nshashtableweakmemory.md)
  Equal to [`weakMemory`](nspointerfunctions/options/weakmemory.md). Uses weak read and write barriers appropriate for ARC or GC. Using [`weakMemory`](nspointerfunctions/options/weakmemory.md) object references will turn to `NULL` on last release.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshashtablecopyin)*