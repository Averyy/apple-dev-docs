# canAddFelicaPass()

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) canAddFelicaPass;
```

#### Discussion

By default, this method returns [`false`](../../Swift/false.md).

## See Also

### Adding passes
- [func canAddSecureElementPass(primaryAccountIdentifier: String) -> Bool](./canaddsecureelementpass%28primaryaccountidentifier%29.md)
  Returns a Boolean value that indicates whether PassKit can add a Secure Element pass for the specified account.
- [func addPasses([PKPass], withCompletionHandler: ((PKPassLibraryAddPassesStatus) -> Void)?)](./addpasses%28_,withcompletionhandler%29.md)
  Presents a user interface for adding multiple passes at once.
- [enum PKPassLibraryAddPassesStatus](../pkpasslibraryaddpassesstatus.md)
  Statuses that PassKit uses when it adds passes to the pass library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/canaddfelicapass())*