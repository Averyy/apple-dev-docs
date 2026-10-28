# init(id:attributeElement:)

**Framework**: IOBluetooth  
**Kind**: init  
**Role**: Initializer

Initializes a new service attribute with the given ID and data element.

**Availability**:
- macOS

## Declaration

```swift
init!(id newAttributeID: BluetoothSDPServiceAttributeID, attributeElement: IOBluetoothSDPDataElement!)
```

```objc
- (instancetype) initWithID:(BluetoothSDPServiceAttributeID) newAttributeID attributeElement:(IOBluetoothSDPDataElement *) attributeElement;
```

## Return Value

Returns self if successful. Returns nil if there was an error.

## Parameters

- `newAttributeID`: The attribute ID of the new service attribute.
- `attributeElement`: The data element of the new service attribute.

## See Also

### Initializers
- [init!(id: BluetoothSDPServiceAttributeID, attributeElementValue: NSObject!)](./init%28id,attributeelementvalue%29-84b3r.md)
  Initializes a new service attribute with the given ID and element value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpserviceattribute/init(id:attributeelement:)-7oebi)*