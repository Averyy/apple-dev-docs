# CNContainerType

**Framework**: Contacts  
**Kind**: enum

The container may be local on the device or associated with a server account that has contacts.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum CNContainerType
```

## Topics

### Constants
- [CNContainerType.local](cncontainertype/local.md)
  A container for contacts only stored locally on the device.
- [CNContainerType.exchange](cncontainertype/exchange.md)
  A container for contacts stored in an Exchange folder from an Exchange server.
- [CNContainerType.cardDAV](cncontainertype/carddav.md)
  A container for contacts stored in an CardDAV server, such as iCloud.
- [CNContainerType.unassigned](cncontainertype/unassigned.md)
  A container where the system hasn’t assigned the container type.
### Initializers
- [init?(rawValue: Int)](cncontainertype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var name: String](cncontainer/name.md)
  The name of the container.
- [var identifier: String](cncontainer/identifier.md)
  The unique identifier for a contacts container on the device.
- [var type: CNContainerType](cncontainer/type.md)
  The type of the container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontainertype)*