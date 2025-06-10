# createNFCSlot(message:completion:)

**Framework**: CryptoTokenKit  
**Kind**: method

Creates an NFC smart card slot using the device’s hardware and presents a system UI.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
func createNFCSlot(message: String?) async throws -> TKSmartCardSlotNFCSession
```

#### Discussion

To finish the NFC session and dismiss the system-presented UI use `TKSmartCardSlotNFCSession.endSession`.

## Parameters

- `message`: Message shown in the system-presented UI
- `completion`: Completion handler which returns the NFC session of the created slot or an error on failure.   If an NFC slot already exists and current caller is not the initial creator   error is returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotmanager/createnfcslot(message:completion:))*