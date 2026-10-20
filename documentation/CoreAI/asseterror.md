# AssetError

**Framework**: Core AI  
**Kind**: struct  
**Role**: Structure

An error that occurs during model asset operations.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct AssetError
```

## Topics

### Inspecting error information
- [var kind: AssetError.Kind](./asseterror/kind-swift.property.md)
  The classification of the error.
- [var debugMessage: String?](./asseterror/debugmessage.md)
  An optional message with additional debugging context.
- [var errorDescription: String?](./asseterror/errordescription.md)
  A localized description of the error.
### Creating errors
- [init(kind: AssetError.Kind, debugMessage: String?)](./asseterror/init%28kind,debugmessage%29.md)
  Creates an asset error.
### Defining error types
- [AssetError.Kind](./asseterror/kind-swift.enum.md)
  The reasons an asset operation can fail.

## Relationships

### Conforms To
- [Error](../Swift/error.md)
- [LocalizedError](../Foundation/localizederror.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/asseterror)*