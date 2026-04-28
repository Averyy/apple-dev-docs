# StatusManagementDeclarationsDeclarationsObject

**Framework**: Device Management  
**Kind**: dictionary

A collection of the client’s processed declarations.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object StatusManagementDeclarationsDeclarationsObject
```

## Topics

### Objects
- [object StatusManagementDeclarationsDeclarationObject](statusmanagementdeclarationsdeclarationobject.md)
  A processed declaration for the client.

## Properties

- `activations` ([StatusManagementDeclarationsDeclarationObject]) *(required)*: An array of declarations that represent the client’s processed activation types.
- `assets` ([StatusManagementDeclarationsDeclarationObject]) *(required)*: An array of declarations that represent the client’s processed assets.
- `configurations` ([StatusManagementDeclarationsDeclarationObject]) *(required)*: An array of declarations that represent the client’s processed configuration types.
- `management` ([StatusManagementDeclarationsDeclarationObject]) *(required)*: An array of declarations that represent the client’s processed declaration types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusmanagementdeclarationsdeclarationsobject)*