# slotNamed(_:)

**Framework**: CryptoTokenKit  
**Kind**: method

Returns the Smart Card slot with a given name.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func slotNamed(_ name: String) -> TKSmartCardSlot?
```

#### Return Value

The slot with the specified name, or `nil` if no slot with that name exists.

## See Also

- [var slotNames: [String]](tksmartcardslotmanager/slotnames.md)
  A list of identifiers for all the Smart Card reader slots available to the system.
- [func getSlot(withName: String, reply: (TKSmartCardSlot?) -> Void)](tksmartcardslotmanager/getslot(withname:reply:).md)
  Asynchronously calls a block with a Smart Card reader slot for a specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotmanager/slotnamed(_:))*