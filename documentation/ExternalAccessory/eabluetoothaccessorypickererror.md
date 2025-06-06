# EABluetoothAccessoryPickerError

**Framework**: External Accessory  
**Kind**: struct

Error codes returned by the Bluetooth accessory picker.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
struct EABluetoothAccessoryPickerError
```

## Topics

### Error Codes
- [static var alreadyConnected: EABluetoothAccessoryPickerError.Code](eabluetoothaccessorypickererror/alreadyconnected.md)
- [static var resultCancelled: EABluetoothAccessoryPickerError.Code](eabluetoothaccessorypickererror/resultcancelled.md)
- [static var resultFailed: EABluetoothAccessoryPickerError.Code](eabluetoothaccessorypickererror/resultfailed.md)
- [static var resultNotFound: EABluetoothAccessoryPickerError.Code](eabluetoothaccessorypickererror/resultnotfound.md)
### Type Properties
- [static var errorDomain: String](eabluetoothaccessorypickererror/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func showBluetoothAccessoryPicker(withNameFilter: NSPredicate?, completion: EABluetoothAccessoryPickerCompletion?)](eaaccessorymanager/showbluetoothaccessorypicker(withnamefilter:completion:).md)
  Displays an alert that allows the user to pair the device with a Bluetooth accessory.
- [typealias EABluetoothAccessoryPickerCompletion](eabluetoothaccessorypickercompletion.md)
  The completion block for the Bluetooth picker.
- [EABluetoothAccessoryPickerError.Code](eabluetoothaccessorypickererror/code.md)
  The error codes that may be passed in an error object for the Bluetooth picker completion block.
- [let EABluetoothAccessoryPickerErrorDomain: String](eabluetoothaccessorypickererrordomain.md)
  The domain for errors passed to a Bluetooth picker completion block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererror)*