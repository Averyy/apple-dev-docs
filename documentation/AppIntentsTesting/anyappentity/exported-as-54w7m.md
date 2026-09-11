# exported(as:)

**Framework**: App Intents Testing  
**Kind**: method

Exports this entity as a system intent value type.

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
func exported<T>(as type: T.Type) async throws -> T where T : _SystemIntentValue, T : IntentValueConvertible
```

#### Return Value

An instance of the requested type.

#### Discussion

Use this for system-provided currency types that conform to `_SystemIntentValue`, such as `PlaceDescriptor`. The entity must declare a `ValueRepresentation` for the requested type.

> **Note**: If the entity does not support the requested value conversion.

## Parameters

- `type`: The target system intent value type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/anyappentity/exported(as:)-54w7m)*