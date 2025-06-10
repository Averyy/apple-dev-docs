# updateConversionValue(_:coarseConversionValue:lockPostback:)

**Framework**: AdAttributionKit  
**Kind**: method

Updates the conversion value with the provided fine and coarse conversion values, and optionally locks the postback, reducing the amount of time the system needs to deliver a signal.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst ?+

## Declaration

```swift
static func updateConversionValue(_ fineConversionValue: Int, coarseConversionValue: CoarseConversionValue, lockPostback: Bool) async throws
```

## Mentions

- [Receiving postbacks in multiple conversion windows](receiving-postbacks-in-multiple-conversion-windows.md)
- [Configuring an advertised app](configuring-an-advertised-app.md)
- [Understanding AdAttributionKit and SKAdNetwork interoperability](adattributionkit-skadnetwork-interoperability.md)
- [Receiving ad attributions and postbacks](receiving-ad-attributions-and-postbacks.md)
- [Identifying the parameters in a postback](identifying-the-parameters-in-a-postback.md)

## Parameters

- `fineConversionValue`: An integer that defines the fine conversion value.
- `coarseConversionValue`: One of the   values.
- `lockPostback`: A Boolean value that indicates whether the system can lock the postback, reducing system time to deliver a signal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/adattributionkit/postback/updateconversionvalue(_:coarseconversionvalue:lockpostback:))*