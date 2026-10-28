# attributes()

**Framework**: Quartz  
**Kind**: method  
**Role**: Type Method

Returns a dictionary that contains strings for the user interface that describe the custom patch.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
class func attributes() -> [AnyHashable : Any]!
```

```objc
+ (NSDictionary *) attributes;
```

## Return Value

The dictionary can contain one or more of these keys along with the appropriate string: [`QCPlugInAttributeNameKey`](../qcpluginattributenamekey.md) and [`QCPlugInAttributeDescriptionKey`](../qcpluginattributedescriptionkey.md).

## Discussion

It’s recommended that you implement this method to enhance the experience of those who use your custom patch. The attribute name string that you provide is displayed in the Quartz Composer editor window when the custom patch name is selected in the Patch Creator (see figure). The attribute description key is displayed in the Information pane of the inspector for the custom patch.

![The patch library with the description box open.](https://developer.apple.com/tutorials/images/com.apple.quartz/media-2557124.jpg)

## See Also

### Defining Patch and Property Port Attributes
- [class func attributesForPropertyPort(withKey: String!) -> [AnyHashable : Any]!](./attributesforpropertyport%28withkey%29.md)
  Returns a dictionary that contains strings for the user interface that describe the optional attributes for ports created from properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/attributes())*