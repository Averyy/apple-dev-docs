# provider(_:didActivate:)

**Framework**: CallKit  
**Kind**: method

Called when the provider’s audio session is activated.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
optional func provider(_ provider: CXProvider, didActivate audioSession: AVAudioSession)
```

## Parameters

- `provider`: The telephony provider.
- `audioSession`: The audio session that was activated.

## See Also

- [func provider(CXProvider, didDeactivate: AVAudioSession)](cxproviderdelegate/provider(_:diddeactivate:).md)
  Called when the provider’s audio session is deactivated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxproviderdelegate/provider(_:didactivate:))*