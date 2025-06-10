# getSlot(withName:reply:)

**Framework**: CryptoTokenKit  
**Kind**: method

Asynchronously calls a block with a Smart Card reader slot for a specified name.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func getSlot(withName name: String) async -> TKSmartCardSlot?
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func getSlot(withName name: String) async -> TKSmartCardSlot?
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

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