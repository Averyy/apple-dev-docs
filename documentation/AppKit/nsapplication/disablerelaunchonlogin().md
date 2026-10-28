# disableRelaunchOnLogin()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Disables relaunching the app on login.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func disableRelaunchOnLogin()
```

```objc
- (void) disableRelaunchOnLogin;
```

## Discussion

Invoking this method will prevent the app from relaunching when the user next logs in to their account.

If your app shouldn’t be relaunched because it launches via some other mechanism (for example, `launchd`), then the recommended usage is to call this method once, and never pair it with an [`enableRelaunchOnLogin()`](./enablerelaunchonlogin%28%29.md) method.

If your app shouldn’t be relaunched because it triggers a restart, for example an installer, then the recommended usage is to invoke this method immediately before you attempt to trigger a restart, and [`enableRelaunchOnLogin()`](./enablerelaunchonlogin%28%29.md) immediately after. This is because the user may cancel restarting; if the user later restarts for another reason, then your app should be brought back.

This methods is thread safe.

## See Also

### Managing relaunch on login
- [func enableRelaunchOnLogin()](./enablerelaunchonlogin%28%29.md)
  Enables relaunching the app on login.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/disablerelaunchonlogin())*