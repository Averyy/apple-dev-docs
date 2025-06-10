# AppLibrary.App

**Framework**: MarketplaceKit  
**Kind**: class

Information about an app that someone installs from a marketplace, including its ID and installation status.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
final class App
```

## Topics

### Structures
- [AppLibrary.App.Installation](applibrary/app/installation-swift.struct.md)
- [AppLibrary.App.Metadata](applibrary/app/metadata.md)
### Operators
- [static func == (AppLibrary.App, AppLibrary.App) -> Bool](applibrary/app/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](applibrary/app/hashvalue.md)
  The hash value.
- [let id: AppleItemID](applibrary/app/id-swift.property.md)
  The stable identity of the entity associated with this instance.
- [var installation: AppLibrary.App.Installation?](applibrary/app/installation-swift.property.md)
- [var installationError: MarketplaceKitError?](applibrary/app/installationerror.md)
  An error that occurs during the installation of an app that resides on a marketplace.
- [var installedMetadata: AppLibrary.App.Metadata?](applibrary/app/installedmetadata.md)
- [var isInstalled: Bool](applibrary/app/isinstalled.md)
- [var isInstalling: Bool](applibrary/app/isinstalling.md)
- [var isUpdating: Bool](applibrary/app/isupdating.md)
### Instance Methods
- [func hash(into: inout Hasher)](applibrary/app/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [AppLibrary.App.ID](applibrary/app/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Default Implementations
- [Equatable Implementations](applibrary/app/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/app)*