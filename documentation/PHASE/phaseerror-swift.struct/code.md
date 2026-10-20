# PHASEError.Code

**Framework**: PHASE  
**Kind**: enum  
**Role**: Enumeration

Codes that identify errors in PHASE.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum Code
```

```c
enum PHASEError : NSInteger;
```

## Topics

### Errors
- [PHASEError.Code.initializeFailed](./code/initializefailed.md)
  An error that indicates the engine failed to initialize.
- [PHASEError.Code.invalidObject](./code/invalidobject.md)
  An error that indicates an object is invalid in a specific context.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Framework Errors
- [struct PHASEError](../phaseerror-swift.struct.md)
  An error that PHASE reports.
- [let PHASEErrorDomain: String](../phaseerrordomain.md)
  A unique error domain for the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseerror-swift.struct/code)*