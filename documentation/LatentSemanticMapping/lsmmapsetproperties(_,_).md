# LSMMapSetProperties(_:_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func  
**Role**: Function

Sets a dictionary of properties for the map.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
func LSMMapSetProperties(_ mapref: LSMMap, _ properties: CFDictionary)
```

```c
void LSMMapSetProperties(LSMMapRef mapref, CFDictionaryRef properties);
```

## Discussion

Latent Semantic Mapping makes its own copy of the properties, so you don’t need to retain them past this call.

## See Also

### Managing a Map’s Properties
- [func LSMMapGetProperties(LSMMap) -> Unmanaged<CFDictionary>](./lsmmapgetproperties%28_%29.md)
  Gets a dictionary of properties for the map.
- [Map Properties](./map-properties.md)
  Special properties that determine a map’s behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmmapsetproperties(_:_:))*