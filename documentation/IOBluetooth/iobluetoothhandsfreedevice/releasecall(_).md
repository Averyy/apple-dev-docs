# releaseCall(_:)

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Ends the call with the specified index.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func releaseCall(_ index: Int32)
```

```objc
- (void) releaseCall:(int) index;
```

## Parameters

- `index`: The index of the call to end.

## See Also

### Ending Calls
- [func endCall()](./endcall%28%29.md)
  Ends the current call or refuses an incoming call.
- [func releaseActiveCalls()](./releaseactivecalls%28%29.md)
  Ends all active calls and accepts a held or waiting call.
- [func releaseHeldCalls()](./releaseheldcalls%28%29.md)
  Ends all calls that are on hold or returns a busy signal for a waiting call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/releasecall(_:))*