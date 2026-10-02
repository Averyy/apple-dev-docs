# UniqueAppEntity

**Framework**: App Intents  
**Kind**: protocol

An AppEntity subtype for entities that only have a single instance.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
protocol UniqueAppEntity : AppEntity where Self.DefaultQuery : UniqueAppEntityQuery
```

#### Overview

If an entity type only ever has one value, use the `UniqueAppEntity` protocol and the related `UniqueAppEntityQuery`.  For example, app-global settings might be represented using an entity of this type.  The protocols will implement several required methods for you and allow the system to present the entity differently in some contexts.  For example, Shortcuts will not generate a “Find” action for that entity type.

An entity conforming to `UniqueAppEntity` must have a `defaultQuery` type that conforms to `UniqueAppEntityQuery`, which has a single required method, `uniqueEntity`, and uses that to provide implementations of the other required query methods.  If you require a separate query definition, such as because it uses `@Dependency`, it would look like this:

```swift
struct MyEntity: UniqueAppEntity {
    static var defaultQuery = MyQuery()
}

struct MyQuery: UniqueAppEntityQuery {
    typealias Entity = MyEntity

    func uniqueEntity() -> Entity { ... }
}
```

If your query type has no requirements other than the `uniqueEntity` method, you may use the simplified `UniqueAppEntityProvider` type, like this:

```swift
struct MyEntity: UniqueAppEntity {
    static var defaultQuery = UniqueAppEntityProvider {
        ...
    }
}
```

The provider instance will call the supplied block to get the entity value when needed.

An entity that will only ever have one value, such as global settings.

## Relationships

### Inherits From
- [AppEntity](appentity.md)
- [AppValue](appvalue.md)
- [CustomLocalizedStringResourceConvertible](../foundation/customlocalizedstringresourceconvertible.md)
- [DisplayRepresentable](displayrepresentable.md)
- [Identifiable](../swift/identifiable.md)
- [InstanceDisplayRepresentable](instancedisplayrepresentable.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
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
- [protocol OwnershipProvidingEntity](ownershipprovidingentity.md)
  A type that provides the system with ownership and sharing context for an app entity.
- [macro UnionValue()](unionvalue().md)
- [protocol AppUnionValue](appunionvalue.md)
  A protocol that provides nominal type identity and metadata for union values.
- [protocol AppUnionValueCasesProviding](appunionvaluecasesproviding.md)
  A protocol for the cases enumeration of an `AppUnionValue`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/uniqueappentity)*