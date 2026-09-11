# AnyEntityQuery

**Framework**: App Intents Testing  
**Kind**: struct

A type-erased, intermediate representation of your entity query for testing purposes.

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
struct AnyEntityQuery
```

#### Overview

The `AnyEntityQuery` structure resolves to your concrete query type, and allows you to test your entity queries and verify their results as shown in the following example:

```swift
let landmarkDef = definitions.entities["LandmarkEntity"]

// Query by string.
let stringQueryResults = try await landmarkDef.entities(matching: "Yosemite")

// Query by identifiers.
let specific = try await landmarkDef.entities(identifiers: ["yosemite-falls"])

// Get all entities.
let all = try await landmarkDef.allEntities()
```

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct AnyAppIntent](anyappintent.md)
  A type-erased, intermediate representation of an app intent for testing purposes.
- [struct AnyAppEntity](anyappentity.md)
  A type-erased, intermediate representation of your app entity for testing purposes.
- [struct AnyAppEnum](anyappenum.md)
  A type-erased representation of an app enumeration that provides dynamic enumeration value access.
- [struct AnyTransientAppEntity](anytransientappentity.md)
  A type-erased representation of a transient app entity that provides dynamic property access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/anyentityquery)*