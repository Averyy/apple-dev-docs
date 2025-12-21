# messageCornerRadius

**Framework**: Messages  
**Kind**: property  
**Required**: Yes

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var messageCornerRadius: CGFloat { get }
```

#### Discussion

The corner radius of the message when presented in the transcript. Use this value to create concentric rounded subviews inside your view. Use continuous corners (kCACornerCurveContinuous) on your view.

This property varies with dynamic type size. Use trait collection registration to trigger an updated layout when dynamic type size changes. To avoid the edges of the transcript view, use `layoutMargins`. This value is only valid when `presentationStyle` is `MSMessagesAppPresentationStyleTranscript`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesapptranscriptpresentation/messagecornerradius)*