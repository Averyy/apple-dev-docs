# PKPassLibraryNotificationName

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct

The types of notifications that the pass library posts.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct PKPassLibraryNotificationName
```

## Topics

### Creating a pass library notification name
- [init(rawValue: String)](pkpasslibrarynotificationname/init(rawvalue:).md)
  Creates a pass library notification name according to the provided raw value.
- [init(String)](pkpasslibrarynotificationname/init(_:).md)
  Creates a pass library notification name according to the provided string.
### Notification names
- [static let PKPassLibraryDidChange: PKPassLibraryNotificationName](pkpasslibrarynotificationname/pkpasslibrarydidchange.md)
  A notification that PassKit posts when the pass library changes.
- [static let PKPassLibraryRemotePaymentPassesDidChange: PKPassLibraryNotificationName](pkpasslibrarynotificationname/pkpasslibraryremotepaymentpassesdidchange.md)
  A notification that PassKit posts when it adds or removes a pass on a paired remote device.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct PKPassLibraryNotificationKey](pkpasslibrarynotificationkey.md)
  The user info keys that a pass library notification uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrarynotificationname)*