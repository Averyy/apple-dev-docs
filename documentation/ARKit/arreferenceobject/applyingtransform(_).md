# applyingTransform(_:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Returns a new reference object by applying the specified transform to the object’s origin.

**Availability**:
- iOS 12.0+ - Deprecated in 27.0
- iPadOS 12.0+ - Deprecated in 27.0

> **Deprecated**: Only supported for legacy reference objects.

## Declaration

```swift
func applyingTransform(_ transform: simd_float4x4) -> ARReferenceObject
```

```objc
- (ARReferenceObject *) referenceObjectByApplyingTransform:(simd_float4x4) transform;
```

## Return Value

The transformed reference object.

## Discussion

You define the local coordinate space of a reference object with the transform parameter when you create it with [`createReferenceObject(transform:center:extent:completionHandler:)`](../arsession/createreferenceobject%28transform,center,extent,completionhandler%29.md). If an existing reference object has a local coordinate origin that doesn’t fit well with the object’s intended use, call this method to change the reference object’s origin with respect to the physical object it represents.

When ARKit detects a reference object, the [`transform`](../aranchor/transform.md) of the resulting [`ARObjectAnchor`](../arobjectanchor.md) is based on the origin of the reference object’s coordinate system. For example, if a reference object represents a physical item that sits on a horizontal surface, virtual content should appear to sit on whatever surface the physical object does. As such, it’s typically useful to align a reference object’s coordinate origin with the bottom of the physical object.

For reference objects loaded from a `.referenceobject` file, this method returns the same reference object unchanged.

## Parameters

- `transform`: A transform matrix in the local coordinate space of the reference object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arreferenceobject/applyingtransform(_:))*