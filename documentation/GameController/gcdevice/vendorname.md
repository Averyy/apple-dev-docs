# vendorName

**Framework**: Game Controller  
**Kind**: property  
**Required**: Yes

The manufacturer-provided name for the device, or the user’s name for the device.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var vendorName: String? { get }
```

#### Discussion

The value of this property may be `nil` and may not be unique. Use this property to present information about the device to the user.

## See Also

- [var productCategory: String](gcdevice/productcategory.md)
  The product category that identifies the type of controller.
- [Product category constants](product-category-constants.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevice/vendorname)*