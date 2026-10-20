# providerDidReset(_:)

**Framework**: CallKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Called when the provider is reset.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func providerDidReset(_ provider: CXProvider)
```

```objc
- (void) providerDidReset:(CXProvider *) provider;
```

## Parameters

- `provider`: The telephony provider.

## See Also

### Handling Provider Events
- [func providerDidBegin(CXProvider)](./providerdidbegin%28_%29.md)
  Called when the provider begins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxproviderdelegate/providerdidreset(_:))*