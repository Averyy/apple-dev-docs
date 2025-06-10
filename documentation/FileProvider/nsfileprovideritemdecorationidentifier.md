# NSFileProviderItemDecorationIdentifier

**Framework**: File Provider  
**Kind**: struct

A decoration identifier defined in the File Provider extension’s information property list.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct NSFileProviderItemDecorationIdentifier
```

## Topics

### Creating Decoration Identifiers
- [init(String)](nsfileprovideritemdecorationidentifier/init(_:).md)
  Returns a new decoration identifier matching the provided String.
- [init(rawValue: String)](nsfileprovideritemdecorationidentifier/init(rawvalue:).md)
  Returns a new decoration identifier matching the provided value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct NSFileProviderItemFields](nsfileprovideritemfields.md)
  Fields that specify which of the item’s properties have changed.
- [class NSFileProviderItemVersion](nsfileprovideritemversion.md)
  The version of the item’s content and its metadata.
- [class NSFileProviderRequest](nsfileproviderrequest.md)
  An object that provides information about the application requesting data from the File Provider extension.
- [protocol NSFileProviderItemDecorating](nsfileprovideritemdecorating.md)
  Support for decorating items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemdecorationidentifier)*