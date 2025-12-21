# canAddSecureElementPass(configuration:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Returns a Boolean value that indicates whether PassKit can create a Secure Element pass using the specified configuration.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func canAddSecureElementPass(configuration: PKAddSecureElementPassConfiguration) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if PassKit validates the configuration; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `configuration`: The configuration to validate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddsecureelementpassviewcontroller/canaddsecureelementpass(configuration:))*