# removeInputPort(forKey:)

**Framework**: Quartz  
**Kind**: method

Removes the input port for a given key.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func removeInputPort(forKey key: String!)
```

#### Discussion

This method throws an exception if from within  the [`execute(_:atTime:withArguments:)`](qcplugin/execute(_:attime:witharguments:).md) method, if there is not an input port with that key, or if the port is created from a property.

## Parameters

- `key`: The key associated with the port that you want to remove.

## See Also

- [func addInputPort(withType: String!, forKey: String!, withAttributes: [AnyHashable : Any]!)](qcplugin/addinputport(withtype:forkey:withattributes:).md)
  Adds an input port of the specified type and associates a key and attributes with the port.
- [func addOutputPort(withType: String!, forKey: String!, withAttributes: [AnyHashable : Any]!)](qcplugin/addoutputport(withtype:forkey:withattributes:).md)
  Adds an output port of the specified type and associates a key and attributes with the port.
- [func removeOutputPort(forKey: String!)](qcplugin/removeoutputport(forkey:).md)
  Removes the output port for a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/removeinputport(forkey:))*