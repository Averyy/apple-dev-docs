# PHASEAssetError.Code

**Framework**: PHASE  
**Kind**: enum

Codes that identify framework asset errors.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum Code
```

## Topics

### Errors
- [PHASEAssetError.Code.alreadyExists](phaseasseterror-swift.struct/code/alreadyexists.md)
  An error the asset registry throws when the app registers an asset twice by the same name.
- [PHASEAssetError.Code.badParameters](phaseasseterror-swift.struct/code/badparameters.md)
  An error that indicates an asset registry call contains invalid data.
- [PHASEAssetError.Code.failedToLoad](phaseasseterror-swift.struct/code/failedtoload.md)
  An error that indicates an asset failed to load.
- [PHASEAssetError.Code.generalError](phaseasseterror-swift.struct/code/generalerror.md)
  An error the asset registry throws when an unspecified problem occurs.
- [PHASEAssetError.Code.invalidEngineInstance](phaseasseterror-swift.struct/code/invalidengineinstance.md)
  An error that indicates an asset registry call references an invalid engine.
- [PHASEAssetError.Code.memoryAllocation](phaseasseterror-swift.struct/code/memoryallocation.md)
  An error the framework throws when an asset depletes system memory.
### Initializers
- [init?(rawValue: Int)](phaseasseterror-swift.struct/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct PHASEAssetError](phaseasseterror-swift.struct.md)
  An asset error that PHASE reports.
- [let PHASEAssetErrorDomain: String](phaseasseterrordomain.md)
  A unique error domain for PHASE assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseasseterror-swift.struct/code)*