# App entities

**Framework**: App Intents

Make your app’s core types and data concepts available to the system using app entity types.

#### Overview

App entities provide the system with information about your app’s data, or about concepts related to your app’s data. App entities help the system resolve parameters for app intents by letting it introspect relevant types. For example, a photo app that provides app entities for its photos and albums might also provide app entities to represent “the current photo” or “this album.” These specific app entities help resolve intents more quickly and with fewer verbal interactions.

Define app entities for core types and concepts that you want to make available to system experiences. Add properties for any data values that help people discover entities using queries. For example, add the name of a photo album or the currency amount for a financial transaction.

## Topics

### Essentials
- [Defining app entities for your custom data types](defining-app-entities-for-your-custom-data-types.md)
  Provide the system with information about the types your app uses to model its data so that your intents can use those types as parameters.
- [Making app entities available in Spotlight](making-app-entities-available-in-spotlight.md)
  Update your app entity types to support Spotlight indexing, and donate entities to make them findable in searches.
### App entity types
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
- [protocol OwnershipProvidingEntity](ownershipprovidingentity.md)
  A type that provides the system with ownership and sharing context for an app entity.
- [macro UnionValue()](unionvalue().md)
- [protocol AppUnionValue](appunionvalue.md)
  A protocol that provides nominal type identity and metadata for union values.
- [protocol AppUnionValueCasesProviding](appunionvaluecasesproviding.md)
  A protocol for the cases enumeration of an `AppUnionValue`.
### Entity collections
- [struct EntityCollection](entitycollection.md)
  An array of entity identifiers that you use to improve the efficiency of operations involving large numbers of entities.
### Entity identity
- [struct EntityIdentifier](entityidentifier.md)
  A type that uniquely identifies a specific instance of an app entity.
- [protocol EntityIdentifierConvertible](entityidentifierconvertible.md)
  An interface for converting between an entity’s identifier and its string representation.
- [struct FileEntityIdentifier](fileentityidentifier.md)
  An identifier for an app entity that refers to a document or other file.
- [protocol PersistentlyIdentifiable](persistentlyidentifiable.md)
  Defines a string that uniquely identifies a type. This is useful for maintaining the identity of a type, even when its type name is changed.
- [struct SyncableEntityIdentifier](syncableentityidentifier.md)
  A type-safe wrapper you use to specify different local and stable identifiers for an entity.
- [struct AttributedEntityIdentifier](attributedentityidentifier.md)
  A unique identifier for an app entity instance within an application.
- [struct AttributedTypeIdentifier](attributedtypeidentifier.md)
  A unique identifier for an app entity or transient app entity type within an application bundle.
- [protocol AppEntityAnnotatable](appentityannotatable.md)
  An interface that system types adopt and use to manage their relationship to app entities.
### Entity queries
- [Entity queries](entity-queries.md)
  Implement one or more query types to help the system find your app’s entities.
### Property declarations
- [macro ComputedProperty()](computedproperty().md)
  A macro that adds a computed app entity property with a get accessor and an optional set accessor.
- [macro ComputedProperty(title: LocalizedStringResource)](computedproperty(title:).md)
  A macro that adds a computed app entity property with a get accessor and an optional set accessor.
- [macro ComputedProperty(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](computedproperty(indexingkey:).md)
  A macro that adds a computed app entity property with get and set accessors.
- [macro ComputedProperty(customIndexingKey: CSCustomAttributeKey)](computedproperty(customindexingkey:).md)
  A macro that adds a computed app entity property with a get accessor and an optional set accessor.
- [macro ComputedProperty(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](computedproperty(title:customindexingkey:).md)
  A macro that adds a computed app entity property with a get accessor and an optional set accessor.
- [macro ComputedProperty(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](computedproperty(title:indexingkey:).md)
  A macro that adds a computed app entity property with a get accessor and an optional set accessor.
- [macro DeferredProperty()](deferredproperty().md)
  A macro that adds an asynchronous app entity property with an asynchronous get accessor.
- [macro DeferredProperty(title: LocalizedStringResource)](deferredproperty(title:).md)
  A macro that adds an asynchronous app entity property with an asynchronous get accessor.
- [macro DeferredProperty(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](deferredproperty(indexingkey:).md)
  A macro that adds an asynchronous app entity property with an asynchronous get accessor.
- [macro DeferredProperty(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](deferredproperty(title:indexingkey:).md)
  A macro that adds an asynchronous app entity property with an asynchronous get accessor.
- [class EntityProperty](entityproperty.md)
  A property wrapper that exposes the associated property to the system.
- [struct EntityPropertyModifiers](entitypropertymodifiers.md)
- [Property comparators](property-comparators.md)
  Specify the type of comparison to perform during a property-matched query.
### Data representations
- [struct DisplayRepresentation](displayrepresentation.md)
  A type that describes the user interface presentation of a custom type.
- [protocol DisplayRepresentable](displayrepresentable.md)
  An interface for providing a dynamic visual representation of a specific type and instances of that type.
- [protocol InstanceDisplayRepresentable](instancedisplayrepresentable.md)
  An interface for providing the visual representation for an instance of a specific type.
- [protocol TypeDisplayRepresentable](typedisplayrepresentable.md)
  An interface for providing the visual representation of a specific type.
- [struct TypeDisplayRepresentation](typedisplayrepresentation.md)
  A type that describes the user interface presentation of a custom type.
- [protocol StaticDisplayRepresentable](staticdisplayrepresentable.md)
  An interface for providing a static visual representation of a specific type.
- [protocol CaseDisplayRepresentable](casedisplayrepresentable.md)
  An interface for providing the visual representation for an iterable collection of values.
### Type bridging
- [struct IntentValueRepresentation](intentvaluerepresentation.md)
  A transfer representation that enables bidirectional conversion between app entities and system intent values.
### Universal link navigation
- [protocol URLRepresentableEntity](urlrepresentableentity.md)
  An app entity with a URL representation.
- [struct EntityURLRepresentation](entityurlrepresentation.md)
  The URL representation of an app entity.
- [protocol CustomURLRepresentationParameterConvertible](customurlrepresentationparameterconvertible.md)
### Foundational types
- [protocol AppValue](appvalue.md)
  An interface that describes conceptual types you use in app intents.
- [protocol AnyIntentValue](anyintentvalue.md)
  A type the system uses to access a parameter or property value.

## See Also

- [App intents](app-intents.md)
  Make your app’s custom actions available to the system by using app intent types.
- [App enums](app-enums.md)
  Make your app’s enumerations and predefined values available to the system by using app enum types.
- [Common data types](common-data-types.md)
  Use framework-defined types for common parameter and result data types such as contacts, files, currencies, and more.
- [App extension](app-extension.md)
  Deliver app intents in an app extension or other package that lives outside your app’s code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-entities)*