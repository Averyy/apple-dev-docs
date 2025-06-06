# SecTransformCreateGroupTransform()

**Framework**: Security  
**Kind**: func

Creates an object that acts as a container for a set of connected transforms.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecTransformCreateGroupTransform() -> SecGroupTransform
```

#### Return Value

A transform group object.

#### Discussion

A [`SecGroupTransform`](secgrouptransform.md) is a container for all of the transforms that are in a directed graph. You can use this container as you would a single transform with the [`SecTransformExecute(_:_:)`](sectransformexecute(_:_:).md), [`SecTransformExecuteAsync(_:_:_:)`](sectransformexecuteasync(_:_:_:).md) and [`SecTransformCopyExternalRepresentation(_:)`](sectransformcopyexternalrepresentation(_:).md) functions.On the other hand, unlike a stand alone transform, you can’t use a transform group with the [`SecTransformConnectTransforms(_:_:_:_:_:_:)`](sectransformconnecttransforms(_:_:_:_:_:_:).md), [`SecTransformSetAttribute(_:_:_:_:)`](sectransformsetattribute(_:_:_:_:).md) or [`SecTransformGetAttribute(_:_:)`](sectransformgetattribute(_:_:).md) functions. Attempting to do so produces undefined behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformcreategrouptransform())*