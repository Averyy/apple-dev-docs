# callCapabilities

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The audio-video capabilities of the call.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var callCapabilities: INCallCapabilityOptions { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INCallCapabilityOptions callCapabilities;
```

*macOS*

```objc
@property (atomic, assign, readonly) INCallCapabilityOptions callCapabilities;
```

## Discussion

Use this property to limit your search to audio-only calls or video calls. You can specify both options.

## See Also

### Getting the Call History Details
- [var dateCreated: INDateComponentsRange?](./datecreated.md)
  The range of dates associated with the call records.
- [var callTypes: INCallRecordTypeOptions](./calltypes.md)
  The types of calls to search.
- [var callType: INCallRecordType](./calltype.md)
  The call type.
- [var unseen: Bool?](./unseen-9ua7o.md)
  A Boolean value that indicates whether the user has seen the call yet.
- [unseen](./unseen-1mohp.md)
  A Boolean value that indicates whether the user has seen the call yet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchcallhistoryintent/callcapabilities)*