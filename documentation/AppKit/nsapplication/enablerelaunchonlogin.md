# enableRelaunchOnLogin()

**Framework**: AppKit  
**Kind**: method

Enables relaunching the app on login.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func enableRelaunchOnLogin()
```

#### Discussion

Invoking this method will cause the app to relaunch when the user next logs in to their account.

This methods is thread safe.

## See Also

- [func disableRelaunchOnLogin()](nsapplication/disablerelaunchonlogin.md)
  Disables relaunching the app on login.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/enablerelaunchonlogin())*