# init(elementValue:)

**Framework**: IOBluetooth  
**Kind**: init

Initializes a new IOBluetoothSDPDataElement with the given value.

**Availability**:
- macOS ?+

## Declaration

```swift
init!(elementValue element: NSObject!)
```

#### Return Value

Returns self if successful. Returns nil if there was an error parsing the element value.

#### Discussion

The value must follow the format listed above and must be an instance of NSData, NSString, NSNumber, NSArray, NSDictionary, IOBluetoothSDPUUID.

## Parameters

- `element`: The data element value of one of the specified types.

## See Also

- [init!(type: BluetoothSDPDataElementTypeDescriptor, sizeDescriptor: BluetoothSDPDataElementSizeDescriptor, size: UInt32, value: NSObject!)](iobluetoothsdpdataelement/init(type:sizedescriptor:size:value:).md)
  Initializes a new IOBluetoothSDPDataElement with the given attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpdataelement/init(elementvalue:))*