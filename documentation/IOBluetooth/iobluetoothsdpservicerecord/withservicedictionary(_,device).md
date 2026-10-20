# withServiceDictionary(_:device:)

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Type Method

Returns an IOBluetoothSDPServiceRecord * with the attributes specified in the provided service dictionary. Provide a pointer to an IOBlueotothDevice if you wish to associate the record to a specific IOBluetoothDevice.

**Availability**:
- macOS

## Declaration

```swift
class func withServiceDictionary(_ serviceDict: [AnyHashable : Any]!, device: IOBluetoothDevice!) -> Self!
```

```objc
+ (instancetype) withServiceDictionary:(NSDictionary *) serviceDict device:(IOBluetoothDevice *) device;
```

#### Return Value

Returns an IOBluetoothSDPServiceRecord * with the attributes specified in the provided dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecord/withservicedictionary(_:device:))*