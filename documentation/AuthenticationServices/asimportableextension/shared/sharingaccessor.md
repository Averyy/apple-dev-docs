# ASImportableExtension.Shared.SharingAccessor

**Framework**: Authentication Services  
**Kind**: struct

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
struct SharingAccessor
```

## Topics

### Initializers
- [init(type: ASImportableExtension.Shared.SharingAccessor.AccessorType, accountID: Data, name: String, permissions: [ASImportableExtension.Shared.SharingAccessor.Permission])](asimportableextension/shared/sharingaccessor/init(type:accountid:name:permissions:).md)
### Instance Properties
- [var accountID: Data](asimportableextension/shared/sharingaccessor/accountid.md)
  The ID of the account that has been granted access to this shared entity.
- [var name: String](asimportableextension/shared/sharingaccessor/name.md)
  The name of the accessor’s account.
- [var permissions: [ASImportableExtension.Shared.SharingAccessor.Permission]](asimportableextension/shared/sharingaccessor/permissions.md)
  The permissions given to this accessor.
- [var type: ASImportableExtension.Shared.SharingAccessor.AccessorType](asimportableextension/shared/sharingaccessor/type.md)
  The type of accessor.
### Enumerations
- [ASImportableExtension.Shared.SharingAccessor.AccessorType](asimportableextension/shared/sharingaccessor/accessortype.md)
- [ASImportableExtension.Shared.SharingAccessor.Permission](asimportableextension/shared/sharingaccessor/permission.md)

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportableextension/shared/sharingaccessor)*