# AppUnionValue

**Framework**: App Intents  
**Kind**: protocol

A protocol that provides nominal type identity and metadata for union values.

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
protocol AppUnionValue : TypeDisplayRepresentable
```

#### Overview

Union values conforming to this protocol can be used as Shortcuts parameters with rich metadata support, enabling appropriate picker UI and parameter summaries.

The `@UnionValue` macro automatically generates conformance to this protocol. You can provide custom metadata by implementing the protocol requirements in an extension.

Example:

```swift
@UnionValue
enum Reaction {
    case tapback(Tapback)
    case text(String)
}

extension Reaction {
    static var typeDisplayRepresentation: TypeDisplayRepresentation {
        "Reaction"
    }

    static let caseDisplayRepresentations: [Cases: DisplayRepresentation] = [
        .tapback: "Tapback",
        .text: "Text Reaction"
    ]
}
```

## Topics

### Associated Types
- [associatedtype Cases : AppUnionValueCasesProviding](appunionvalue/cases.md)
  The nominal type representing the cases of this union value.
### Type Properties
- [static var caseDisplayRepresentations: [Self.Cases : DisplayRepresentation]](appunionvalue/casedisplayrepresentations.md)
  A dictionary that maps each case to the visual elements that represent it.

## Relationships

### Inherits From
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
- [protocol OwnershipProvidingEntity](ownershipprovidingentity.md)
  A type that provides the system with ownership and sharing context for an app entity.
- [macro UnionValue()](unionvalue().md)
- [protocol AppUnionValueCasesProviding](appunionvaluecasesproviding.md)
  A protocol for the cases enumeration of an `AppUnionValue`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appunionvalue)*