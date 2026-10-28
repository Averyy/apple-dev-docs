# attributesForPropertyPort(withKey:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Type Method

Returns a dictionary that contains strings for the user interface that describe the optional attributes for ports created from properties.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
class func attributesForPropertyPort(withKey key: String!) -> [AnyHashable : Any]!
```

```objc
+ (NSDictionary *) attributesForPropertyPortWithKey:(NSString *) key;
```

## Return Value

A dictionary that contains key-value pairs for the port’s attributes. The keys must be one or more of the constants defined in [Input and Output Port Attributes](../input-and-output-port-attributes.md).

## Discussion

It’s recommended that you implement this method to enhance the experience of those who use your custom patch. The attributes appear in a help tag when the user hovers a pointer over the property port on your custom patch. At a minimum, you should provide a user-readable name for the port. It might also be helpful to provide default, minimum, and maximum values for the port.

## Parameters

- `key`: The name of the property.

## See Also

### Defining Patch and Property Port Attributes
- [class func attributes() -> [AnyHashable : Any]!](./attributes%28%29.md)
  Returns a dictionary that contains strings for the user interface that describe the custom patch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/attributesforpropertyport(withkey:))*