# PKPassLibrary.Capability

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum

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

#### Discussion

Pass a capability to [`authorizationStatus(for:)`](pkpasslibrary/authorizationstatus(for:).md) or [`requestAuthorization(for:completion:)`](pkpasslibrary/requestauthorization(for:completion:).md) to check or request someone’s permission to use that feature. Currently, [`PKPassLibrary.Capability.backgroundAddPasses`](pkpasslibrary/capability/backgroundaddpasses.md) is the only capability PassKit defines; it controls whether your app can add passes to Wallet automatically, without prompting the person to review or confirm each pass.

## Topics

### Capabilities
- [PKPassLibrary.Capability.backgroundAddPasses](pkpasslibrary/capability/backgroundaddpasses.md)
  A capability that lets your app add passes to Wallet automatically, without prompting the person to review or confirm each pass.
### Initializers
- [init?(rawValue: Int)](pkpasslibrary/capability/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func requestAuthorization(for: PKPassLibrary.Capability, completion: (PKPassLibrary.AuthorizationStatus) -> Void)](pkpasslibrary/requestauthorization(for:completion:).md)
  Requests a person’s authorization to use a pass library capability.
- [PKPassLibrary.AuthorizationStatus](pkpasslibrary/authorizationstatus.md)
  Statuses that indicate whether a person authorized your app to add a pass to their Wallet.
- [func addPasses([PKPass], withCompletionHandler: ((PKPassLibraryAddPassesStatus) -> Void)?)](pkpasslibrary/addpasses(_:withcompletionhandler:).md)
  Presents a user interface for adding multiple passes at once.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/capability)*