# resourceGroupName

**Framework**: ARKit  
**Kind**: property

The AR resource group name for this image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var resourceGroupName: String? { get }
```

#### Discussion

If ARKit loaded this image from an AR resource group in an asset catalog, ARKit sets the value of this property to the resource group’s name. Otherwise, the value of this property is `nil`>.

## See Also

- [var name: String?](arreferenceimage/name.md)
  A descriptive name for the image.
- [var physicalSize: CGSize](arreferenceimage/physicalsize.md)
  The real-world dimensions, in meters, of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arreferenceimage/resourcegroupname)*