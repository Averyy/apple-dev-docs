# inquiryLength

**Framework**: IOBluetooth  
**Kind**: property

Set the length of the inquiry that is performed each time -start is used on an inquiry object.

**Availability**:
- macOS ?+

## Declaration

```swift
var inquiryLength: UInt8 { get set }
```

#### Discussion

A default of 10 seconds is used, unless a different value is specified using this method. Note that if you have called -start again too quickly, your inquiry may actually take much longer than what length you specify, as inquiries are throttled in the system. Also note that if you have the inquiry object updating device names for you, the whole inquiry process could be much longer than the specified length, depending on the number of devices found and how responsive to name requests they are. If you -must- have a strict inquiry length, disable name updates. In other words, this “length” only refers to the actual device discovery portion of the whole inquiry process.

## Parameters

- `seconds`: Number of seconds the inquiry will search for in-range devices before refreshing device names, if specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquiry/inquirylength)*