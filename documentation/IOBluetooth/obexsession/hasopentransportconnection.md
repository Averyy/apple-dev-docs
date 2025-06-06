# hasOpenTransportConnection()

**Framework**: IOBluetooth  
**Kind**: method

You must override this - it will be called periodically to determine if a transport connection is open or not.

**Availability**:
- macOS ?+

## Declaration

```swift
func hasOpenTransportConnection() -> Bool
```

#### Return Value

Return whether or not the transport connection is still open.

#### Discussion

Tranport subclasses must override this! When called you simply return if the transport connection is still open or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexsession/hasopentransportconnection())*