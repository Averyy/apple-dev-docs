# systemExtensionWillBecomeInactive(_:)

**Framework**: System Extensions  
**Kind**: method

**Availability**:
- macOS 15.1+

## Declaration

```swift
optional func systemExtensionWillBecomeInactive(_ systemExtensionInfo: OSSystemExtensionInfo)
```

#### Discussion

This delegate method will be called when a system extension is deactivated and is about to get uninstalled. The extension may still be running until the system is rebooted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionsworkspaceobserver/systemextensionwillbecomeinactive(_:))*