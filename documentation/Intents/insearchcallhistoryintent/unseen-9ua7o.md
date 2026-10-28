# unseen

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the user has seen the call yet.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 11.0+ - Deprecated in 15.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
@nonobjc
final var unseen: Bool? { get }
```

## Discussion

## See Also

### Getting the Call History Details
- [var dateCreated: INDateComponentsRange?](./datecreated.md)
  The range of dates associated with the call records.
- [var callTypes: INCallRecordTypeOptions](./calltypes.md)
  The types of calls to search.
- [var callType: INCallRecordType](./calltype.md)
  The call type.
- [var callCapabilities: INCallCapabilityOptions](./callcapabilities.md)
  The audio-video capabilities of the call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchcallhistoryintent/unseen-9ua7o)*