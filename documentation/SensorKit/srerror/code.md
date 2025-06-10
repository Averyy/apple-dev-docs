# SRError.Code

**Framework**: SensorKit  
**Kind**: enum

The kinds of problems that stop a recording or a fetch.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum Code
```

## Topics

### Errors
- [SRError.Code.promptDeclined](srerror/code/promptdeclined.md)
  Occurs when the user cancels the sensor approval workflow.
- [SRError.Code.dataInaccessible](srerror/code/datainaccessible.md)
  Occurs when the app can’t access the sensor’s data.
- [SRError.Code.fetchRequestInvalid](srerror/code/fetchrequestinvalid.md)
  Occurs when the app misconfigures a fetch request.
- [SRError.Code.invalidEntitlement](srerror/code/invalidentitlement.md)
  Occurs when the app lacks the required entitlement.
- [SRError.Code.noAuthorization](srerror/code/noauthorization.md)
  Occurs when the user declines sensor access in the Settings app.
### Creating an error
- [init?(rawValue: Int)](srerror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let SRErrorDomain: String](srerrordomain.md)
  An error domain that’s unique to the framework.
- [struct SRError](srerror.md)
  An error that SensorKit reports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srerror/code)*