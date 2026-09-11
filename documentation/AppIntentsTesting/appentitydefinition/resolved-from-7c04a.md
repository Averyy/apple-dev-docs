# resolved(from:)

**Framework**: App Intents Testing  
**Kind**: method

Resolves an entity from a transferable intent value type through the entity type’s transferable conformance.

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
func resolved<T>(from value: T) async throws -> AnyAppEntity where T : IntentValueConvertible, T : Transferable
```

#### Return Value

The resolved entity.

#### Discussion

The value is serialized through its `TransferRepresentation` and resolved into the entity type through the same pipeline used at runtime.

> **Note**: If the entity type does not support the given value type.

```swift
let person = try await entity.exported(as: IntentPerson.self)
let resolved = try await personEntityDef.resolved(from: person)
```

## Parameters

- `value`: The transferable intent value (e.g., an `IntentPerson` instance).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appentitydefinition/resolved(from:)-7c04a)*