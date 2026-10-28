# disableCollectorForPointer:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Specifies that a given pointer will not be collected.

**Availability**:
- macOS 10.5+ - Deprecated in 10.10

## Declaration

```objc
- (void) disableCollectorForPointer:(const void *) ptr;
```

## Discussion

You use this method to ensure that memory at a given address will not be collected. You can use this, for example, to create new root objects:

```objc
NSMutableDictionary *globalDictionary;
globalDictionary = [NSMutableDictionary dictionary];
[[NSGarbageCollector defaultCollector]
    disableCollectorForPointer:globalDictionary];
```

The new dictionary will not be collectable and will persist for the lifetime of the application unless it is subsequently passed as the argument to [`enableCollectorForPointer:`](./enablecollectorforpointer_.md). For more about root objects and scanned memory, see Garbage Collection Programming Guide.

## Parameters

- `ptr`: A pointer to the memory that should not be collected.

## See Also

### Manipulating External References
- [- enableCollectorForPointer:](./enablecollectorforpointer_.md)
  Specifies that a given pointer may be collected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsgarbagecollector/disablecollectorforpointer:)*