# LSMMapGetProperties(_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func  
**Role**: Function

Gets a dictionary of properties for the map.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
func LSMMapGetProperties(_ mapref: LSMMap) -> Unmanaged<CFDictionary>
```

```c
CFDictionaryRefLSMMapGetProperties(LSMMapRef mapref);
```

## Discussion

Latent Semantic Mapping retains ownership of this dictionary; don’t release it.

## See Also

### Managing a Map’s Properties
- [func LSMMapSetProperties(LSMMap, CFDictionary)](./lsmmapsetproperties%28_,_%29.md)
  Sets a dictionary of properties for the map.
- [Map Properties](./map-properties.md)
  Special properties that determine a map’s behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmmapgetproperties(_:))*