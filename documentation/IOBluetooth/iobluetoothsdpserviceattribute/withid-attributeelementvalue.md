# withID(_:attributeElementValue:)

**Framework**: IOBluetooth  
**Kind**: method

Creates a new service attribute with the given ID and element value.

**Availability**:
- macOS ?+

## Declaration

```swift
class func withID(_ newAttributeID: BluetoothSDPServiceAttributeID, attributeElementValue: NSObject!) -> Self!
```

#### Return Value

Returns the newly allocated service attribute object. Returns nil if there was an error parsing the element value. The returned IOBluetoothSDPDataElement object has been autoreleased, so it is not necessary for the caller to release it. If the object is to be referenced and kept around, retain should be called.

#### Discussion

See +[IOBluetoothSDPDataElement withElementValue:] for a description of the types that may be passed in as the attributeElementValue.

## Parameters

- `newAttributeID`: The attribute ID of the new service attribute.
- `attributeElementValue`: The data element value of the new service attribute


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpserviceattribute/withid(_:attributeelementvalue:))*