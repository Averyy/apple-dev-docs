# enableCollectorForPointer:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Specifies that a given pointer may be collected.

**Availability**:
- macOS 10.5+ - Deprecated in 10.10

## Declaration

```objc
- (void) enableCollectorForPointer:(const void *) ptr;
```

## Discussion

You use this method to make memory that was previously marked as uncollectable. For example, given the address of the global dictionary created in [`disableCollectorForPointer:`](./disablecollectorforpointer_.md), you could make the dictionary collectable as follows:

```objc
[[NSGarbageCollector defaultCollector]
    enableCollectorForPointer:globalDictionary];
```

For more about root objects and scanned memory, see Garbage Collection Programming Guide.

## Parameters

- `ptr`: A pointer to the memory that may be collected.

## See Also

### Manipulating External References
- [- disableCollectorForPointer:](./disablecollectorforpointer_.md)
  Specifies that a given pointer will not be collected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsgarbagecollector/enablecollectorforpointer:)*