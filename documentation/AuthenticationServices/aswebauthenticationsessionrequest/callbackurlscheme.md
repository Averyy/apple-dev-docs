# callbackURLScheme

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The scheme for the browser to use when returning the result of the authentication attempt to the app requesting it.

**Availability**:
- macOS 10.15+ - Deprecated in 14.4

> **Deprecated**: Use [`callback`](./callback.md) to match all callback types.

## Declaration

```swift
var callbackURLScheme: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * callbackURLScheme;
```

## Mentions

- [Supporting Single Sign-On in a Web Browser App](../supporting-single-sign-on-in-a-web-browser-app.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionrequest/callbackurlscheme)*