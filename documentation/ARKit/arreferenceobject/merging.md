# merging(_:)

**Framework**: ARKit  
**Kind**: method

Returns a new reference object that combines spatial information from both this reference object and another.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func merging(_ object: ARReferenceObject) throws -> ARReferenceObject
```

#### Return Value

A new [`ARReferenceObject`](arreferenceobject.md) that includes the spatial information from both objects. From Swift, this method throws an [`ARError`](arerror.md) if the two objects cannot be merged. From Objective-C, it returns `nil` and populates the `error` parameter with a description of the failure.

#### Discussion

The accuracy of 3D object detection depends on similarity of lighting and environmental conditions between when you scan a real object (producing an [`ARReferenceObject`](arreferenceobject.md)) and when a user of your app attempts to detect that object. If, for example, you scan an object in a bright environment, then a user attempts to detect it in a dark environment, ARKit may fail to recognize that the real object matches the reference object, or may not detect the object quickly.

To make a reference object that is more robust in a wide variety of detection conditions, scan the same real-world object multiple times: For each scan, vary the lighting conditions or the background environment to capture the variety of situations in which your app might attempt to detect the same real object. Then, use this method to combine those scan results into a single [`ARReferenceObject`](arreferenceobject.md) incorporating recognition information for all the conditions you scanned in.

## Parameters

- `object`: The other reference object with which to combine this reference object.

## See Also

- [func applyingTransform(simd_float4x4) -> ARReferenceObject](arreferenceobject/applyingtransform(_:).md)
  Returns a new reference object created by applying the specified transform to this reference object’s geometric data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arreferenceobject/merging(_:))*