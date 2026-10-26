# init(participants:callTypes:callCapability:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a filtered call record with the details about a call.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(participants: [INPerson]?, callTypes: INCallRecordTypeOptions = [], callCapability: INCallCapability)
```

```objc
- (instancetype) initWithParticipants:(NSArray<INPerson *> *) participants callTypes:(INCallRecordTypeOptions) callTypes callCapability:(INCallCapability) callCapability;
```

#### Return Value

An initialized [`INCallRecordFilter`](../incallrecordfilter.md) object or `nil` if the object could not be initialized.

## Parameters

- `participants`: The recipient of the user’s call request.
- `callTypes`: The various call options that the user can request.
- `callCapability`: An indicator of whether the call supports audio or video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallrecordfilter/init(participants:calltypes:callcapability:))*