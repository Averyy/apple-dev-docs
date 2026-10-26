# INStartCallCallRecordToCallBackUnsupportedReason

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

A reason why your app can’t use a record to call a person back.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
enum INStartCallCallRecordToCallBackUnsupportedReason
```

```c
enum INStartCallCallRecordToCallBackUnsupportedReason : NSInteger;
```

## Topics

### Reasons
- [INStartCallCallRecordToCallBackUnsupportedReason.noMatchingCall](./instartcallcallrecordtocallbackunsupportedreason/nomatchingcall.md)
  A reason indicating that no call record matches the intent’s parameter.
### Initializers
- [init?(rawValue: Int)](./instartcallcallrecordtocallbackunsupportedreason/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Starting a Call
- [protocol INStartCallIntentHandling](./instartcallintenthandling.md)
  An interface that handles requests to start audio and video calls.
- [class INStartCallIntent](./instartcallintent.md)
  A request to start an audio or video call with one or more users.
- [class INStartCallIntentResponse](./instartcallintentresponse.md)
  Your app’s response to a start call intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallcallrecordtocallbackunsupportedreason)*