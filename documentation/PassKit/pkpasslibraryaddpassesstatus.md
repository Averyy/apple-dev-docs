# PKPassLibraryAddPassesStatus

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum  
**Role**: Enumeration

Statuses that PassKit uses when it adds passes to the pass library.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum PKPassLibraryAddPassesStatus
```

```c
enum PKPassLibraryAddPassesStatus : NSInteger;
```

## Topics

### Constants
- [PKPassLibraryAddPassesStatus.didAddPasses](./pkpasslibraryaddpassesstatus/didaddpasses.md)
  A status that occurs when the user successfully adds one or more passes.
- [PKPassLibraryAddPassesStatus.shouldReviewPasses](./pkpasslibraryaddpassesstatus/shouldreviewpasses.md)
  A status that occurs when the app prompts the user to review the passes.
- [PKPassLibraryAddPassesStatus.didCancelAddPasses](./pkpasslibraryaddpassesstatus/didcanceladdpasses.md)
  A status that occurs when the user cancels the addition of passes.
### Initializers
- [init?(rawValue: Int)](./pkpasslibraryaddpassesstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Adding passes
- [func canAddSecureElementPass(primaryAccountIdentifier: String) -> Bool](./pkpasslibrary/canaddsecureelementpass%28primaryaccountidentifier%29.md)
  Returns a Boolean value that indicates whether PassKit can add a Secure Element pass for the specified account.
- [func canAddFelicaPass() -> Bool](./pkpasslibrary/canaddfelicapass%28%29.md)
  Returns a Boolean value that indicates whether the library can add FeliCa™ passes.
- [func addPasses([PKPass], withCompletionHandler: ((PKPassLibraryAddPassesStatus) -> Void)?)](./pkpasslibrary/addpasses%28_,withcompletionhandler%29.md)
  Presents a user interface for adding multiple passes at once.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibraryaddpassesstatus)*