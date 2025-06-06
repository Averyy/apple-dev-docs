# init(id:attributeElement:)

**Framework**: IOBluetooth  
**Kind**: init

Initializes a new service attribute with the given ID and data element.

**Availability**:
- macOS ?+

## Declaration

```swift
init!(id newAttributeID: BluetoothSDPServiceAttributeID, attributeElement: IOBluetoothSDPDataElement!)
```

#### Return Value

Returns self if successful. Returns nil if there was an error.

## Parameters

- `newAttributeID`: The attribute ID of the new service attribute.
- `attributeElement`: The data element of the new service attribute.

## See Also

- [init!(id: BluetoothSDPServiceAttributeID, attributeElementValue: NSObject!)](iobluetoothsdpserviceattribute/init(id:attributeelementvalue:).md)
  Initializes a new service attribute with the given ID and element value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpserviceattribute/init(id:attributeelement:))*