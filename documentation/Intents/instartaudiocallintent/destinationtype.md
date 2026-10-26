# destinationType

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The type of call to place.

**Availability**:
- iOS 11.0+ - Deprecated in 13.0
- iPadOS 11.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 6.0

## Declaration

```swift
var destinationType: INCallDestinationType { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INCallDestinationType destinationType;
```

*macOS*

```objc
@property (atomic, assign, readonly) INCallDestinationType destinationType;
```

#### Discussion

Use this property to differentiate regular calls from specialized types of calls. For example, when the value of this property is [`voicemailDestination`](../incalldestinationtype/voicemaildestination.md), the user is attempting to connect to their voicemail messages.

## See Also

### Getting the Call Attributes
- [var contacts: [INPerson]?](./contacts.md)
  The users to call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartaudiocallintent/destinationtype)*