# placeAllOthers(onHold:)

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Places all calls except the call with the specified index on hold.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func placeAllOthers(onHold index: Int32)
```

```objc
- (void) placeAllOthersOnHold:(int) index;
```

## Parameters

- `index`: The index of the call that remains active.

## See Also

### Holding Calls
- [func holdCall()](./holdcall%28%29.md)
  Places all active calls on hold and accepts a held or waiting call.
- [func addHeldCall()](./addheldcall%28%29.md)
  Adds held calls to the current conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/placeallothers(onhold:))*