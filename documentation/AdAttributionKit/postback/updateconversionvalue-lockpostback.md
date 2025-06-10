# updateConversionValue(_:lockPostback:)

**Framework**: AdAttributionKit  
**Kind**: method

Updates a conversion value with the provided fine and coarse conversion values, and optionally locks the postback, reducing the system time to deliver a signal.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst ?+

## Declaration

```swift
static func updateConversionValue(_ fineConversionValue: Int, lockPostback: Bool) async throws
```

## Mentions

- [Understanding AdAttributionKit and SKAdNetwork interoperability](adattributionkit-skadnetwork-interoperability.md)
- [Receiving postbacks in multiple conversion windows](receiving-postbacks-in-multiple-conversion-windows.md)
- [Configuring an advertised app](configuring-an-advertised-app.md)
- [Identifying the parameters in a postback](identifying-the-parameters-in-a-postback.md)

## Parameters

- `fineConversionValue`: An integer the defines the fine conversion value.
- `lockPostback`: A Boolean value that indicates whether the system can lock the postback, reducing the system time to deliver a signal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/adattributionkit/postback/updateconversionvalue(_:lockpostback:))*