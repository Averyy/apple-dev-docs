# callTypes

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The types of calls to search.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var callTypes: INCallRecordTypeOptions { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INCallRecordTypeOptions callTypes;
```

*macOS*

```objc
@property (atomic, assign, readonly) INCallRecordTypeOptions callTypes;
```

## See Also

### Getting the Call History Details
- [var dateCreated: INDateComponentsRange?](./datecreated.md)
  The range of dates associated with the call records.
- [var callType: INCallRecordType](./calltype.md)
  The call type.
- [var callCapabilities: INCallCapabilityOptions](./callcapabilities.md)
  The audio-video capabilities of the call.
- [var unseen: Bool?](./unseen-9ua7o.md)
  A Boolean value that indicates whether the user has seen the call yet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchcallhistoryintent/calltypes)*