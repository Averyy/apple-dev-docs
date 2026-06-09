# resolved(from:)

**Framework**: App Intents Testing  
**Kind**: method

Resolves a transient entity from an exported `IntentFile` through the entity type’s `Transferable` conformance.

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
func resolved(from file: IntentFile) async throws -> AnyTransientAppEntity
```

#### Return Value

The resolved transient entity.

#### Discussion

Use this to verify the import direction — that an `IntentFile` produced by `AnyTransientAppEntity/exported(as:)-swift.method` (or constructed from test data) can be resolved back into a transient entity through the same pipeline used at runtime.

> **Note**: If the entity type does not support the file’s content type.

```swift
let file = try await transientEntity.exported(as: .json)
let resolved = try await sessionEntityDef.resolved(from: file)
```

## Parameters

- `file`: The `IntentFile` containing the exported entity data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/transientappentitydefinition/resolved(from:)-6xsjl)*