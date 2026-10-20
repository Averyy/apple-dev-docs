# PHASEError.Code.invalidObject

**Framework**: PHASE  
**Kind**: case  
**Role**: Case

An error that indicates an object is invalid in a specific context.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
case invalidObject
```

```c
PHASEErrorInvalidObject
```

#### Discussion

The [`addChild(_:)`](../../phaseobject/addchild%28_%29.md) function throws this error if the specified child already has a parent in the scene graph hierarchy.

## See Also

### Errors
- [PHASEError.Code.initializeFailed](./initializefailed.md)
  An error that indicates the engine failed to initialize.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseerror-swift.struct/code/invalidobject)*