# disableRelaunchOnLogin()

**Framework**: AppKit  
**Kind**: method

Disables relaunching the app on login.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func disableRelaunchOnLogin()
```

#### Discussion

Invoking this method will prevent the app from relaunching when the user next logs in to their account.

If your app shouldn’t be relaunched because it launches via some other mechanism (for example, `launchd`), then the recommended usage is to call this method once, and never pair it with an [`enableRelaunchOnLogin()`](nsapplication/enablerelaunchonlogin().md) method.

If your app shouldn’t be relaunched because it triggers a restart, for example an installer, then the recommended usage is to invoke this method immediately before you attempt to trigger a restart, and [`enableRelaunchOnLogin()`](nsapplication/enablerelaunchonlogin().md) immediately after. This is because the user may cancel restarting; if the user later restarts for another reason, then your app should be brought back.

This methods is thread safe.

## See Also

- [func enableRelaunchOnLogin()](nsapplication/enablerelaunchonlogin.md)
  Enables relaunching the app on login.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/disablerelaunchonlogin())*