# https(host:path:)

**Framework**: Authentication Services  
**Kind**: method

Creates a callback object that matches against HTTPS URLs with the given host and path.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
class func https(host: String, path: String) -> Self
```

#### Discussion

The following example creates a session that requires a callback with an `https://` URL:

```swift
let session = ASWebAuthenticationSession(
    url: URL(string: "https://example.com/oauth/login/authorize")!,
    callback: .https(host: "auth.example.com", path: "/auth/callback/example")
) { callbackURL, error in
    // Handle the session result.
}
```

## Parameters

- `host`: The host that the app requires in the callback URL. The host must be a member of a domain associated with the app, as described in  .
- `path`: The path that the app requires in the callback URL.

## See Also

- [class func customScheme(String) -> Self](aswebauthenticationsession/callback/customscheme(_:).md)
  Creates a callback object that matches against URLs with the given custom scheme.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsession/callback/https(host:path:))*