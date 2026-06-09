# resolved(from:)

**Framework**: App Intents Testing  
**Kind**: method

Resolves an entity from an exported intent file through the entity type’s transferable conformance.

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
func resolved(from file: IntentFile) async throws -> AnyAppEntity
```

#### Return Value

The resolved entity.

#### Discussion

Use this to verify the import direction — that an [`IntentFile`](https://developer.apple.com/documentation/AppIntents/IntentFile) produced by `AnyAppEntity/exported(as:)-swift.method` (or constructed from test data) can be resolved back into an entity through the same pipeline used at runtime.

> **Note**: If the entity type does not support the file’s content type.

```swift
let file = try await entity.exported(as: .json)
let resolved = try await coffeeOrderDef.resolved(from: file)
```

## Parameters

- `file`: The `<doc://com.apple.documentation/documentation/appintents/intentfile>` containing the exported entity data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appentitydefinition/resolved(from:)-2fld0)*