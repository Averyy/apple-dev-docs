# account

**Framework**: Social  
**Kind**: property

Account information used to authenticate the request.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
var account: ACAccount! { get set }
```

#### Discussion

The account is used to sign a request with OAuth1 services or to add an access token for OAuth2 services. By associating the account with the request, the necessary tokens are added automatically. The default value is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slrequest/account)*