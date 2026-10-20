# SystemExtensions.RemovableSystemExtensions

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

A dictionary that maps team identifiers to bundle identifiers of extensions that are removable.

**Availability**:
- macOS 12.0+

## Declaration

```
object SystemExtensions.RemovableSystemExtensions
```

## Properties

- `ANY` ([string]): The dictionary maps team identifiers (keys) to arrays of bundle identifiers, where the bundle identifier defines the system extension.

## See Also

### Objects
- [object SystemExtensions.AllowedSystemExtensionTypes](./allowedsystemextensiontypes-data.dictionary.md)
  A dictionary that maps team identifiers to system extensions.
- [object SystemExtensions.AllowedSystemExtensions](./allowedsystemextensions-data.dictionary.md)
  A dictionary that maps team identifiers to bundle identifiers that are allowed.
- [object SystemExtensions.NonRemovableFromUISystemExtensions](./nonremovablefromuisystemextensions-data.dictionary.md)
  A dictionary that maps team identifiers to bundle identifiers of extensions that are non-removable.
- [object SystemExtensions.NonRemovableSystemExtensions](./nonremovablesystemextensions-data.dictionary.md)
  A dictionary that maps team identifiers to bundle identifiers of extensions that are non-removable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/systemextensions/removablesystemextensions-data.dictionary)*