# systemExtensionWillBecomeDisabled(_:)

**Framework**: System Extensions  
**Kind**: method

**Availability**:
- macOS 15.1+

## Declaration

```swift
optional func systemExtensionWillBecomeDisabled(_ systemExtensionInfo: OSSystemExtensionInfo)
```

#### Discussion

This delegate method will be called when the user disables an already enabled system extension, or when the system extension is first installed and is in the disabled state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionsworkspaceobserver/systemextensionwillbecomedisabled(_:))*