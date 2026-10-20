# SRError.Code

**Framework**: SensorKit  
**Kind**: enum  
**Role**: Enumeration

The kinds of problems that stop a recording or a fetch.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum Code
```

```c
enum SRErrorCode : NSInteger;
```

## Topics

### Errors
- [SRError.Code.promptDeclined](./code/promptdeclined.md)
  Occurs when the user cancels the sensor approval workflow.
- [SRError.Code.dataInaccessible](./code/datainaccessible.md)
  Occurs when the app can’t access the sensor’s data.
- [SRError.Code.fetchRequestInvalid](./code/fetchrequestinvalid.md)
  Occurs when the app misconfigures a fetch request.
- [SRError.Code.invalidEntitlement](./code/invalidentitlement.md)
  Occurs when the app lacks the required entitlement.
- [SRError.Code.noAuthorization](./code/noauthorization.md)
  Occurs when the user declines sensor access in the Settings app.
### Creating an error
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Interpreting Errors
- [let SRErrorDomain: String](../srerrordomain.md)
  An error domain that’s unique to the framework.
- [struct SRError](../srerror.md)
  An error that SensorKit reports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srerror/code)*