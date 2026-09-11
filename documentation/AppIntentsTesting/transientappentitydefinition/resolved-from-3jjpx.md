# resolved(from:)

**Framework**: App Intents Testing  
**Kind**: method

Resolves a transient entity from a system intent value type through the entity type’s `Transferable` conformance.

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
func resolved<T>(from value: T) async throws -> AnyTransientAppEntity where T : _SystemIntentValue, T : IntentValueConvertible
```

#### Return Value

The resolved transient entity.

#### Discussion

> **Note**: If the entity type does not support the given value type.

## Parameters

- `value`: The system intent value (e.g., a `PlaceDescriptor` instance).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/transientappentitydefinition/resolved(from:)-3jjpx)*