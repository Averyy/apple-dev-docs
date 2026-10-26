# emergencyDestination

**Framework**: Intents  
**Kind**: property  
**Role**: Type Property

A call routed to an emergency number.

**Availability**:
- iOS 11.0+ - Deprecated in 11.0
- iPadOS 11.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.13+ - Deprecated in 10.13
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 4.0

> **Deprecated**: Use INCallDestinationTypeEmergency instead

## Declaration

```swift
static var emergencyDestination: INCallDestinationType { get }
```

```c
INCallDestinationTypeEmergencyDestination
```

## See Also

### Constants
- [INCallDestinationType.unknown](./unknown.md)
  An unknown call destination.
- [INCallDestinationType.normal](./normal.md)
  A call routed to its expected destination.
- [INCallDestinationType.emergency](./emergency.md)
  A call routed to an emergency number.
- [INCallDestinationType.voicemail](./voicemail.md)
  A call routed to the user’s voicemail.
- [INCallDestinationType.redial](./redial.md)
  A call that was the result of redialing a previous call.
- [INCallDestinationType.callBack](./callback.md)
  A call that was the result of a call back.
- [static var normalDestination: INCallDestinationType](./normaldestination.md)
  A call routed to its expected destination.
- [static var voicemailDestination: INCallDestinationType](./voicemaildestination.md)
  A call routed to the user’s voicemail.
- [static var redialDestination: INCallDestinationType](./redialdestination.md)
  A call that was the result of redialing a previous call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incalldestinationtype/emergencydestination)*