# init(url:callbackURLScheme:completionHandler:)

**Framework**: Authentication Services  
**Kind**: init

Creates a web authentication session instance.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.15+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
init(url URL: URL, callbackURLScheme: String?, completionHandler: @escaping ASWebAuthenticationSession.CompletionHandler)
```

## Parameters

- `URL`: A URL with the   or   scheme pointing to the authentication webpage.
- `callbackURLScheme`: The custom URL scheme that the app requires in the callback URL.
- `completionHandler`: A completion handler the session calls when it completes successfully, or when the user cancels the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsession/init(url:callbackurlscheme:completionhandler:))*