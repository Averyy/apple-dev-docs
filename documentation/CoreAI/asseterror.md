# AssetError

**Framework**: Core AI  
**Kind**: struct

An error that occurs during model asset operations.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct AssetError
```

## Topics

### Inspecting error information
- [var kind: AssetError.Kind](asseterror/kind-swift.property.md)
  The classification of the error.
- [var debugMessage: String?](asseterror/debugmessage.md)
  An optional message with additional debugging context.
- [var errorDescription: String?](asseterror/errordescription.md)
  A localized description of the error.
### Creating errors
- [init(kind: AssetError.Kind, debugMessage: String?)](asseterror/init(kind:debugmessage:).md)
  Creates an asset error.
### Defining error types
- [AssetError.Kind](asseterror/kind-swift.enum.md)
  The reasons an asset operation can fail.

## Relationships

### Conforms To
- [Error](../swift/error.md)
- [LocalizedError](../foundation/localizederror.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/asseterror)*