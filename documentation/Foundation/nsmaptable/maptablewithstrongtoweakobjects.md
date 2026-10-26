# mapTableWithStrongToWeakObjects

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a new map table object which has strong references to the keys and weak references to the values.

**Availability**:
- macOS 10.5+ - Deprecated in 10.8

> **Deprecated**: Use [`strongToWeakObjects()`](./strongtoweakobjects%28%29.md) instead.

## Declaration

```objc
+ (id) mapTableWithStrongToWeakObjects;
```

#### Return Value

A new map table object which has strong references to the keys and weak references to the values.

#### Discussion

`NSMapTable` objects created using this method do not support weak references under Automatic Reference Counting (ARC).

## See Also

### Deprecated
- [+ mapTableWithStrongToStrongObjects](./maptablewithstrongtostrongobjects.md)
  Returns a new map table object which has strong references to the keys and values.
- [+ mapTableWithWeakToStrongObjects](./maptablewithweaktostrongobjects.md)
  Returns a new map table object which has weak references to the keys and strong references to the values.
- [+ mapTableWithWeakToWeakObjects](./maptablewithweaktoweakobjects.md)
  Returns a new map table object which has weak references to the keys and values.
- [Legacy Map Table Implementation](../legacy-map-table-implementation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmaptable/maptablewithstrongtoweakobjects)*