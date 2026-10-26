# hashTableWithWeakObjects

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a new hash table for storing weak references to its contents.

**Availability**:
- macOS 10.5+ - Deprecated in 10.8

> **Deprecated**: Use [`weakObjects()`](./weakobjects%28%29.md) instead.

## Declaration

```objc
+ (id) hashTableWithWeakObjects;
```

#### Return Value

A new has table that uses the options [`NSHashTableZeroingWeakMemory`](../nshashtablezeroingweakmemory.md) and [`objectPersonality`](../nspointerfunctions/options/objectpersonality.md) and has an initial capacity of `0`.

#### Discussion

This method is not supported under Automatic Reference Counting (ARC).

## See Also

### Deprecated
- [Legacy Hash Table Implementation](../legacy-hash-table-implementation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshashtable/hashtablewithweakobjects)*