# name

**Framework**: ARKit  
**Kind**: property

A descriptive name for the image.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+

## Declaration

```swift
var name: String? { get set }
```

#### Discussion

For reference images loaded from an Xcode asset catalog, this property is the name assigned in the asset catalog. For programmatically created reference images, this value is `nil`.

> **Note**:  This string is not localized text intended for user display. However, in debugging  you can use this property to indicate which image was detected.

 This string is not localized text intended for user display. However, in debugging  you can use this property to indicate which image was detected.

## See Also

- [var physicalSize: CGSize](arreferenceimage/physicalsize.md)
  The real-world dimensions, in meters, of the image.
- [var resourceGroupName: String?](arreferenceimage/resourcegroupname.md)
  The AR resource group name for this image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arreferenceimage/name)*