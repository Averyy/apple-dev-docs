# addInputPort(withType:forKey:withAttributes:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Adds an input port of the specified type and associates a key and attributes with the port.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func addInputPort(withType type: String!, forKey key: String!, withAttributes attributes: [AnyHashable : Any]! = [:])
```

```objc
- (void) addInputPortWithType:(NSString *) type forKey:(NSString *) key withAttributes:(NSDictionary *) attributes;
```

#### Discussion

This method throws an exception if called from within  the [`execute(_:atTime:withArguments:)`](./execute%28_,attime,witharguments%29.md) method  or if there’s already an input or output port with that key.

## Parameters

- `type`: The port type. See [Port Input and Output Types](../port-input-and-output-types.md).
- `key`: The key to associate with the port.
- `attributes`: A dictionary of attributes for the port. See [Input and Output Port Attributes](../input-and-output-port-attributes.md). Although the dictionary is optional, it’s recommended that provide attributes to enhance the experience of those who use your custom patch. The attributes appear in a help tag when the user hovers a pointer over the property port on your custom patch. (See [`attributesForPropertyPort(withKey:)`](./attributesforpropertyport%28withkey%29.md).) Pass  `nil` if you do not want to provide attributes.

## See Also

### Adding Ports Dynamically
- [func removeInputPort(forKey: String!)](./removeinputport%28forkey%29.md)
  Removes the input port for a given key.
- [func addOutputPort(withType: String!, forKey: String!, withAttributes: [AnyHashable : Any]!)](./addoutputport%28withtype,forkey,withattributes%29.md)
  Adds an output port of the specified type and associates a key and attributes with the port.
- [func removeOutputPort(forKey: String!)](./removeoutputport%28forkey%29.md)
  Removes the output port for a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/addinputport(withtype:forkey:withattributes:))*