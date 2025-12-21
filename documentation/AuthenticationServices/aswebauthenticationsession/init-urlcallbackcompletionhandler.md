# init(url:callback:completionHandler:)

**Framework**: Authentication Services  
**Kind**: init

Creates a web authentication session instance that uses a callback to evaluate a redirection URL.

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
init(url URL: URL, callback: ASWebAuthenticationSession.Callback, completionHandler: @escaping ASWebAuthenticationSession.CompletionHandler)
```

#### Discussion

The following example creates a session that requires a callback with a custom URL scheme, using the [`customScheme(_:)`](aswebauthenticationsession/callback/customscheme(_:).md) type method to create the `callback` parameter:

```swift
let session = ASWebAuthenticationSession(
    url: URL(string: "https://example.com/oauth/login/authorize")!,
    callback: .customScheme("myappscheme")
) { callbackURL, error in
    // Handle the session result.
}
```

## Parameters

- `URL`: The initial URL pointing to the authentication webpage. This initializer only supports URLs with   or   schemes.
- `callback`: An object that describes when the session calls its completion handler.
- `completionHandler`: A completion handler that the system calls when the session completes successfully, or when the person using the app cancels the request.

## See Also

- [ASWebAuthenticationSession.Callback](aswebauthenticationsession/callback.md)
  An object for evaluating navigation events in an authentication session.
- [ASWebAuthenticationSession.CompletionHandler](aswebauthenticationsession/completionhandler.md)
  A completion handler for the web authentication session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsession/init(url:callback:completionhandler:))*