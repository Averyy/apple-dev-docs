# SystemExtensions.AllowedSystemExtensionTypes

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

A dictionary that maps team identifiers to system extensions.

**Availability**:
- macOS 10.15+

## Declaration

```
object SystemExtensions.AllowedSystemExtensionTypes
```

## Properties

- `ANY` ([string]): The mapping of team identifier to an array of strings, where each string is a type of system extension that you can install for that team identifier.

## See Also

### Objects
- [object SystemExtensions.AllowedSystemExtensions](./allowedsystemextensions-data.dictionary.md)
  A dictionary that maps team identifiers to bundle identifiers that are allowed.
- [object SystemExtensions.NonRemovableFromUISystemExtensions](./nonremovablefromuisystemextensions-data.dictionary.md)
  A dictionary that maps team identifiers to bundle identifiers of extensions that are non-removable.
- [object SystemExtensions.NonRemovableSystemExtensions](./nonremovablesystemextensions-data.dictionary.md)
  A dictionary that maps team identifiers to bundle identifiers of extensions that are non-removable.
- [object SystemExtensions.RemovableSystemExtensions](./removablesystemextensions-data.dictionary.md)
  A dictionary that maps team identifiers to bundle identifiers of extensions that are removable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/systemextensions/allowedsystemextensiontypes-data.dictionary)*