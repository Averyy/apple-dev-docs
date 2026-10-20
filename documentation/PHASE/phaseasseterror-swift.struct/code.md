# PHASEAssetError.Code

**Framework**: PHASE  
**Kind**: enum  
**Role**: Enumeration

Codes that identify framework asset errors.

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
enum PHASEAssetError : NSInteger;
```

## Topics

### Errors
- [PHASEAssetError.Code.alreadyExists](./code/alreadyexists.md)
  An error the asset registry throws when the app registers an asset twice by the same name.
- [PHASEAssetError.Code.badParameters](./code/badparameters.md)
  An error that indicates an asset registry call contains invalid data.
- [PHASEAssetError.Code.failedToLoad](./code/failedtoload.md)
  An error that indicates an asset failed to load.
- [PHASEAssetError.Code.generalError](./code/generalerror.md)
  An error the asset registry throws when an unspecified problem occurs.
- [PHASEAssetError.Code.invalidEngineInstance](./code/invalidengineinstance.md)
  An error that indicates an asset registry call references an invalid engine.
- [PHASEAssetError.Code.memoryAllocation](./code/memoryallocation.md)
  An error the framework throws when an asset depletes system memory.
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

### Asset Errors
- [struct PHASEAssetError](../phaseasseterror-swift.struct.md)
  An asset error that PHASE reports.
- [let PHASEAssetErrorDomain: String](../phaseasseterrordomain.md)
  A unique error domain for PHASE assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseasseterror-swift.struct/code)*