# PHASEAssetError

**Framework**: PHASE  
**Kind**: struct

An asset error that PHASE reports.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct PHASEAssetError
```

## Topics

### Creating an Error
- [PHASEAssetError.Code](phaseasseterror-swift.struct/code.md)
  Codes that identify framework asset errors.
### Identifying an Error Cause
- [static var alreadyExists: PHASEAssetError.Code](phaseasseterror-swift.struct/alreadyexists.md)
  An error the asset registry throws when the app registers an asset twice by the same name.
- [static var badParameters: PHASEAssetError.Code](phaseasseterror-swift.struct/badparameters.md)
  An error that indicates an asset registry call contains invalid data.
- [static var failedToLoad: PHASEAssetError.Code](phaseasseterror-swift.struct/failedtoload.md)
  An error that indicates an asset failed to load.
- [static var generalError: PHASEAssetError.Code](phaseasseterror-swift.struct/generalerror.md)
  An error the asset registry throws when an unspecified problem occurs.
- [static var invalidEngineInstance: PHASEAssetError.Code](phaseasseterror-swift.struct/invalidengineinstance.md)
  An error that indicates an asset registry call references an invalid engine.
- [static var memoryAllocation: PHASEAssetError.Code](phaseasseterror-swift.struct/memoryallocation.md)
  An error the framework throws when an asset depletes system memory.
### Type Properties
- [static var errorDomain: String](phaseasseterror-swift.struct/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [PHASEAssetError.Code](phaseasseterror-swift.struct/code.md)
  Codes that identify framework asset errors.
- [let PHASEAssetErrorDomain: String](phaseasseterrordomain.md)
  A unique error domain for PHASE assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseasseterror-swift.struct)*