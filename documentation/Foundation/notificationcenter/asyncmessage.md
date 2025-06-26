# NotificationCenter.AsyncMessage

**Framework**: Foundation  
**Kind**: protocol

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
protocol AsyncMessage : Sendable
```

## Topics

### Associated Types
- [associatedtype Subject](notificationcenter/asyncmessage/subject.md)
### Type Properties
- [static var name: Notification.Name](notificationcenter/asyncmessage/name.md)
### Type Methods
- [static func makeMessage(Notification) -> Self?](notificationcenter/asyncmessage/makemessage(_:).md)
- [static func makeNotification(Self, object: Self.Subject?) -> Notification](notificationcenter/asyncmessage/makenotification(_:object:).md)

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [Bundle.DidLoadMessage](bundle/didloadmessage.md)
- [Calendar.CalendarDayChangedMessage](calendar/calendardaychangedmessage.md)
- [FileHandle.ConnectionAcceptedMessage](filehandle/connectionacceptedmessage.md)
- [FileHandle.DataAvailableMessage](filehandle/dataavailablemessage.md)
- [FileHandle.ReadCompletionMessage](filehandle/readcompletionmessage.md)
- [FileHandle.ReadToEndOfFileCompletionMessage](filehandle/readtoendoffilecompletionmessage.md)
- [HTTPCookieStorage.CookiesChangedMessage](httpcookiestorage/cookieschangedmessage.md)
- [NSBundleResourceRequest.LowDiskSpaceMessage](nsbundleresourcerequest/lowdiskspacemessage.md)
- [NSMetadataQuery.DidFinishGatheringMessage](nsmetadataquery/didfinishgatheringmessage.md)
- [NSMetadataQuery.DidStartGatheringMessage](nsmetadataquery/didstartgatheringmessage.md)
- [Port.DidBecomeInvalidMessage](port/didbecomeinvalidmessage.md)
- [Process.DidTerminateMessage](process/didterminatemessage.md)
- [ProcessInfo.PowerStateDidChangeMessage](processinfo/powerstatedidchangemessage.md)
- [ProcessInfo.ThermalStateDidChangeMessage](processinfo/thermalstatedidchangemessage.md)
- [UserDefaults.DidChangeMessage](userdefaults/didchangemessage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/asyncmessage)*