# LiveAssistanceLaunchReason.additionalInfo

**Framework**: LiveCommunicationKit  
**Kind**: case

A launch reason that indicates the person using the extension needs to provide some information not related to authentication.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)
- Mac Catalyst 27.1+ (Beta)
- macOS 27.1+
- visionOS 27.1+

## Declaration

```swift
case additionalInfo
```

#### Discussion

Use this value when your extension needs information like a language preference or other configuration. You might also use this value when you want confirmation to proceed with establishing the assistance service.

## See Also

- [LiveAssistanceLaunchReason.signIn](liveassistancelaunchreason/signin.md)
  A launch reason that indicates the person using the extension isn’t signed into the VRS provider service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistancelaunchreason/additionalinfo)*