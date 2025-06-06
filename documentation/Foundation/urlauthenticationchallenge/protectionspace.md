# protectionSpace

**Framework**: Foundation  
**Kind**: property

The receiver’s protection space.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var protectionSpace: URLProtectionSpace { get }
```

## Mentions

- [Performing manual server trust authentication](performing-manual-server-trust-authentication.md)

#### Discussion

A protection space object provides additional information about the authentication request, such as the host, port, authentication realm, and so on. The protection space also tells you whether the authentication challenge is asking you to provide the user’s credentials or to verify the TLS credentials provided by the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlauthenticationchallenge/protectionspace)*