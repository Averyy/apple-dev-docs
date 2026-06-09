# isTemporary

**Framework**: SwiftData  
**Kind**: property

A Boolean value that indicates whether the identifier is temporary.

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
var isTemporary: Bool { get }
```

#### Discussion

A temporary identifier is assigned to a model when it is first initialized. Once you call [`save()`](modelcontext/save().md), the model receives a permanent identifier.

Temporary identifiers should not be persisted or used to create durable maps to a model. Temporary identifiers are only valid until an object is persisted, and must be remapped to the permanent identifier once a model is saved.

```swift
if model.persistentModelID.isTemporary {
    try modelContext.save()
}
let data = try JSONEncoder().encode(model.persistentModelID)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/persistentidentifier/istemporary)*