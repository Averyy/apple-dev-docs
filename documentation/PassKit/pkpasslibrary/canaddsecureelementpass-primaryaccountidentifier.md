# canAddSecureElementPass(primaryAccountIdentifier:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Returns a Boolean value that indicates whether PassKit can add a Secure Element pass for the specified account.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.12+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
func canAddSecureElementPass(primaryAccountIdentifier: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if PassKit can add a secure element pass for the specified account; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Adding a Secure Element pass requires a special entitlement that Apple provides. If the entitlement isn’t present, this method returns [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `primaryAccountIdentifier`: A unique identifer for the underlying primary account number (PAN) for funding transactions. This isn’t the PAN itself.

## See Also

- [func canAddFelicaPass() -> Bool](pkpasslibrary/canaddfelicapass.md)
  Returns a Boolean value that indicates whether the library can add FeliCa™ passes.
- [func addPasses([PKPass], withCompletionHandler: ((PKPassLibraryAddPassesStatus) -> Void)?)](pkpasslibrary/addpasses(_:withcompletionhandler:).md)
  Presents a user interface for adding multiple passes at once.
- [enum PKPassLibraryAddPassesStatus](pkpasslibraryaddpassesstatus.md)
  Statuses that PassKit uses when it adds passes to the pass library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/canaddsecureelementpass(primaryaccountidentifier:))*