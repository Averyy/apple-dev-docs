# systemExtensionWillBecomeEnabled(_:)

**Framework**: System Extensions  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 15.1+

## Declaration

```swift
optional func systemExtensionWillBecomeEnabled(_ systemExtensionInfo: OSSystemExtensionInfo)
```

```objc
- (void) systemExtensionWillBecomeEnabled:(OSSystemExtensionInfo *) systemExtensionInfo;
```

#### Discussion

This delegate method will be called when a system extension has been validated and allowed by the user to run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionsworkspaceobserver/systemextensionwillbecomeenabled(_:))*