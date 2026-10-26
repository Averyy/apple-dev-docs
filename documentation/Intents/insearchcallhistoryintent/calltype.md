# callType

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The call type.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 4.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var callType: INCallRecordType { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INCallRecordType callType;
```

*macOS*

```objc
@property (atomic, assign, readonly) INCallRecordType callType;
```

#### Discussion

Use this property to limit your search to the specified type of calls. If the value of this property is [`INCallRecordType.unknown`](../incallrecordtype/unknown.md), search all call types.

## See Also

### Getting the Call History Details
- [var dateCreated: INDateComponentsRange?](./datecreated.md)
  The range of dates associated with the call records.
- [var callTypes: INCallRecordTypeOptions](./calltypes.md)
  The types of calls to search.
- [var callCapabilities: INCallCapabilityOptions](./callcapabilities.md)
  The audio-video capabilities of the call.
- [var unseen: Bool?](./unseen-9ua7o.md)
  A Boolean value that indicates whether the user has seen the call yet.
- [unseen](./unseen-1mohp.md)
  A Boolean value that indicates whether the user has seen the call yet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchcallhistoryintent/calltype)*