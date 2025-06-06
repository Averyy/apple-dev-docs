# provider(_:perform:)

**Framework**: CallKit  
**Kind**: method

Called when the provider performs the specified set held call action.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
optional func provider(_ provider: CXProvider, perform action: CXSetHeldCallAction)
```

## Parameters

- `provider`: The telephony provider.
- `action`: The set held call action.

## See Also

- [func provider(CXProvider, perform: CXStartCallAction)](cxproviderdelegate/provider(_:perform:)-2lem5.md)
  Called when the provider performs the specified start call action.
- [func provider(CXProvider, perform: CXAnswerCallAction)](cxproviderdelegate/provider(_:perform:)-h4in.md)
  Called when the provider performs the specified answer call action.
- [func provider(CXProvider, perform: CXEndCallAction)](cxproviderdelegate/provider(_:perform:)-9a0m.md)
  Called when the provider performs the specified end call action.
- [func provider(CXProvider, perform: CXSetMutedCallAction)](cxproviderdelegate/provider(_:perform:)-4u3yu.md)
  Called when the provider performs the specified set muted call action.
- [func provider(CXProvider, perform: CXSetGroupCallAction)](cxproviderdelegate/provider(_:perform:)-9masw.md)
  Called when the provider performs the specified set group call action.
- [func provider(CXProvider, perform: CXPlayDTMFCallAction)](cxproviderdelegate/provider(_:perform:)-4htxt.md)
  Called when the provider performs the specified play DTMF (dual tone multifrequency) call action.
- [func provider(CXProvider, timedOutPerforming: CXAction)](cxproviderdelegate/provider(_:timedoutperforming:).md)
  Called when the provider performs the specified action times out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxproviderdelegate/provider(_:perform:)-947b1)*