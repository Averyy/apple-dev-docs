# isBusy()

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Get the action state of the module

**Availability**:
- macOS

## Declaration

```swift
func isBusy() -> Bool
```

```objc
- (BOOL) isBusy;
```

#### Return Value

Success or failure code.

#### Discussion

OBEXFileTransferServices will be considered “busy” when an operation in taking place or has not completed. Calling abort: on this module will not automatically reset its busy state. The user will have to wait for the operation to complete or for the current operation to timeout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/isbusy())*