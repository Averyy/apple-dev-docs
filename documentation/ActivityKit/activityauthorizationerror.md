# ActivityAuthorizationError

**Framework**: ActivityKit  
**Kind**: enum

An error that indicates why the request to start a Live Activity failed.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
enum ActivityAuthorizationError
```

## Topics

### Error codes
- [ActivityAuthorizationError.attributesTooLarge](activityauthorizationerror/attributestoolarge.md)
  The provided Live Activity attributes exceeded the maximum size of 4KB.
- [ActivityAuthorizationError.denied](activityauthorizationerror/denied.md)
  A person deactivated Live Activities in Settings.
- [ActivityAuthorizationError.globalMaximumExceeded](activityauthorizationerror/globalmaximumexceeded.md)
  The device reached the maximum number of ongoing Live Activities.
- [ActivityAuthorizationError.malformedActivityIdentifier](activityauthorizationerror/malformedactivityidentifier.md)
  The provided activity identifier is malformed.
- [ActivityAuthorizationError.missingProcessIdentifier](activityauthorizationerror/missingprocessidentifier.md)
  The process that tried to start the Live Activity is missing a process identifier.
- [ActivityAuthorizationError.persistenceFailure](activityauthorizationerror/persistencefailure.md)
  The system couldn’t persist the Live Activity.
- [ActivityAuthorizationError.reconnectNotPermitted](activityauthorizationerror/reconnectnotpermitted.md)
  The process that tried to recreate the Live Activity is not the process that originally created the Live Activity.
- [ActivityAuthorizationError.targetMaximumExceeded](activityauthorizationerror/targetmaximumexceeded.md)
  The app has already started the maximum number of concurrent Live Activities.
- [ActivityAuthorizationError.unentitled](activityauthorizationerror/unentitled.md)
  The app doesn’t have the required entitlement to start a Live Activity.
- [ActivityAuthorizationError.unsupported](activityauthorizationerror/unsupported.md)
  The device doesn’t support Live Activities.
- [ActivityAuthorizationError.unsupportedTarget](activityauthorizationerror/unsupportedtarget.md)
  The app doesn’t have the required entitlement to start a Live Activities.
- [ActivityAuthorizationError.visibility](activityauthorizationerror/visibility.md)
  The app tried to start the Live Activity while it was in the background.
### Getting error information
- [var failureReason: String?](activityauthorizationerror/failurereason.md)
  A string that describes the error that occurred.
- [var recoverySuggestion: String?](activityauthorizationerror/recoverysuggestion.md)
  A localized message that describes how to recover from the error.
### Protocol confirmation
- [var errorCode: Int](activityauthorizationerror/errorcode.md)
  An integer value that represents the error code.
- [static var errorDomain: String](activityauthorizationerror/errordomain.md)
  The domain for errors that can happen when starting a Live Activity.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static func request(attributes: Attributes, content: ActivityContent<Activity<Attributes>.ContentState>, pushType: PushType?) throws -> Activity<Attributes>](activity/request(attributes:content:pushtype:).md)
  Requests and starts a standard Live Activity.
- [static func request(attributes: Attributes, content: ActivityContent<Activity<Attributes>.ContentState>, pushType: PushType?, style: ActivityStyle) throws -> Activity<Attributes>](activity/request(attributes:content:pushtype:style:).md)
  Requests and starts a Live Activity.
- [static func request(attributes: Attributes, content: ActivityContent<Activity<Attributes>.ContentState>, pushType: PushType?, style: ActivityStyle, alertConfiguration: AlertConfiguration, start: Date) throws -> Activity<Attributes>](activity/request(attributes:content:pushtype:style:alertconfiguration:start:).md)
  Requests and schedules a Live Activity for a specific date.
- [static func request(attributes: Attributes, content: ActivityContent<Activity<Attributes>.ContentState>, pushType: PushType?, style: ActivityStyle, alertConfiguration: AlertConfiguration, startDate: Date) throws -> Activity<Attributes>](activity/request(attributes:content:pushtype:style:alertconfiguration:startdate:).md)
- [let attributes: Attributes](activity/attributes.md)
  A set of attributes that describe a Live Activity and its content.
- [protocol ActivityAttributes](activityattributes.md)
  The protocol you implement to describe the content of a Live Activity.
- [enum ActivityStyle](activitystyle.md)
- [var content: ActivityContent<Activity<Attributes>.ContentState>](activity/content.md)
  The dynamic content of a Live Activity.
- [struct ActivityContent](activitycontent.md)
  A structure that describes the state and configuration of a Live Activity.
- [typealias ContentState](activity/contentstate-swift.typealias.md)
  The type alias for the structure that describes the dynamic content of a Live Activity.
- [struct PushType](pushtype.md)
  The structure that offers constants you use to configure a Live Activity to receive updates through ActivityKit push notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activityauthorizationerror)*