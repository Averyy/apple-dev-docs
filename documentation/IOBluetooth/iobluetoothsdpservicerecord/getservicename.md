# getServiceName()

**Framework**: IOBluetooth  
**Kind**: method

Returns the name of the service.

**Availability**:
- macOS ?+

## Declaration

```swift
func getServiceName() -> String!
```

#### Return Value

Returns the name of the target service.

#### Discussion

This is currently implemented to simply return the attribute with an id of 0x0100. In the future, it will be extended to allow name localization based on the user’s chosen language or other languages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecord/getservicename())*