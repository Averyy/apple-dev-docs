# NSHashTableZeroingWeakMemory

**Framework**: Foundation  
**Kind**: var  
**Role**: Global Variable

This option has been deprecated. Instead use the `NSHashTableWeakMemory` option. Equal to [`NSPointerFunctionsZeroingWeakMemory`](./nspointerfunctionsoptions/nspointerfunctionszeroingweakmemory.md).

**Availability**:
- macOS 10.5+ - Deprecated in 10.8

## Declaration

```c
static const NSPointerFunctionsOptions NSHashTableZeroingWeakMemory;
```

## Discussion

Note that `NSHashTableWeakMemory` is not entirely equivalent to and compatible with the previous option’s behavior: objects must be weak-reference-safe under manual and automatic reference counting; not all objects are.

## See Also

### Constants
- [var NSHashTableStrongMemory: NSPointerFunctions.Options](./nshashtablestrongmemory.md)
  Equal to [`strongMemory`](./nspointerfunctions/options/strongmemory.md).
- [var NSHashTableCopyIn: NSPointerFunctions.Options](./nshashtablecopyin.md)
  Equal to [`copyIn`](./nspointerfunctions/options/copyin.md).
- [var NSHashTableObjectPointerPersonality: NSPointerFunctions.Options](./nshashtableobjectpointerpersonality.md)
  Equal to [`objectPointerPersonality`](./nspointerfunctions/options/objectpointerpersonality.md).
- [var NSHashTableWeakMemory: NSPointerFunctions.Options](./nshashtableweakmemory.md)
  Equal to [`weakMemory`](./nspointerfunctions/options/weakmemory.md). Uses weak read and write barriers appropriate for ARC or GC. Using [`weakMemory`](./nspointerfunctions/options/weakmemory.md) object references will turn to `NULL` on last release.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshashtablezeroingweakmemory)*