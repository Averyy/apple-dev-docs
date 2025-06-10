# name

**Framework**: ARKit  
**Kind**: property

A descriptive name for the reference object.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var name: String? { get set }
```

#### Discussion

For a reference object loaded from an Xcode asset catalog, this property is the name assigned in the asset catalog. You can also use this property to assign a name to an object you’ve recorded in an AR session using extractReferenceObject.

> **Note**:  This string is not localized text intended for user display. However, in debugging you can use this property to indicate which reference object was detected.

## See Also

- [var resourceGroupName: String?](arreferenceobject/resourcegroupname.md)
- [var center: simd_float3](arreferenceobject/center.md)
  The center point of the reference object’s space-mapping data.
- [var extent: simd_float3](arreferenceobject/extent.md)
  The size of the reference object’s space-mapping data.
- [var scale: simd_float3](arreferenceobject/scale.md)
  A scale factor for the local coordinate space the reference object defines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arreferenceobject/name)*