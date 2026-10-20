# init(serviceDictionary:device:)

**Framework**: IOBluetooth  
**Kind**: init  
**Role**: Initializer

Returns an initialized IOBluetoothSDPServiceRecord * with the attributes specified in the provided service dictionary. Provide a pointer to an IOBlueotothDevice if you wish to associate the record to a specific IOBluetoothDevice.

**Availability**:
- macOS

## Declaration

```swift
init!(serviceDictionary serviceDict: [AnyHashable : Any]!, device: IOBluetoothDevice!)
```

```objc
- (instancetype) initWithServiceDictionary:(NSDictionary *) serviceDict device:(IOBluetoothDevice *) device;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecord/init(servicedictionary:device:))*