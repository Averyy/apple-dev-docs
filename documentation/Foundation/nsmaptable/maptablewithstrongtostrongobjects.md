# mapTableWithStrongToStrongObjects

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a new map table object which has strong references to the keys and values.

**Availability**:
- macOS 10.5+ - Deprecated in 10.8

> **Deprecated**: Use [`strongToStrongObjects()`](./strongtostrongobjects%28%29.md) instead.

## Declaration

```objc
+ (id) mapTableWithStrongToStrongObjects;
```

#### Return Value

A new map table object which has strong references to the keys and values.

## See Also

### Deprecated
- [+ mapTableWithWeakToStrongObjects](./maptablewithweaktostrongobjects.md)
  Returns a new map table object which has weak references to the keys and strong references to the values.
- [+ mapTableWithStrongToWeakObjects](./maptablewithstrongtoweakobjects.md)
  Returns a new map table object which has strong references to the keys and weak references to the values.
- [+ mapTableWithWeakToWeakObjects](./maptablewithweaktoweakobjects.md)
  Returns a new map table object which has weak references to the keys and values.
- [Legacy Map Table Implementation](../legacy-map-table-implementation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmaptable/maptablewithstrongtostrongobjects)*