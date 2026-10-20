# maximumTextMessageSize

**Framework**: TelephonyMessagingKit  
**Kind**: property  
**Role**: Instance Property

The maximum size of a text chat message that a person can enter in a 1-to-1 chat or group chat session.

**Availability**:
- iOS 26.0+

## Declaration

```swift
var maximumTextMessageSize: Measurement<UnitInformationStorage>? { get }
```

#### Discussion

This value is represented as a Foundation [`Measurement`](../../../Foundation/measurement.md) that uses the [`UnitInformationStorage`](../../../Foundation/unitinformationstorage.md) unit type. If the messaging service is disabled, the value is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/configuration/maximumtextmessagesize)*