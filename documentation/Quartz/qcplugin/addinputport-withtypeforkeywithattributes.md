# addInputPort(withType:forKey:withAttributes:)

**Framework**: Quartz  
**Kind**: method

Adds an input port of the specified type and associates a key and attributes with the port.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func addInputPort(withType type: String!, forKey key: String!, withAttributes attributes: [AnyHashable : Any]! = [:])
```

#### Discussion

This method throws an exception if called from within  the [`execute(_:atTime:withArguments:)`](qcplugin/execute(_:attime:witharguments:).md) method  or if there’s already an input or output port with that key.

## Parameters

- `type`: The port type. See  .
- `key`: The key to associate with the port.
- `attributes`: A dictionary of attributes for the port. See  . Although the dictionary is optional, it’s recommended that provide attributes to enhance the experience of those who use your custom patch. The attributes appear in a help tag when the user hovers a pointer over the property port on your custom patch. (See  .) Pass    if you do not want to provide attributes.

## See Also

- [func removeInputPort(forKey: String!)](qcplugin/removeinputport(forkey:).md)
  Removes the input port for a given key.
- [func addOutputPort(withType: String!, forKey: String!, withAttributes: [AnyHashable : Any]!)](qcplugin/addoutputport(withtype:forkey:withattributes:).md)
  Adds an output port of the specified type and associates a key and attributes with the port.
- [func removeOutputPort(forKey: String!)](qcplugin/removeoutputport(forkey:).md)
  Removes the output port for a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/addinputport(withtype:forkey:withattributes:))*