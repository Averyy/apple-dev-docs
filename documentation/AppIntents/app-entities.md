# App entities

**Framework**: App Intents

Make core types or concepts discoverable to the system by declaring them as app entities.

#### Overview

App entities provide the system with information about your app’s data, or about concepts related to your app’s data. App entities help the system resolve parameters for app intents by letting it introspect relevant types. For example, a photo app that provides app entities for its photos and albums might also provide app entities to represent “the current photo” or “this album.” These specific app entities help resolve intents more quickly and with fewer verbal interactions.

Define app entities for core types and concepts that you want to make available to system experiences. Add properties for any data values that help people discover entities using queries. For example, add the name of a photo album or the currency amount for a financial transaction.

## Topics

### Entities
- [Integrating custom data types into your intents](integrating-custom-types-into-your-intents.md)
  Provide the system with information about the types your app uses to model its data so that your intents can use those types as parameters.
- [protocol AppEntity](appentity.md)
  An interface for exposing a custom type or app-specific concept to system experiences like Siri and the Shortcuts app.
- [protocol FileEntity](fileentity.md)
  An entity that refers to a document or other file.
- [protocol IndexedEntity](indexedentity.md)
  `IndexedEntity` represents an App Entity decorated with an attribute set. A set of attributes that enable the system to perform structured indexing  and queries of entities.
- [protocol TransientAppEntity](transientappentity.md)
  A type that represents a transient model object which exposes its interface to App Intents via properties. Note that `TransientAppEntity` types are not meant to be queried.
- [protocol UniqueAppEntity](uniqueappentity.md)
  An entity that will only ever have one value, such as global settings.
- [protocol URLRepresentableEntity](urlrepresentableentity.md)
  An app entity with a URL representation.
### Entity identity
- [protocol PersistentlyIdentifiable](persistentlyidentifiable.md)
  Defines a string that uniquely identifies a type. This is useful for maintaining the identity of a type, even when its type name is changed.
- [struct EntityIdentifier](entityidentifier.md)
  A type that uniquely identifies a specific instance of an app entity.
- [protocol EntityIdentifierConvertible](entityidentifierconvertible.md)
  An interface for converting between an entity’s identifier and its string representation.
### Entity content
- [class EntityProperty](entityproperty.md)
  A property wrapper that exposes the associated property to the system.
- [protocol AppValue](appvalue.md)
  An interface that describes conceptual types you use in app intents.
- [protocol AnyIntentValue](anyintentvalue.md)
  A type the system uses to access a parameter or property value.
- [protocol AppEnum](appenum.md)
  An interface to express that a custom type has a predefined, static set of valid values to display.
- [protocol URLRepresentableEnum](urlrepresentableenum.md)
  An app enum with a URL representation.
### Entity property macros
- [macro ComputedProperty()](computedproperty().md)
  A macro that creates a computed property for an AppEntity that allows for providing a get and/or set accessor
- [macro ComputedProperty(title: LocalizedStringResource)](computedproperty(title:).md)
  A macro that creates a computed property for an AppEntity that allows for providing a get and/or set accessor
- [macro ComputedProperty(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](computedproperty(indexingkey:).md)
  A macro that creates a computed property for an AppEntity that allows for providing a get and/or set accessor
- [macro ComputedProperty(customIndexingKey: CSCustomAttributeKey)](computedproperty(customindexingkey:).md)
  A macro that creates a computed property for an AppEntity that allows for providing a get and/or set accessor
- [macro ComputedProperty(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](computedproperty(title:customindexingkey:).md)
  A macro that creates a computed property for an AppEntity that allows for providing a get and/or set accessor
- [macro ComputedProperty(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](computedproperty(title:indexingkey:).md)
  A macro that creates a computed property for an AppEntity that allows for providing a get and/or set accessor
- [macro DeferredProperty()](deferredproperty().md)
  A macro that creates an async property for an AppEntity that allows for providing an async get accessor
- [macro DeferredProperty(title: LocalizedStringResource)](deferredproperty(title:).md)
  A macro that creates an async property for an AppEntity that allows for providing an async get accessor.
### Entity presentation
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

## See Also

- [Adding parameters to an app intent](adding-parameters-to-an-app-intent.md)
  Enable people to configure app intents with their custom input values.
- [Integrating custom data types into your intents](integrating-custom-types-into-your-intents.md)
  Provide the system with information about the types your app uses to model its data so that your intents can use those types as parameters.
- [Parameter resolution](parameter-resolution.md)
  Define the required parameters for your app intents and specify how to resolve those parameters at runtime.
- [Entity queries](entity-queries.md)
  Help the system find the entities your app defines and use them to resolve parameters.
- [Resolvers](resolvers.md)
  Resolve the parameters of your app intents, and extend the standard resolution types to include your app’s custom types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-entities)*