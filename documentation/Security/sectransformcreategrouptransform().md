# SecTransformCreateGroupTransform()

**Framework**: Security  
**Kind**: func  
**Role**: Function

Creates an object that acts as a container for a set of connected transforms.

**Availability**:
- macOS 10.7+ - Deprecated in 12.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
func SecTransformCreateGroupTransform() -> SecGroupTransform
```

```c
extern SecGroupTransformRefSecTransformCreateGroupTransform();
```

#### Return Value

A transform group object.

#### Discussion

A [`SecGroupTransform`](./secgrouptransform.md) is a container for all of the transforms that are in a directed graph. You can use this container as you would a single transform with the [`SecTransformExecute(_:_:)`](./sectransformexecute%28_,_%29.md), [`SecTransformExecuteAsync(_:_:_:)`](./sectransformexecuteasync%28_,_,_%29.md) and [`SecTransformCopyExternalRepresentation(_:)`](./sectransformcopyexternalrepresentation%28_%29.md) functions.On the other hand, unlike a stand alone transform, you can’t use a transform group with the [`SecTransformConnectTransforms(_:_:_:_:_:_:)`](./sectransformconnecttransforms%28_,_,_,_,_,_%29.md), [`SecTransformSetAttribute(_:_:_:_:)`](./sectransformsetattribute%28_,_,_,_%29.md) or [`SecTransformGetAttribute(_:_:)`](./sectransformgetattribute%28_,_%29.md) functions. Attempting to do so produces undefined behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformcreategrouptransform())*