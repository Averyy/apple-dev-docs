# AnyAppEntity

**Framework**: App Intents Testing  
**Kind**: struct

A type-erased, intermediate representation of your app entity for testing purposes.

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
@dynamicMemberLookup
struct AnyAppEntity
```

## Mentions

- [Testing your App Intents code](testing-your-app-intents-code.md)

#### Overview

The `AnyAppEntity` structure resolves to your actual entity type and gives you access to its properties, enabling you to test your app entity code:

```swift
// Define your app entity type from your app bundle:
let definitions = IntentDefinitions(
    bundleIdentifier: "com.apple.example"
)
let exampleEntity = definitions.entities[
    "ExampleEntity"
]

// Create an entity from an identifier.
let entity = exampleEntity.makeReference(
    identifier: "my-example"
)

// Type-safe access to the entity's properties.
let name: String? = entity.name
let itemCount: Int? = entity.itemCount

// Accessing nested properties (requires try).
if try entity.profile.name == "John Doe" {
    print("User found")
}
```

## Topics

### Identifying the entity
- [var identifier: AttributedEntityIdentifier](anyappentity/identifier.md)
  The value that uniquely identifies the app entity.
### Instance Methods
- [func exported<T>(as: T.Type) async throws -> T](anyappentity/exported(as:)-54w7m.md)
  Exports this entity as a system intent value type.
- [func exported<T>(as: T.Type) async throws -> T](anyappentity/exported(as:)-7pg2q.md)
  Exports this entity as a transferable intent value type.
- [func exported(as: UTType?) async throws -> IntentFile](anyappentity/exported(as:)-8qa8k.md)
  Exports this entity’s content as an `IntentFile`.
### Subscripts
- [subscript(dynamicMember _: String) -> (any IntentValueExpressing)?](anyappentity/subscript(dynamicmember:)-4bdp1.md)
  Accesses an entity property by name, without casting.
- [subscript<T>(dynamicMember _: String) -> T](anyappentity/subscript(dynamicmember:)-5twll.md)
  Accesses an entity property by name, for comparison with a known value.
- [subscript(dynamicMember _: String) -> DynamicPropertyPath](anyappentity/subscript(dynamicmember:)-yuv.md)
  Accesses a nested entity property by name.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [IntentValueConvertible](../appintents/intentvalueconvertible.md)
- [IntentValueExpressing](../appintents/intentvalueexpressing.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct AnyAppIntent](anyappintent.md)
  A type-erased, intermediate representation of an app intent for testing purposes.
- [struct AnyEntityQuery](anyentityquery.md)
  A type-erased, intermediate representation of your entity query for testing purposes.
- [struct AnyAppEnum](anyappenum.md)
  A type-erased representation of an app enumeration that provides dynamic enumeration value access.
- [struct AnyTransientAppEntity](anytransientappentity.md)
  A type-erased representation of a transient app entity that provides dynamic property access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/anyappentity)*