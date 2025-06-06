# attributes()

**Framework**: Quartz  
**Kind**: method

Returns a dictionary that contains strings for the user interface that describe the custom patch.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class func attributes() -> [AnyHashable : Any]!
```

#### Return Value

The dictionary can contain one or more of these keys along with the appropriate string: [`QCPlugInAttributeNameKey`](qcpluginattributenamekey.md) and [`QCPlugInAttributeDescriptionKey`](qcpluginattributedescriptionkey.md).

#### Discussion

It’s recommended that you implement this method to enhance the experience of those who use your custom patch. The attribute name string that you provide is displayed in the Quartz Composer editor window when the custom patch name is selected in the Patch Creator (see figure). The attribute description key is displayed in the Information pane of the inspector for the custom patch.

![The patch library with the description box open.](https://docs-assets.developer.apple.com/published/182f1859f4e24613deb8250f60516d69/media-2557124.jpg)

## See Also

- [class func attributesForPropertyPort(withKey: String!) -> [AnyHashable : Any]!](qcplugin/attributesforpropertyport(withkey:).md)
  Returns a dictionary that contains strings for the user interface that describe the optional attributes for ports created from properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/attributes())*