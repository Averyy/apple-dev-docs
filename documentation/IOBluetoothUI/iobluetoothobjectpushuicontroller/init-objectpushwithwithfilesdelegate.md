# init(objectPushWith:withFiles:delegate:)

**Framework**: IOBluetooth UI  
**Kind**: init

Creates and returns a new IOBluetoothObjectPush object

**Availability**:
- macOS 10.2+

## Declaration

```swift
@MainActor
init!(objectPushWith inDevice: IOBluetoothDevice!, withFiles inFiles: [Any]!, delegate inDelegate: Any!)
```

#### Discussion

The event delegate should implement a single delegate method:

- (void) objectPushComplete: (IOBluetoothObjectPushUIController*) inPusher

The method will be called when the transaction is complete and should be used to release the push object by the delegate. If no delegate is set the object will release itself when the transfer is finished.

## Parameters

- `inDevice`: The remote device to send the files to
- `inFiles`: An array of file paths to send
- `inDelegate`: A delegate object that implements the single method above. If no delegate is specified this object will release itself when the transaction is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothobjectpushuicontroller/init(objectpushwith:withfiles:delegate:))*