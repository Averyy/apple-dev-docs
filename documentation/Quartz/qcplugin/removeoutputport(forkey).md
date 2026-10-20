# removeOutputPort(forKey:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Removes the output port for a given key.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func removeOutputPort(forKey key: String!)
```

```objc
- (void) removeOutputPortForKey:(NSString *) key;
```

#### Discussion

This method throws an exception if called from within the [`execute(_:atTime:withArguments:)`](./execute%28_,attime,witharguments%29.md) method, if there is not an output port with that key, or if the port is created from a property.

## Parameters

- `key`: The key associated with the port that you want to remove.

## See Also

### Adding Ports Dynamically
- [func addInputPort(withType: String!, forKey: String!, withAttributes: [AnyHashable : Any]!)](./addinputport%28withtype,forkey,withattributes%29.md)
  Adds an input port of the specified type and associates a key and attributes with the port.
- [func removeInputPort(forKey: String!)](./removeinputport%28forkey%29.md)
  Removes the input port for a given key.
- [func addOutputPort(withType: String!, forKey: String!, withAttributes: [AnyHashable : Any]!)](./addoutputport%28withtype,forkey,withattributes%29.md)
  Adds an output port of the specified type and associates a key and attributes with the port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/removeoutputport(forkey:))*