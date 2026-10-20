# cancel()

**Framework**: Safari Services  
**Kind**: method  
**Role**: Instance Method

Cancels the currently running session when the consent dialog is up or when the webpage is up. This is how applications stop the login process.

**Availability**:
- iOS 11.0+ - Deprecated in 12.0 (renamed: ASWebAuthenticationSession)
- iPadOS 11.0+ - Deprecated in 12.0 (renamed: ASWebAuthenticationSession)
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
func cancel()
```

```objc
- (void) cancel;
```

## See Also

### Instance Methods
- [func start() -> Bool](./start%28%29.md)
  Starts the session after initializing an instance of SFAuthenticationSession. This will trigger the consent dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfauthenticationsession/cancel())*