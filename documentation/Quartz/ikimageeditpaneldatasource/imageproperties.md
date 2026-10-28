# imageProperties

**Framework**: Quartz  
**Kind**: property  
**Role**: Instance Property

Returns a dictionary of the image properties associated with the image in the image edit panel.

**Availability**:
- macOS 10.4+

## Declaration

```swift
optional var imageProperties: [AnyHashable : Any]! { get }
```

```objc
@property (atomic, copy, readonly) NSDictionary * imageProperties;
```

## Return Value

A dictionary that contains the properties of the image.

## See Also

### Related Documentation
- [protocol IKImageEditPanelDataSource](../ikimageeditpaneldatasource.md)
  The `IKImageEditPanelDataSource` protocol describes the methods that an [`IKImageEditPanel`](../ikimageeditpanel.md) object uses to access the contents of its data source object.
- [Image Kit Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/ImageKitProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004907)
### Getting and Setting Image Properties
- [func setImage(CGImage!, imageProperties: [AnyHashable : Any]!)](./setimage%28_,imageproperties%29.md)
  Sets an image with the specified properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageeditpaneldatasource/imageproperties)*