# dateCreated

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The range of dates associated with the call records.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
@NSCopying
var dateCreated: INDateComponentsRange? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INDateComponentsRange * dateCreated;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INDateComponentsRange * dateCreated;
```

## Discussion

Use this property to limit your search to calls that occurred within the specified range of dates. Include the start and end dates in your search.

## See Also

### Getting the Call History Details
- [var callTypes: INCallRecordTypeOptions](./calltypes.md)
  The types of calls to search.
- [var callType: INCallRecordType](./calltype.md)
  The call type.
- [var callCapabilities: INCallCapabilityOptions](./callcapabilities.md)
  The audio-video capabilities of the call.
- [var unseen: Bool?](./unseen-9ua7o.md)
  A Boolean value that indicates whether the user has seen the call yet.
- [unseen](./unseen-1mohp.md)
  A Boolean value that indicates whether the user has seen the call yet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchcallhistoryintent/datecreated)*