# setOpenTransportConnectionAsyncSelector(_:target:refCon:)

**Framework**: IOBluetooth  
**Kind**: method

Allows you to set the selector to be used when a transport connection is opened, or fails to open.

**Availability**:
- macOS ?+

## Declaration

```swift
func setOpenTransportConnectionAsyncSelector(_ inSelector: Selector!, target inSelectorTarget: Any!, refCon inUserRefCon: UnsafeMutableRawPointer!)
```

#### Discussion

You do not need to call this on the session typically, unless you have subclassed the OBEXSession to implement a new transport and that transport supports async opening of connections. If it does not support async open, then using this is pointless.

## Parameters

- `inSelector`: Selector to call on the target.
- `inSelectorTarget`: Target to be called with the selector.
- `inUserRefCon`: User’s refCon that will get passed to them when their selector is invoked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothobexsession/setopentransportconnectionasyncselector(_:target:refcon:))*