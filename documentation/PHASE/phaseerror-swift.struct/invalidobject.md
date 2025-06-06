# invalidObject

**Framework**: PHASE  
**Kind**: property

An error that indicates an object is invalid in a specific context.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
static var invalidObject: PHASEError.Code { get }
```

#### Discussion

The [`addChild(_:)`](phaseobject/addchild(_:).md) function throws this error if the specified child already has a parent in the scene graph hierarchy.

## See Also

- [static var initializeFailed: PHASEError.Code](phaseerror-swift.struct/initializefailed.md)
  An error that indicates the engine failed to initialize.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseerror-swift.struct/invalidobject)*