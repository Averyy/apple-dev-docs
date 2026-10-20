# provider(_:perform:)

**Framework**: CallKit  
**Kind**: method  
**Role**: Instance Method

Called when the provider performs the specified set translation action.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+

## Declaration

```swift
optional func provider(_ provider: CXProvider, perform action: CXSetTranslatingCallAction)
```

```objc
- (void) provider:(CXProvider *) provider performSetTranslatingCallAction:(CXSetTranslatingCallAction *) action;
```

## Parameters

- `provider`: The telephony provider.
- `action`: The set translation action.

## See Also

### Handling Call Actions
- [func provider(CXProvider, perform: CXStartCallAction)](./provider%28_,perform%29-2lem5.md)
  Called when the provider performs the specified start call action.
- [func provider(CXProvider, perform: CXAnswerCallAction)](./provider%28_,perform%29-h4in.md)
  Called when the provider performs the specified answer call action.
- [func provider(CXProvider, perform: CXEndCallAction)](./provider%28_,perform%29-9a0m.md)
  Called when the provider performs the specified end call action.
- [func provider(CXProvider, perform: CXSetHeldCallAction)](./provider%28_,perform%29-947b1.md)
  Called when the provider performs the specified set held call action.
- [func provider(CXProvider, perform: CXSetMutedCallAction)](./provider%28_,perform%29-4u3yu.md)
  Called when the provider performs the specified set muted call action.
- [func provider(CXProvider, perform: CXSetGroupCallAction)](./provider%28_,perform%29-9masw.md)
  Called when the provider performs the specified set group call action.
- [func provider(CXProvider, perform: CXPlayDTMFCallAction)](./provider%28_,perform%29-4htxt.md)
  Called when the provider performs the specified play DTMF (dual tone multifrequency) call action.
- [func provider(CXProvider, timedOutPerforming: CXAction)](./provider%28_,timedoutperforming%29.md)
  Called when the provider performs the specified action times out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxproviderdelegate/provider(_:perform:)-43atg)*