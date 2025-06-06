# addPasses(_:withCompletionHandler:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Presents a user interface for adding multiple passes at once.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func addPasses(_ passes: [PKPass]) async -> PKPassLibraryAddPassesStatus
```

#### Discussion

Use this method whenever the user initiates an action that generates a single pass (like purchasing a concert ticket) or multiple passes (like checking into a multiconnection flight). The user receives a prompt to confirm the overall action or to review the passes individually. If you want to force the user to review individual passes visually before adding them, use an instance of [`PKAddPassesViewController`](pkaddpassesviewcontroller.md).

## Parameters

- `passes`: The passes to add.
- `completion`: The completion handler that PassKit calls after the user selects an action. This handler takes the following parameter:

## See Also

- [func canAddSecureElementPass(primaryAccountIdentifier: String) -> Bool](pkpasslibrary/canaddsecureelementpass(primaryaccountidentifier:).md)
  Returns a Boolean value that indicates whether PassKit can add a Secure Element pass for the specified account.
- [func canAddFelicaPass() -> Bool](pkpasslibrary/canaddfelicapass.md)
  Returns a Boolean value that indicates whether the library can add FeliCa™ passes.
- [enum PKPassLibraryAddPassesStatus](pkpasslibraryaddpassesstatus.md)
  Statuses that PassKit uses when it adds passes to the pass library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/addpasses(_:withcompletionhandler:))*