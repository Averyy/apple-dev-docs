# SystemExtensions.AllowedSystemExtensions

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that maps team identifiers to bundle identifiers that are allowed.

**Availability**:
- macOS 10.15+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object SystemExtensions.AllowedSystemExtensions
```

## Properties

- `ANY` ([string]): The mapping of team identifiers to arrays of bundle identifiers, where the bundle identifier is that of the system extension to be installed.

## See Also

- [object SystemExtensions.AllowedSystemExtensionTypes](systemextensions/allowedsystemextensiontypes-data.dictionary.md)
  A dictionary that maps team identifiers to system extensions.
- [object SystemExtensions.NonRemovableFromUISystemExtensions](systemextensions/nonremovablefromuisystemextensions-data.dictionary.md)
  A dictionary that maps team identifiers to bundle identifiers of extensions that are non-removable.
- [object SystemExtensions.NonRemovableSystemExtensions](systemextensions/nonremovablesystemextensions-data.dictionary.md)
  A dictionary that maps team identifiers to bundle identifiers of extensions that are non-removable.
- [object SystemExtensions.RemovableSystemExtensions](systemextensions/removablesystemextensions-data.dictionary.md)
  A dictionary that maps team identifiers to bundle identifiers of extensions that are removable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/systemextensions/allowedsystemextensions-data.dictionary)*