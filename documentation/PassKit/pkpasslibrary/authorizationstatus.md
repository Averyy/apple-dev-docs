# PKPassLibrary.AuthorizationStatus

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum

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

## Topics

### Authorization statuses
- [PKPassLibrary.AuthorizationStatus.authorized](pkpasslibrary/authorizationstatus/authorized.md)
  A status that occurs when the person allows your app to add one or more passes to Wallet.
- [PKPassLibrary.AuthorizationStatus.denied](pkpasslibrary/authorizationstatus/denied.md)
  A status that occurs when the person doesn’t allow your app to add one or more passes to Wallet.
- [PKPassLibrary.AuthorizationStatus.notDetermined](pkpasslibrary/authorizationstatus/notdetermined.md)
  A status that occurs when the authorization status isn’t specified.
- [PKPassLibrary.AuthorizationStatus.restricted](pkpasslibrary/authorizationstatus/restricted.md)
  A status that occurs when the authorization status is limited.
### Initializers
- [init?(rawValue: Int)](pkpasslibrary/authorizationstatus/init(rawvalue:).md)

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
- [PKPassLibrary.Capability](pkpasslibrary/capability.md)
  Features for which your app can request authorization from a person.
- [func addPasses([PKPass], withCompletionHandler: ((PKPassLibraryAddPassesStatus) -> Void)?)](pkpasslibrary/addpasses(_:withcompletionhandler:).md)
  Presents a user interface for adding multiple passes at once.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/authorizationstatus)*