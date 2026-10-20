# init(url:callbackURLScheme:completionHandler:)

**Framework**: Authentication Services  
**Kind**: init  
**Role**: Initializer

Creates a web authentication session instance.

**Availability**:
- iOS 12.0+ - Deprecated in 27.2
- iPadOS 12.0+ - Deprecated in 27.2
- Mac Catalyst 12.0+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- tvOS 16.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 6.2+ - Deprecated in 27.2

> **Deprecated**: Use [`init(url:callback:completionHandler:)`](./init%28url,callback,completionhandler%29-6nut7.md) to handle callbacks.

## Declaration

```swift
init(url URL: URL, callbackURLScheme: String?, completionHandler: @escaping ASWebAuthenticationSession.CompletionHandler)
```

```objc
- (instancetype) initWithURL:(NSURL *) URL callbackURLScheme:(NSString *) callbackURLScheme completionHandler:(ASWebAuthenticationSessionCompletionHandler) completionHandler;
```

## Parameters

- `URL`: A URL with the `http` or `https` scheme pointing to the authentication webpage.
- `callbackURLScheme`: The custom URL scheme that the app requires in the callback URL.
- `completionHandler`: A completion handler the session calls when it completes successfully, or when the user cancels the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsession/init(url:callbackurlscheme:completionhandler:)-7fpox)*