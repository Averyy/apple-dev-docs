# customScheme(_:)

**Framework**: Authentication Services  
**Kind**: method

Creates a callback object that matches against URLs with the given custom scheme.

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
class func customScheme(_ customScheme: String) -> Self
```

#### Discussion

The following example creates a session that requires a callback with a custom URL scheme:

```swift
let session = ASWebAuthenticationSession(
    url: URL(string: "https://example.com/oauth/login/authorize")!,
    callback: .customScheme("myappscheme")
) { callbackURL, error in
    // Handle the session result.
}
```

## Parameters

- `customScheme`: The custom scheme that the app requires in the callback URL.

## See Also

- [class func https(host: String, path: String) -> Self](aswebauthenticationsession/callback/https(host:path:).md)
  Creates a callback object that matches against HTTPS URLs with the given host and path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsession/callback/customscheme(_:))*