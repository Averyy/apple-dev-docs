# withElementValue(_:)

**Framework**: IOBluetooth  
**Kind**: method

Creates a new IOBluetoothSDPDataElement with the given value.

**Availability**:
- macOS ?+

## Declaration

```swift
class func withElementValue(_ element: NSObject!) -> Self!
```

#### Return Value

Returns the newly allocated data element object. Returns nil if there was an error parsing the element value. The returned IOBluetoothSDPDataElement object has been autoreleased, so it is not necessary for the caller to release it. If the object is to be referenced and kept around, retain should be called.

#### Discussion

The value must follow the format listed above and must be an instance of NSData, NSString, NSNumber, NSArray, NSDictionary, IOBluetoothSDPUUID.

## Parameters

- `element`: The data element value of one of the specified types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpdataelement/withelementvalue(_:))*