# getAttributeDataElement(_:)

**Framework**: IOBluetooth  
**Kind**: method

Returns the data element for the given attribute ID in the target service.

**Availability**:
- macOS ?+

## Declaration

```swift
func getAttributeDataElement(_ attributeID: BluetoothSDPServiceAttributeID) -> IOBluetoothSDPDataElement!
```

#### Return Value

Returns the data element for the given attribute ID in the target service. If the service does not contain an attribute with the given ID, then nil is returned.

## Parameters

- `attributeID`: The attribute ID of the desired attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecord/getattributedataelement(_:))*