# resourceGroupName

**Framework**: ARKit  
**Kind**: property

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var resourceGroupName: String? { get }
```

#### Discussion

If ARKit loaded this object from an AR resource group in an asset catalog, ARKit sets the value of this property to the resource group’s name. Otherwise, the value of this property is `nil`.

## See Also

- [var name: String?](arreferenceobject/name.md)
  A descriptive name for the reference object.
- [var center: simd_float3](arreferenceobject/center.md)
  The center point of the reference object’s space-mapping data.
- [var extent: simd_float3](arreferenceobject/extent.md)
  The size of the reference object’s space-mapping data.
- [var scale: simd_float3](arreferenceobject/scale.md)
  A scale factor for the local coordinate space the reference object defines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arreferenceobject/resourcegroupname)*