# PKPassLibrary.AuthorizationStatus.denied

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case  
**Role**: Case

A status that occurs when the person doesn’t allow your app to add one or more passes to Wallet.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
case denied
```

```c
PKPassLibraryAuthorizationStatusDenied
```

## See Also

### Authorization statuses
- [PKPassLibrary.AuthorizationStatus.authorized](./authorized.md)
  A status that occurs when the person allows your app to add one or more passes to Wallet.
- [PKPassLibrary.AuthorizationStatus.notDetermined](./notdetermined.md)
  A status that occurs when the authorization status isn’t specified.
- [PKPassLibrary.AuthorizationStatus.restricted](./restricted.md)
  A status that occurs when the authorization status is limited.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/authorizationstatus/denied)*