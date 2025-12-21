# maximumImageSize

**Framework**: TelephonyMessagingKit  
**Kind**: property

The maximum size of an image, in bytes, allowed for a sent group message.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
var maximumImageSize: Measurement<UnitInformationStorage>?
```

#### Discussion

When this value isn’t set, the system uses the value of [`maximumMessageSize`](mmsservice/configuration/maximummessagesize.md) instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmsservice/configuration/maximumimagesize)*