# provider(_:didDeactivate:)

**Framework**: CallKit  
**Kind**: method  
**Role**: Instance Method

Called when the provider’s audio session is deactivated.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
optional func provider(_ provider: CXProvider, didDeactivate audioSession: AVAudioSession)
```

```objc
- (void) provider:(CXProvider *) provider didDeactivateAudioSession:(AVAudioSession *) audioSession;
```

## Parameters

- `provider`: The telephony provider.
- `audioSession`: The audio session that was deactivated.

## See Also

### Handling Changes to Audio Session Activation State
- [func provider(CXProvider, didActivate: AVAudioSession)](./provider%28_,didactivate%29.md)
  Called when the provider’s audio session is activated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxproviderdelegate/provider(_:diddeactivate:))*