# EABluetoothAccessoryPickerError.Code

**Framework**: External Accessory  
**Kind**: enum  
**Role**: Enumeration

The error codes that may be passed in an error object for the Bluetooth picker completion block.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

```c
enum EABluetoothAccessoryPickerErrorCode : NSInteger;
```

## Topics

### Error Codes
- [EABluetoothAccessoryPickerError.Code.alreadyConnected](./code/alreadyconnected.md)
  The specified accessory was already connected.
- [EABluetoothAccessoryPickerError.Code.resultNotFound](./code/resultnotfound.md)
  The specified accessory could not be found, perhaps because it was turned off prior to connection.
- [EABluetoothAccessoryPickerError.Code.resultCancelled](./code/resultcancelled.md)
  The user canceled the picker alert.
- [EABluetoothAccessoryPickerError.Code.resultFailed](./code/resultfailed.md)
  Selecting an accessory failed for an unknown reason.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Presenting the Bluetooth Picker
- [func showBluetoothAccessoryPicker(withNameFilter: NSPredicate?, completion: (((any Error)?) -> Void)?)](../eaaccessorymanager/showbluetoothaccessorypicker%28withnamefilter,completion%29.md)
  Displays an alert that allows the user to pair the device with a Bluetooth accessory.
- [typealias EABluetoothAccessoryPickerCompletion](../eabluetoothaccessorypickercompletion.md)
  The completion block for the Bluetooth picker.
- [struct EABluetoothAccessoryPickerError](../eabluetoothaccessorypickererror.md)
  Error codes returned by the Bluetooth accessory picker.
- [let EABluetoothAccessoryPickerErrorDomain: String](../eabluetoothaccessorypickererrordomain.md)
  The domain for errors passed to a Bluetooth picker completion block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererror/code)*