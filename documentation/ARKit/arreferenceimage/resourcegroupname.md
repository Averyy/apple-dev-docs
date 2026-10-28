# resourceGroupName

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The AR resource group name for this image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
var resourceGroupName: String? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSString * resourceGroupName;
```

## Discussion

If ARKit loaded this image from an AR resource group in an asset catalog, ARKit sets the value of this property to the resource group’s name. Otherwise, the value of this property is `nil`>.

## See Also

### Examining a Reference Image
- [var name: String?](./name.md)
  A descriptive name for the image.
- [var physicalSize: CGSize](./physicalsize.md)
  The real-world dimensions, in meters, of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arreferenceimage/resourcegroupname)*