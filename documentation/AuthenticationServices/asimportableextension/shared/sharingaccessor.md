# ASImportableExtension.Shared.SharingAccessor

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

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
- [init(type: ASImportableExtension.Shared.SharingAccessor.AccessorType, accountID: Data, name: String, permissions: [ASImportableExtension.Shared.SharingAccessor.Permission])](./sharingaccessor/init%28type,accountid,name,permissions%29.md)
### Instance Properties
- [var accountID: Data](./sharingaccessor/accountid.md)
  The ID of the account that has been granted access to this shared entity.
- [var name: String](./sharingaccessor/name.md)
  The name of the accessor’s account.
- [var permissions: [ASImportableExtension.Shared.SharingAccessor.Permission]](./sharingaccessor/permissions.md)
  The permissions given to this accessor.
- [var type: ASImportableExtension.Shared.SharingAccessor.AccessorType](./sharingaccessor/type.md)
  The type of accessor.
### Enumerations
- [ASImportableExtension.Shared.SharingAccessor.AccessorType](./sharingaccessor/accessortype.md)
- [ASImportableExtension.Shared.SharingAccessor.Permission](./sharingaccessor/permission.md)

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportableextension/shared/sharingaccessor)*