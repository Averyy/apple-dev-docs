# inquiryWithDelegate:

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Type Method

Class method to create an inquiry object.

**Availability**:
- macOS

## Declaration

```objc
+ (instancetype) inquiryWithDelegate:(id) delegate;
```

## Return Value

A pointer to the created IOBluetoothDeviceInquiry object.

## Discussion

The inquiry is NOT automatically started. You musts call -start on it to start the search for in-range devices.

## Parameters

- `delegate`: A delegate object that wishes to receive messages from the inquiry object. Delegate methods are listed below, under IOBluetoothDeviceInquiryDelegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquiry/inquirywithdelegate:)*