# init(id:attributeElementValue:)

**Framework**: IOBluetooth  
**Kind**: init  
**Role**: Initializer

Initializes a new service attribute with the given ID and element value.

**Availability**:
- macOS

## Declaration

```swift
init!(id newAttributeID: BluetoothSDPServiceAttributeID, attributeElementValue: NSObject!)
```

```objc
- (instancetype) initWithID:(BluetoothSDPServiceAttributeID) newAttributeID attributeElementValue:(NSObject *) attributeElementValue;
```

#### Return Value

Returns self if successful. Returns nil if there was an error parsing the element value.

#### Discussion

See +[IOBluetoothSDPDataElement withElementValue:] for a description of the types that may be passed in as the attributeElementValue.

## Parameters

- `newAttributeID`: The attribute ID of the new service attribute.
- `attributeElementValue`: The data element value of the new service attribute

## See Also

### Initializers
- [init!(id: BluetoothSDPServiceAttributeID, attributeElement: IOBluetoothSDPDataElement!)](./init%28id,attributeelement%29-7oebi.md)
  Initializes a new service attribute with the given ID and data element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpserviceattribute/init(id:attributeelementvalue:)-84b3r)*