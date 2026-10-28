# resourceGroupName

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0

> **Deprecated**: Only supported for legacy reference objects.

## Declaration

```swift
var resourceGroupName: String? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSString * resourceGroupName;
```

## Discussion

If ARKit loaded this object from an AR resource group in an asset catalog, ARKit sets the value of this property to the resource group’s name. Otherwise, the value of this property is `nil`.

## See Also

### Examining a Reference Object
- [var name: String?](./name.md)
  A descriptive name for the reference object.
- [var center: simd_float3](./center.md)
  The center point of the reference object’s space-mapping data.
- [var extent: simd_float3](./extent.md)
  The size of the reference object’s space-mapping data.
- [var scale: simd_float3](./scale.md)
  A scale factor for the local coordinate space the reference object defines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arreferenceobject/resourcegroupname)*