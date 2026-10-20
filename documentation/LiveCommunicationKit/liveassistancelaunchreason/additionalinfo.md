# LiveAssistanceLaunchReason.additionalInfo

**Framework**: LiveCommunicationKit  
**Kind**: case  
**Role**: Case

A launch reason that indicates the person using the extension needs to provide some information not related to authentication.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- visionOS 27.2+

## Declaration

```swift
case additionalInfo
```

#### Discussion

Use this value when your extension needs information like a language preference or other configuration. You might also use this value when you want confirmation to proceed with establishing the assistance service.

## See Also

### Working with launch reasons
- [LiveAssistanceLaunchReason.signIn](./signin.md)
  A launch reason that indicates the person using the extension isn’t signed into the VRS provider service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistancelaunchreason/additionalinfo)*