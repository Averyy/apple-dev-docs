# IntentValueRepresentation

**Framework**: App Intents  
**Kind**: struct

A transfer representation that enables bidirectional conversion between app entities and system intent values.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
struct IntentValueRepresentation<Item, IntentValue> where Item : Transferable, IntentValue : _IntentValue, IntentValue : Sendable
```

## Mentions

- [Defining app entities for your custom data types](defining-app-entities-for-your-custom-data-types.md)
- [Providing contextual cues to Apple Intelligence and Siri](providing-contextual-cues-to-apple-intelligence-and-siri.md)

#### Overview

`IntentValueRepresentation` bridges the gap between your custom `AppEntity` types and system-provided intent values (like `IntentPerson`, `PlaceDescriptor`, and other `_SystemIntentValue` types).

#### Export and Import

You can create a representation that supports export only, or both export and import:

```swift
// Export only
ValueRepresentation(
    exporting: { entity in
        IntentPerson(name: .displayName(entity.name))
    }
)

// Bidirectional
ValueRepresentation(
    exporting: { entity in
        IntentPerson(name: .displayName(entity.name))
    },
    importing: { person in
        ContactEntity(name: person.name.displayString)
    }
)
```

#### Key Path Based Export

For entities that directly contain a system intent value property, you can use a simplified key path syntax:

```swift
struct LocationEntity: TransientAppEntity, Transferable {
    @Property
    var place: PlaceDescriptor

    static var transferRepresentation: some TransferRepresentation {
        ValueRepresentation(exporting: \.place)
    }
}
```

## Topics

### Initializers
- [init(exporting: (Item) async throws -> IntentValue)](intentvaluerepresentation/init(exporting:)-2woe8.md)
  Creates a value representation that exports an entity to a system intent value.
- [init(exporting: (Item) async throws -> IntentValue)](intentvaluerepresentation/init(exporting:)-7wi2e.md)
  Creates a value representation that exports an entity to an `IntentPerson`.
- [init(exporting: (Item) async throws -> IntentValue, importing: (IntentValue) async throws -> Item)](intentvaluerepresentation/init(exporting:importing:)-4zz9c.md)
  Creates a value representation that supports bidirectional conversion between an entity and a system intent value.
- [init(exporting: (Item) async throws -> IntentValue, importing: (IntentValue) async throws -> Item)](intentvaluerepresentation/init(exporting:importing:)-550j7.md)
  an entity and an `IntentPerson`.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [TransferRepresentation](../coretransferable/transferrepresentation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentvaluerepresentation)*