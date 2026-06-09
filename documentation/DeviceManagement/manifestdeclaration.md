# ManifestDeclaration

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes a declaration.

## Declaration

```swift
object ManifestDeclaration
```

## Properties

- `Identifier` (string) *(required)*: The declaration’s identifier.
- `ServerToken` (string) *(required)*: The `ServerToken` value of the declaration. The client uses this to determine if the actual payload is different from the one on the client. Servers must compute the token over the entire declaration content to ensure the value always changes whenever there’s any change to the content.

## See Also

- [object DeclarationItemsResponse.ManifestDeclarationItems](declarationitemsresponse/manifestdeclarationitems.md)
  The dictionary that contains the lists of declarations available on the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/manifestdeclaration)*