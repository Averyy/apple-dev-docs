# start()

**Framework**: Safari Services  
**Kind**: method  
**Role**: Instance Method

Starts the session after initializing an instance of SFAuthenticationSession. This will trigger the consent dialog.

**Availability**:
- iOS 11.0+ - Deprecated in 12.0 (renamed: ASWebAuthenticationSession)
- iPadOS 11.0+ - Deprecated in 12.0 (renamed: ASWebAuthenticationSession)
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
func start() -> Bool
```

```objc
- (BOOL) start;
```

## See Also

### Instance Methods
- [func cancel()](./cancel%28%29.md)
  Cancels the currently running session when the consent dialog is up or when the webpage is up. This is how applications stop the login process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfauthenticationsession/start())*