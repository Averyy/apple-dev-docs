# resourceGroupName

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A string value the represents the name of the resource group the framework loads an image from.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var resourceGroupName: String? { get }
```

## Discussion

The property contains a value only if the framework loads a reference image from a resource group. Otherwise, it’s `nil`.

## See Also

### Inspecting a reference image
- [var physicalSize: CGSize](./physicalsize.md)
  The size, in meters, of a reference image in the real world.
- [var name: String?](./name.md)
  The name of a reference image.
- [var description: String](./description.md)
  A textual representation of this reference image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/referenceimage/resourcegroupname)*