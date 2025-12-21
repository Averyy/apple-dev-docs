# canAddFelicaPass()

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Returns a Boolean value that indicates whether the library can add FeliCa™ passes.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 3.1+

## Declaration

```swift
func canAddFelicaPass() -> Bool
```

#### Discussion

By default, this method returns [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func canAddSecureElementPass(primaryAccountIdentifier: String) -> Bool](pkpasslibrary/canaddsecureelementpass(primaryaccountidentifier:).md)
  Returns a Boolean value that indicates whether PassKit can add a Secure Element pass for the specified account.
- [func addPasses([PKPass], withCompletionHandler: ((PKPassLibraryAddPassesStatus) -> Void)?)](pkpasslibrary/addpasses(_:withcompletionhandler:).md)
  Presents a user interface for adding multiple passes at once.
- [enum PKPassLibraryAddPassesStatus](pkpasslibraryaddpassesstatus.md)
  Statuses that PassKit uses when it adds passes to the pass library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/canaddfelicapass())*