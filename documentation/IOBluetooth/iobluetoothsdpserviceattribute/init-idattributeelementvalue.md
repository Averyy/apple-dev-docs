# init(id:attributeElementValue:)

**Framework**: IOBluetooth  
**Kind**: init

Initializes a new service attribute with the given ID and element value.

**Availability**:
- macOS ?+

## Declaration

```swift
init!(id newAttributeID: BluetoothSDPServiceAttributeID, attributeElementValue: NSObject!)
```

#### Return Value

Returns self if successful. Returns nil if there was an error parsing the element value.

#### Discussion

See +[IOBluetoothSDPDataElement withElementValue:] for a description of the types that may be passed in as the attributeElementValue.

## Parameters

- `newAttributeID`: The attribute ID of the new service attribute.
- `attributeElementValue`: The data element value of the new service attribute

## See Also

- [init!(id: BluetoothSDPServiceAttributeID, attributeElement: IOBluetoothSDPDataElement!)](iobluetoothsdpserviceattribute/init(id:attributeelement:).md)
  Initializes a new service attribute with the given ID and data element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpserviceattribute/init(id:attributeelementvalue:))*