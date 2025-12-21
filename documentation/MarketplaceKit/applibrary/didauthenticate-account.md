# didAuthenticate(account:)

**Framework**: MarketplaceKit  
**Kind**: method

Instructs iOS to reinstall an app after a required reuthorization completes.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+

## Declaration

```swift
nonisolated
final func didAuthenticate(account: String) async
```

## Mentions

- [Reauthenticating a person to manage apps](reauthenticating-a-person-to-manage-apps.md)

#### Discussion

The marketplace or other web-distributed app calls this method after reauthenticating a person when the access token expires. For more information, see [`Reauthenticating a person to manage apps`](reauthenticating-a-person-to-manage-apps.md).

## Parameters

- `account`: The account ID or username for the person. The marketplace server provides this value in the   installation request.

## See Also

- [static let current: AppLibrary](applibrary/current.md)
  A global accessor for the device’s app library instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/didauthenticate(account:))*