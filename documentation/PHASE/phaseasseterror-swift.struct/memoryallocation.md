# memoryAllocation

**Framework**: PHASE  
**Kind**: property  
**Role**: Type Property

An error the framework throws when an asset depletes system memory.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
static var memoryAllocation: PHASEAssetError.Code { get }
```

## See Also

### Identifying an Error Cause
- [static var alreadyExists: PHASEAssetError.Code](./alreadyexists.md)
  An error the asset registry throws when the app registers an asset twice by the same name.
- [static var badParameters: PHASEAssetError.Code](./badparameters.md)
  An error that indicates an asset registry call contains invalid data.
- [static var failedToLoad: PHASEAssetError.Code](./failedtoload.md)
  An error that indicates an asset failed to load.
- [static var generalError: PHASEAssetError.Code](./generalerror.md)
  An error the asset registry throws when an unspecified problem occurs.
- [static var invalidEngineInstance: PHASEAssetError.Code](./invalidengineinstance.md)
  An error that indicates an asset registry call references an invalid engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseasseterror-swift.struct/memoryallocation)*