# PKPassLibrary.Capability

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum  
**Role**: Enumeration

Features for which your app can request authorization from a person.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
enum Capability
```

```c
enum PKPassLibraryCapability : NSInteger;
```

## Discussion

Pass a capability to [`authorizationStatus(for:)`](./authorizationstatus%28for%29.md) or [`requestAuthorization(for:completion:)`](./requestauthorization%28for,completion%29.md) to check or request someone’s permission to use that feature. Currently, [`PKPassLibrary.Capability.backgroundAddPasses`](./capability/backgroundaddpasses.md) is the only capability PassKit defines; it controls whether your app can add passes to Wallet automatically, without prompting the person to review or confirm each pass.

## Topics

### Capabilities
- [PKPassLibrary.Capability.backgroundAddPasses](./capability/backgroundaddpasses.md)
  A capability that lets your app add passes to Wallet automatically, without prompting the person to review or confirm each pass.
### Initializers
- [init?(rawValue: Int)](./capability/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Automatically adding passes
- [func requestAuthorization(for: PKPassLibrary.Capability, completion: (PKPassLibrary.AuthorizationStatus) -> Void)](./requestauthorization%28for,completion%29.md)
  Requests a person’s authorization to use a pass library capability.
- [PKPassLibrary.AuthorizationStatus](./authorizationstatus.md)
  Statuses that indicate whether a person authorized your app to add a pass to their Wallet.
- [func addPasses([PKPass], withCompletionHandler: ((PKPassLibraryAddPassesStatus) -> Void)?)](./addpasses%28_,withcompletionhandler%29.md)
  Presents a user interface for adding multiple passes at once.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/capability)*