# getSlot(withName:reply:)

**Framework**: CryptoTokenKit  
**Kind**: method  
**Role**: Instance Method

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
func getSlot(withName name: String, reply: @escaping @Sendable (TKSmartCardSlot?) -> Void)
```

```swift
func getSlot(withName name: String) async -> TKSmartCardSlot?
```

```objc
- (void) getSlotWithName:(NSString *) name reply:(void (^)(TKSmartCardSlot *slot)) reply;
```

## Parameters

- `name`: The name of the Smart Card reader slot.
- `reply`:

  - **slot**: The Smart Card reader slot corresponding to the specified name. If no slot exists with that name, this argument is `nil`.

## See Also

### Accessing Smart Card Slots
- [var slotNames: [String]](./slotnames.md)
  A list of identifiers for all the Smart Card reader slots available to the system.
- [func slotNamed(String) -> TKSmartCardSlot?](./slotnamed%28_%29.md)
  Returns the Smart Card slot with a given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotmanager/getslot(withname:reply:))*