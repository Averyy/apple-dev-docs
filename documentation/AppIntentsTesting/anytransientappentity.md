# AnyTransientAppEntity

**Framework**: App Intents Testing  
**Kind**: struct  
**Role**: Structure

A type-erased representation of a transient app entity that provides dynamic property access.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@dynamicMemberLookup
struct AnyTransientAppEntity
```

#### Overview

Use `AnyTransientAppEntity` to work with transient entities when you don’t know the specific entity type at compile time.

```swift
// Getting transient entity definitions.
let definitions = IntentDefinitions(bundleIdentifier: "com.apple.example")
let sessionEntity = definitions.transientEntities["UserSessionEntity"]

// Creating a transient entity with properties.
var entity = sessionEntity.withProperties(
    name: "John Doe",
    age: 30
)

// Accessing properties with type safety.
let userName: String? = try entity.name
let userAge: Int? = try entity.age

// Accessing nested properties (requires try).
if try entity.profile.name == "John Doe" {
    print("User found")
}
```

## Topics

### Identifying the entity type
- [var entityType: AttributedTypeIdentifier](./anytransientappentity/entitytype.md)
  The type of transient app entity represented by this identifier.
### Instance Methods
- [func exported<T>(as: T.Type) async throws -> T](./anytransientappentity/exported%28as%29-2rmw6.md)
  Exports this transient entity as a transferable intent value type.
- [func exported(as: UTType?) async throws -> IntentFile](./anytransientappentity/exported%28as%29-7mrbg.md)
  Exports this transient entity’s content as an `IntentFile`.
- [func exported<T>(as: T.Type) async throws -> T](./anytransientappentity/exported%28as%29-8zhnu.md)
  Exports this transient entity as a system intent value type.
### Subscripts
- [subscript(dynamicMember _: String) -> (any IntentValueExpressing)?](./anytransientappentity/subscript%28dynamicmember%29-5ygut.md)
  Accesses an entity property by name, without casting.
- [subscript(dynamicMember _: String) -> DynamicPropertyPath](./anytransientappentity/subscript%28dynamicmember%29-63vyv.md)
  Accesses a nested entity property by name.
- [subscript<T>(dynamicMember _: String) -> T](./anytransientappentity/subscript%28dynamicmember%29-8pfwv.md)
  Accesses an entity property by name, for comparison with a known value.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [IntentValueConvertible](../AppIntents/intentvalueconvertible.md)
- [IntentValueExpressing](../AppIntents/intentvalueexpressing.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Intermediate types
- [struct AnyAppIntent](./anyappintent.md)
  A type-erased, intermediate representation of an app intent for testing purposes.
- [struct AnyAppEntity](./anyappentity.md)
  A type-erased, intermediate representation of your app entity for testing purposes.
- [struct AnyEntityQuery](./anyentityquery.md)
  A type-erased, intermediate representation of your entity query for testing purposes.
- [struct AnyAppEnum](./anyappenum.md)
  A type-erased representation of an app enumeration that provides dynamic enumeration value access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/anytransientappentity)*