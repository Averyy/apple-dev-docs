# sortedAttributes

**Framework**: IOBluetooth  
**Kind**: property  
**Role**: Instance Property

Returns a sorted array of SDP attributes

**Availability**:
- macOS

## Declaration

```swift
var sortedAttributes: [Any]! { get }
```

```objc
@property (copy, readonly) NSArray * sortedAttributes;
```

## Return Value

Returns a sorted array of SDP attributes

## Discussion

This method will walk all the elements of the service record and return an array of IOBluetoothSDPServiceAttribute objects sorted by attributeID


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecord/sortedattributes-swift.property)*