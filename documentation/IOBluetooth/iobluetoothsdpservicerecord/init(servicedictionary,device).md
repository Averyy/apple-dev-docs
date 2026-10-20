# init(serviceDictionary:device:)

**Framework**: IOBluetooth  
**Kind**: init

Returns an initialized IOBluetoothSDPServiceRecord * with the attributes specified in the provided service dictionary. Provide a pointer to an IOBlueotothDevice if you wish to associate the record to a specific IOBluetoothDevice.

**Availability**:
- macOS ?+

## Declaration

```swift
init!(serviceDictionary serviceDict: [AnyHashable : Any]!, device: IOBluetoothDevice!)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecord/init(servicedictionary:device:))*