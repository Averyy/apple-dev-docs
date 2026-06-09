# SyncableEntity

**Framework**: App Intents  
**Kind**: protocol

An interface that indicates your entity has an identifier that’s consistent across devices.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
protocol SyncableEntity : AppEntity
```

## Mentions

- [Defining app entities for your custom data types](defining-app-entities-for-your-custom-data-types.md)

#### Overview

Adopt the `SyncableEntity` protocol in your entity types when they have an identifier that’s the same across devices. The presence of this protocol tells the system that it can refer to your entity consistently across devices. For eample, Siri uses this capability to transfer a conversation from one device to another.

If you configure entities with an identifier that’s already consistent across devices, you can adopt this protocol without any additional changes. For example, if you initialize entities with a UUID you retrieve from your server, you can use that value for the identifier and not make any additional changes to your type. The following example shows an app entity type that adopts `SyncableEntity` and uses a server-based UUID.

```swift
struct Article: AppEntity, SyncableEntity {
    var id: UUID  // No changes needed!
    var title: String
}
```

If your entity maintains different local and stable identifiers, adopt this protocol and set the type of your identifier to [`SyncableEntityIdentifier`](syncableentityidentifier.md). When creating an entity, initialize its `id` property with both the local and stable identifier values for your type, as shown in the following example. When you need to refer to an entity in your code, use the local identifier.

```swift
struct Photo: AppEntity, SyncableEntity {
    var id: SyncableEntityIdentifier<String, String>
    var creationDate: Date

    init(localID: String, stableID: String, creationDate: Date) {
        self.id = SyncableEntityIdentifier(local: localID, stable: stableID)
        self.creationDate = creationDate
    }
}
```

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
- [protocol TransientAppEntity](transientappentity.md)
  A type that represents a transient model object which exposes its interface to App Intents via properties. Note that `TransientAppEntity` types are not meant to be queried.
- [protocol UniqueAppEntity](uniqueappentity.md)
  An entity that will only ever have one value, such as global settings.
- [protocol OwnershipProvidingEntity](ownershipprovidingentity.md)
  A type that provides the system with ownership and sharing context for an app entity.
- [macro UnionValue()](unionvalue().md)
- [protocol AppUnionValue](appunionvalue.md)
  A protocol that provides nominal type identity and metadata for union values.
- [protocol AppUnionValueCasesProviding](appunionvaluecasesproviding.md)
  A protocol for the cases enumeration of an `AppUnionValue`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/syncableentity)*