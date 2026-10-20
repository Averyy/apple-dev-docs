# createNFCSlot(message:completion:)

**Framework**: CryptoTokenKit  
**Kind**: method  
**Role**: Instance Method

Creates an NFC smart card slot using the device’s hardware and presents a system UI.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func createNFCSlot(message: String?, completion: @escaping @Sendable (TKSmartCardSlotNFCSession?, (any Error)?) -> Void)
```

```swift
func createNFCSlot(message: String?) async throws -> TKSmartCardSlotNFCSession
```

```objc
- (void) createNFCSlotWithMessage:(NSString *) message completion:(void (^)(TKSmartCardSlotNFCSession *session, NSError *error)) completion;
```

#### Discussion

To finish the NFC session and dismiss the system-presented UI use `TKSmartCardSlotNFCSession.endSession`.

## Parameters

- `message`: Message shown in the system-presented UI
- `completion`: Completion handler which returns the NFC session of the created slot or an error on failure. If an NFC slot already exists and current caller is not the initial creator `TKErrorCodeObjectNotFound` error is returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotmanager/createnfcslot(message:completion:))*