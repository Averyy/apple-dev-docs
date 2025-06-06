# init(data:)

**Framework**: HomeKit  
**Kind**: init

Creates an ownership token from data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init?(data: Data)
```

#### Discussion

Obtain token data by negotiating with an accessory outside of HomeKit. You typically obtain token data for an accessory that you manufacture.

Token creation can fail if the data doesn’t represent a valid ownership token.

## Parameters

- `data`: Data to be sent to the accessory to prove ownership.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessoryownershiptoken/init(data:))*