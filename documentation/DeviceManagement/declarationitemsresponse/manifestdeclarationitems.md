# DeclarationItemsResponse.ManifestDeclarationItems

**Framework**: Device Management  
**Kind**: dictionary

The dictionary that contains the lists of declarations available on the server.

## Declaration

```swift
object DeclarationItemsResponse.ManifestDeclarationItems
```

## Topics

### Supporting Objects
- [object ManifestDeclaration](manifestdeclaration.md)
  A dictionary that describes a declaration.

## Properties

- `Activations` ([ManifestDeclaration]) *(required)*: The list of available activation declarations on the server.
- `Assets` ([ManifestDeclaration]) *(required)*: The list of available asset declarations on the server.
- `Configurations` ([ManifestDeclaration]) *(required)*: The list of available configuration declarations on the server.
- `Management` ([ManifestDeclaration]) *(required)*: The list of available management declarations on the server.

## See Also

- [object ManifestDeclaration](manifestdeclaration.md)
  A dictionary that describes a declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/declarationitemsresponse/manifestdeclarationitems)*