# setImage(_:imageProperties:)

**Framework**: Quartz  
**Kind**: method  
**Required**: Yes

Sets an image with the specified properties.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setImage(_ image: CGImage!, imageProperties metaData: [AnyHashable : Any]!)
```

#### Discussion

Your data source must implement this method.

## See Also

- [protocol IKImageEditPanelDataSource](ikimageeditpaneldatasource.md)
  The `IKImageEditPanelDataSource` protocol describes the methods that an [`IKImageEditPanel`](ikimageeditpanel.md) object uses to access the contents of its data source object.
- [var imageProperties: [AnyHashable : Any]!](ikimageeditpaneldatasource/imageproperties.md)
  Returns a dictionary of the image properties associated with the image in the image edit panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageeditpaneldatasource/setimage(_:imageproperties:))*