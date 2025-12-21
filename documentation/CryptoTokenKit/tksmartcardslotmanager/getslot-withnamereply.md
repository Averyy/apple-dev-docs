# getSlot(withName:reply:)

**Framework**: CryptoTokenKit  
**Kind**: method

Asynchronously calls a block with a Smart Card reader slot for a specified name.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func getSlot(withName name: String) async -> TKSmartCardSlot?
```

## Parameters

- `name`: The name of the Smart Card reader slot.
- `reply`: 

## See Also

- [var slotNames: [String]](tksmartcardslotmanager/slotnames.md)
  A list of identifiers for all the Smart Card reader slots available to the system.
- [func slotNamed(String) -> TKSmartCardSlot?](tksmartcardslotmanager/slotnamed(_:).md)
  Returns the Smart Card slot with a given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotmanager/getslot(withname:reply:))*