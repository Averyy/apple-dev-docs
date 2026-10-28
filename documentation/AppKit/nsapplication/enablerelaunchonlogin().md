# enableRelaunchOnLogin()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Enables relaunching the app on login.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func enableRelaunchOnLogin()
```

```objc
- (void) enableRelaunchOnLogin;
```

## Discussion

Invoking this method will cause the app to relaunch when the user next logs in to their account.

This methods is thread safe.

## See Also

### Managing relaunch on login
- [func disableRelaunchOnLogin()](./disablerelaunchonlogin%28%29.md)
  Disables relaunching the app on login.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/enablerelaunchonlogin())*