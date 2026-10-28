# canAddSecureElementPass(primaryAccountIdentifier:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) canAddSecureElementPassWithPrimaryAccountIdentifier:(NSString *) primaryAccountIdentifier;
```

## Return Value

[`true`](../../Swift/true.md) if PassKit can add a secure element pass for the specified account; otherwise, [`false`](../../Swift/false.md).

## Discussion

Adding a Secure Element pass requires a special entitlement that Apple provides. If the entitlement isn’t present, this method returns [`false`](../../Swift/false.md).

## Parameters

- `primaryAccountIdentifier`: A unique identifer for the underlying primary account number (PAN) for funding transactions. This isn’t the PAN itself.

## See Also

### Adding passes
- [func canAddFelicaPass() -> Bool](./canaddfelicapass%28%29.md)
  Returns a Boolean value that indicates whether the library can add FeliCa™ passes.
- [func addPasses([PKPass], withCompletionHandler: ((PKPassLibraryAddPassesStatus) -> Void)?)](./addpasses%28_,withcompletionhandler%29.md)
  Presents a user interface for adding multiple passes at once.
- [enum PKPassLibraryAddPassesStatus](../pkpasslibraryaddpassesstatus.md)
  Statuses that PassKit uses when it adds passes to the pass library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/canaddsecureelementpass(primaryaccountidentifier:))*