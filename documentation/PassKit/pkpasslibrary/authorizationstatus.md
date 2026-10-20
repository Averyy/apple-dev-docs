# PKPassLibrary.AuthorizationStatus

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum  
**Role**: Enumeration

Statuses that indicate whether a person authorized your app to add a pass to their Wallet.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
enum AuthorizationStatus
```

```c
enum PKPassLibraryAuthorizationStatus : NSInteger;
```

## Topics

### Authorization statuses
- [PKPassLibrary.AuthorizationStatus.authorized](./authorizationstatus/authorized.md)
  A status that occurs when the person allows your app to add one or more passes to Wallet.
- [PKPassLibrary.AuthorizationStatus.denied](./authorizationstatus/denied.md)
  A status that occurs when the person doesn’t allow your app to add one or more passes to Wallet.
- [PKPassLibrary.AuthorizationStatus.notDetermined](./authorizationstatus/notdetermined.md)
  A status that occurs when the authorization status isn’t specified.
- [PKPassLibrary.AuthorizationStatus.restricted](./authorizationstatus/restricted.md)
  A status that occurs when the authorization status is limited.
### Initializers
- [init?(rawValue: Int)](./authorizationstatus/init%28rawvalue%29.md)

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
- [PKPassLibrary.Capability](./capability.md)
  Features for which your app can request authorization from a person.
- [func addPasses([PKPass], withCompletionHandler: ((PKPassLibraryAddPassesStatus) -> Void)?)](./addpasses%28_,withcompletionhandler%29.md)
  Presents a user interface for adding multiple passes at once.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/authorizationstatus)*