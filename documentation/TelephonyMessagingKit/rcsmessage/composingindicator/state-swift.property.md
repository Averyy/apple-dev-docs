# state

**Framework**: TelephonyMessagingKit  
**Kind**: property  
**Role**: Instance Property

The state of the composer.

**Availability**:
- iOS 26.0+

## Declaration

```swift
var state: RCSMessage.ComposingIndicator.State
```

## See Also

### Accessing composing indicator properties
- [RCSMessage.ComposingIndicator.State](./state-swift.enum.md)
  An enumeration that represents the state of the indicator.
- [var lastActive: Date?](./lastactive.md)
  The time of last activity.
- [var contentType: UTType?](./contenttype.md)
  The type of message being composed.
- [struct UTType](../../../UniformTypeIdentifiers/uttype-swift.struct.md)
  A structure that represents a type of data to load, send, or receive.
- [var refreshInterval: Duration?](./refreshinterval.md)
  The time interval after which the receiver can expect an update from the composer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/composingindicator/state-swift.property)*