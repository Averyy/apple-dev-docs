# OwnershipProvidingEntity

**Framework**: App Intents  
**Kind**: protocol

A type that provides the system with ownership and sharing context for an app entity.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
protocol OwnershipProvidingEntity : AppEntity
```

#### Overview

When your app passes app entities as parameters to an [`AppIntent`](appintent.md) and returns them from app intent results, people can use Apple Intelligence, Siri, and custom shortcuts to work with those entities across apps. For destructive or sensitive actions like deleting or updating an app entity, your app can require a person’s confirmation. Additionally, Apple Intelligence and Siri may also request a person’s confirmation. Conform your app entities to [`OwnershipProvidingEntity`](ownershipprovidingentity.md) so the system prompts for confirmation — with appropriate context in the confirmation dialog — when an intent acts on shared or publicly accessible app entities.

The following example shows an app entity for a photo album that updates its [`ownership`](ownershipprovidingentity/ownership.md) based on whether a person shares the album with their family or publishes it publicly:

```swift
@AppEntity(schema: .photos.album)
struct PhotoAlbumEntity: OwnershipProvidingEntity {
    let id = UUID()
    var isSharedWithFamily: Bool
    var isPublicAlbum: Bool

    // MARK: - .photos.album properties
    var name: String
    var creationDate: Date?
    var albumType: PhotoAlbumType

    var ownership: EntityOwnership {
        var ownership: EntityOwnership = []
        if isSharedWithFamily {
            ownership.insert(.shared)
        }
        if isPublicAlbum {
            ownership.insert(.public)
        }
        return ownership
    }
}
```

## Topics

### Instance Properties
- [var ownership: EntityOwnership](ownershipprovidingentity/ownership.md)
  The sharing and ownership state of the entity.

## Relationships

### Inherits From
- [AppEntity](appentity.md)
- [AppValue](appvalue.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/CustomLocalizedStringResourceConvertible.md)
- [DisplayRepresentable](displayrepresentable.md)
- [Identifiable](../Swift/Identifiable.md)
- [InstanceDisplayRepresentable](instancedisplayrepresentable.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TypeDisplayRepresentable](typedisplayrepresentable.md)

## See Also

- [protocol AppEntity](appentity.md)
  An interface for making a custom type or app-specific concept discoverable by Apple Intelligence and experiences like Siri or the Shortcuts app.
- [protocol FileEntity](fileentity.md)
  An entity that refers to a document or other file.
- [protocol IndexedEntity](indexedentity.md)
  An interface that allows you to include an entity in your app’s Spotlight index.
- [protocol SyncableEntity](syncableentity.md)
  An interface that indicates your entity has an identifier that’s consistent across devices.
- [protocol TransientAppEntity](transientappentity.md)
  A type that represents a transient model object which exposes its interface to App Intents via properties. Note that `TransientAppEntity` types are not meant to be queried.
- [protocol UniqueAppEntity](uniqueappentity.md)
  An entity that will only ever have one value, such as global settings.
- [macro UnionValue()](unionvalue().md)
- [protocol AppUnionValue](appunionvalue.md)
  A protocol that provides nominal type identity and metadata for union values.
- [protocol AppUnionValueCasesProviding](appunionvaluecasesproviding.md)
  A protocol for the cases enumeration of an `AppUnionValue`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/ownershipprovidingentity)*