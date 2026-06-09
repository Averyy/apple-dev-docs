# DeclarationItemsResponse

**Framework**: Device Management  
**Kind**: dictionary

The set of available declarations on the server.

## Declaration

```swift
object DeclarationItemsResponse
```

## Topics

### Supporting Objects
- [object DeclarationItemsResponse.ManifestDeclarationItems](declarationitemsresponse/manifestdeclarationitems.md)
  The dictionary that contains the lists of declarations available on the server.
- [object ManifestDeclaration](manifestdeclaration.md)
  A dictionary that describes a declaration.

## Properties

- `Declarations` (DeclarationItemsResponse.ManifestDeclarationItems) *(required)*: The set of available declarations on the server.
- `DeclarationsToken` (string) *(required)*: The current value of the declarations token. Clients use this to detect when declarations change so they can refetch the token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/declarationitemsresponse)*