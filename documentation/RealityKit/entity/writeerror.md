# Entity.WriteError

**Framework**: RealityKit  
**Kind**: enum

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum WriteError
```

## Topics

### Handling write errors
- [Entity.WriteError.conflictingOptions(_:)](entity/writeerror/conflictingoptions(_:).md)

## Relationships

### Conforms To
- [Error](../Swift/Error.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func write(to: URL, options: Entity.WriteOptions) async throws](entity/write(to:options:).md)
- [static func write([Entity], to: URL, options: Entity.WriteOptions) async throws](entity/write(_:to:options:).md)
  Exports an array of entities as separate scenes within a single RealityKit file.
- [Entity.WriteOptions](entity/writeoptions.md)
  Options for writing an entity to a RealityKit file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/writeerror)*