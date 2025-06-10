# refreshInterval

**Framework**: TelephonyMessagingKit  
**Kind**: property

The time interval after which the receiver can expect an update from the composer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
let refreshInterval: Duration?
```

## See Also

- [let state: RCSMessage.ComposingIndicator.State](rcsmessage/composingindicator/state-swift.property.md)
  The state of the composer.
- [RCSMessage.ComposingIndicator.State](rcsmessage/composingindicator/state-swift.enum.md)
  An enumeration that represents the state of the indicator.
- [let lastActive: Date?](rcsmessage/composingindicator/lastactive.md)
  The time of last activity.
- [let contentType: UTType?](rcsmessage/composingindicator/contenttype.md)
  The type of message being composed.
- [struct UTType](../UniformTypeIdentifiers/UTType-swift.struct.md)
  A structure that represents a type of data to load, send, or receive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/composingindicator/refreshinterval)*