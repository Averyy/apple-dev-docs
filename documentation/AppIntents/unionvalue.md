# UnionValue()

**Framework**: App Intents  
**Kind**: macro

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@attached
(extension, conformances: _IntentValueRepresentable, AppUnionValue, names: arbitrary) macro UnionValue()
```

## Mentions

- [Adding parameters to an app intent](adding-parameters-to-an-app-intent.md)
- [Defining app entities for your custom data types](defining-app-entities-for-your-custom-data-types.md)

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
- [protocol OwnershipProvidingEntity](ownershipprovidingentity.md)
  A type that provides the system with ownership and sharing context for an app entity.
- [protocol AppUnionValue](appunionvalue.md)
  A protocol that provides nominal type identity and metadata for union values.
- [protocol AppUnionValueCasesProviding](appunionvaluecasesproviding.md)
  A protocol for the cases enumeration of an `AppUnionValue`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/unionvalue())*