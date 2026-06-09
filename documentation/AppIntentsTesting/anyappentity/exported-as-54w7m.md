# exported(as:)

**Framework**: App Intents Testing  
**Kind**: method

Exports this entity as a system intent value type.

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