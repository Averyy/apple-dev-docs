# resolved(from:)

**Framework**: App Intents Testing  
**Kind**: method

Resolves a transient entity from a transferable intent value type through the entity type’s `Transferable` conformance.

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
func resolved<T>(from value: T) async throws -> AnyTransientAppEntity where T : IntentValueConvertible, T : Transferable
```

#### Return Value

The resolved transient entity.

#### Discussion

The value is serialized through its `TransferRepresentation` and resolved into the transient entity type through the same pipeline used at runtime.

> **Note**: If the entity type does not support the given value type.

```swift
let person = try await transientEntity.exported(as: IntentPerson.self)
let resolved = try await sessionEntityDef.resolved(from: person)
```

## Parameters

- `value`: The transferable intent value (e.g., an `IntentPerson` instance).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/transientappentitydefinition/resolved(from:)-1lap2)*