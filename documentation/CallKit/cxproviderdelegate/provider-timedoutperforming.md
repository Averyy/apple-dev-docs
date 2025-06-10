# provider(_:timedOutPerforming:)

**Framework**: CallKit  
**Kind**: method

Called when the provider performs the specified action times out.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
optional func provider(_ provider: CXProvider, timedOutPerforming action: CXAction)
```

#### Discussion

Depending on the action, a timeout may also force the call to end.

An action that has already timed out should not be fulfilled or failed by the provider delegate.

## Parameters

- `provider`: The telephony provider.
- `action`: The action that timed out.

## See Also

- [func provider(CXProvider, perform: CXStartCallAction)](cxproviderdelegate/provider(_:perform:)-2lem5.md)
  Called when the provider performs the specified start call action.
- [func provider(CXProvider, perform: CXAnswerCallAction)](cxproviderdelegate/provider(_:perform:)-h4in.md)
  Called when the provider performs the specified answer call action.
- [func provider(CXProvider, perform: CXEndCallAction)](cxproviderdelegate/provider(_:perform:)-9a0m.md)
  Called when the provider performs the specified end call action.
- [func provider(CXProvider, perform: CXSetHeldCallAction)](cxproviderdelegate/provider(_:perform:)-947b1.md)
  Called when the provider performs the specified set held call action.
- [func provider(CXProvider, perform: CXSetMutedCallAction)](cxproviderdelegate/provider(_:perform:)-4u3yu.md)
  Called when the provider performs the specified set muted call action.
- [func provider(CXProvider, perform: CXSetGroupCallAction)](cxproviderdelegate/provider(_:perform:)-9masw.md)
  Called when the provider performs the specified set group call action.
- [func provider(CXProvider, perform: CXPlayDTMFCallAction)](cxproviderdelegate/provider(_:perform:)-4htxt.md)
  Called when the provider performs the specified play DTMF (dual tone multifrequency) call action.
- [func provider(CXProvider, perform: CXSetTranslatingCallAction)](cxproviderdelegate/provider(_:perform:)-43atg.md)
  Called when the provider performs the specified set translation action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxproviderdelegate/provider(_:timedoutperforming:))*