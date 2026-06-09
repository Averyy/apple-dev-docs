# exported(as:)

**Framework**: App Intents Testing  
**Kind**: method

Exports this transient entity’s content as an `IntentFile`.

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
func exported(as contentType: UTType? = nil) async throws -> IntentFile
```

#### Return Value

The exported content as an `IntentFile`.

#### Discussion

When no content type is specified, the entity’s first registered `TransferRepresentation` is used.

The exported file can be passed as a parameter to another intent or used to verify the entity’s export format. To resolve exported content back into an entity, use `AppEntityDefinition/resolved(from:)-8f2x` on a non-transient entity definition — transient entities are not resolvable by design since they have no stable identifier.

> **Note**: If the entity does not conform to `Transferable` or does not support the requested format.

## Parameters

- `contentType`: The desired export format (e.g., `.json`, `.png`). Pass `nil` to use the entity’s default representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/anytransientappentity/exported(as:)-7mrbg)*