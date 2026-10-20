# SystemExtensions.AllowedSystemExtensions

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

A dictionary that maps team identifiers to bundle identifiers that are allowed.

**Availability**:
- macOS 10.15+

## Declaration

```
object SystemExtensions.AllowedSystemExtensions
```

## Properties

- `ANY` ([string]): The mapping of team identifiers to arrays of bundle identifiers, where the bundle identifier defines the system extension to install.

## See Also

### Objects
- [object SystemExtensions.AllowedSystemExtensionTypes](./allowedsystemextensiontypes-data.dictionary.md)
  A dictionary that maps team identifiers to system extensions.
- [object SystemExtensions.NonRemovableFromUISystemExtensions](./nonremovablefromuisystemextensions-data.dictionary.md)
  A dictionary that maps team identifiers to bundle identifiers of extensions that are non-removable.
- [object SystemExtensions.NonRemovableSystemExtensions](./nonremovablesystemextensions-data.dictionary.md)
  A dictionary that maps team identifiers to bundle identifiers of extensions that are non-removable.
- [object SystemExtensions.RemovableSystemExtensions](./removablesystemextensions-data.dictionary.md)
  A dictionary that maps team identifiers to bundle identifiers of extensions that are removable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/systemextensions/allowedsystemextensions-data.dictionary)*