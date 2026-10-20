# isSessionTargetAMac()

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Tells whether the target device is a Mac by checking its service record.

**Availability**:
- macOS

## Declaration

```swift
func isSessionTargetAMac() -> Bool
```

```objc
- (BOOL) isSessionTargetAMac;
```

#### Return Value

TRUE only if device service record has Mac entry, FALSE for all else.

#### Discussion

Tells whether the target device is a Mac by checking its service record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothobexsession/issessiontargetamac())*