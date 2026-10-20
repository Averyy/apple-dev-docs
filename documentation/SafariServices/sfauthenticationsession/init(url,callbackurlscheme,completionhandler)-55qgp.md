# init(url:callbackURLScheme:completionHandler:)

**Framework**: Safari Services  
**Kind**: init  
**Role**: Initializer

Initializes the SFAuthenticationSession in an application.

**Availability**:
- iOS 11.0+ - Deprecated in 12.0 (renamed: ASWebAuthenticationSession)
- iPadOS 11.0+ - Deprecated in 12.0 (renamed: ASWebAuthenticationSession)
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
init(url URL: URL, callbackURLScheme: String?, completionHandler: @escaping SFAuthenticationSession.CompletionHandler)
```

```objc
- (instancetype) initWithURL:(NSURL *) URL callbackURLScheme:(NSString *) callbackURLScheme completionHandler:(SFAuthenticationCompletionHandler) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfauthenticationsession/init(url:callbackurlscheme:completionhandler:)-55qgp)*