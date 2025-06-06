# attributes

**Framework**: IOBluetooth  
**Kind**: property

Returns an NSDictionary containing the attributes for the service.

**Availability**:
- macOS ?+

## Declaration

```swift
var attributes: [AnyHashable : Any]! { get }
```

#### Return Value

Returns an NSDictionary containing the attributes for the target service.

#### Discussion

The attribute dictionary is keyed off of the attribute id represented as an NSNumber. The values in the NSDictionary are IOBluetoothSDPDataElement objects representing the data element for the given attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecord/attributes)*