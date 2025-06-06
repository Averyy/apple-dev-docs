# init(type:sizeDescriptor:size:value:)

**Framework**: IOBluetooth  
**Kind**: init

Initializes a new IOBluetoothSDPDataElement with the given attributes.

**Availability**:
- macOS ?+

## Declaration

```swift
init!(type newType: BluetoothSDPDataElementTypeDescriptor, sizeDescriptor newSizeDescriptor: BluetoothSDPDataElementSizeDescriptor, size newSize: UInt32, value newValue: NSObject!)
```

#### Return Value

Returns self if successful. Returns nil if an error is encountered (not likely due to the limited error checking currently done).

#### Discussion

Warning - be careful using this method. There is next to no error checking done on the attributes. It is entirely possible to construct an invalid data element. It is recommended that +withElementValue: be used instead of this one.

## Parameters

- `newType`: The type descriptor for the data element.
- `newSizeDescriptor`: The size descriptor for the data element (verify it matches the size parameter).
- `newSize`: The size of the data element in bytes (make sure it is a valid size for the given size descriptor).
- `newValue`: The raw value itself. This must be the base NSString, NSNumber, NSArray or NSData objects. It may not be NSDictionary. If a dictionary format is present, use +withElementValue:.

## See Also

- [init!(elementValue: NSObject!)](iobluetoothsdpdataelement/init(elementvalue:).md)
  Initializes a new IOBluetoothSDPDataElement with the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpdataelement/init(type:sizedescriptor:size:value:))*