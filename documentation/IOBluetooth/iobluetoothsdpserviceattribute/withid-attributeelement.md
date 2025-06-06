# withID(_:attributeElement:)

**Framework**: IOBluetooth  
**Kind**: method

Creates a new service attribute with the given ID and data element.

**Availability**:
- macOS ?+

## Declaration

```swift
class func withID(_ newAttributeID: BluetoothSDPServiceAttributeID, attributeElement: IOBluetoothSDPDataElement!) -> Self!
```

#### Return Value

Returns the newly allocated service attribute object. Returns nil if there was an error. The returned IOBluetoothSDPDataElement object has been autoreleased, so it is not necessary for the caller to release it. If the object is to be referenced and kept around, retain should be called.

## Parameters

- `newAttributeID`: The attribute ID of the new service attribute.
- `attributeElement`: The data element of the new service attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpserviceattribute/withid(_:attributeelement:))*