# NotificationCenter.Message

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
protocol Message
```

## Topics

### Associated Types
- [associatedtype Subject](notificationcenter/message/subject.md)
### Type Properties
- [static var name: Notification.Name](notificationcenter/message/name.md)
### Type Methods
- [static func makeMessage(Notification) -> Self?](notificationcenter/message/makemessage(_:).md)
- [static func makeNotification(Self, object: Self.Subject?) -> Notification](notificationcenter/message/makenotification(_:object:).md)

## Relationships

### Inherited By
- [NotificationCenter.AsyncMessage](notificationcenter/asyncmessage.md)
- [NotificationCenter.MainActorMessage](notificationcenter/mainactormessage.md)
### Conforming Types
- [Bundle.DidLoadMessage](bundle/didloadmessage.md)
- [Calendar.CalendarDayChangedMessage](calendar/calendardaychangedmessage.md)
- [Date.SystemClockDidChangeMessage](date/systemclockdidchangemessage.md)
- [FileHandle.ConnectionAcceptedMessage](filehandle/connectionacceptedmessage.md)
- [FileHandle.DataAvailableMessage](filehandle/dataavailablemessage.md)
- [FileHandle.ReadCompletionMessage](filehandle/readcompletionmessage.md)
- [FileHandle.ReadToEndOfFileCompletionMessage](filehandle/readtoendoffilecompletionmessage.md)
- [FileManager.UbiquityIdentityDidChangeMessage](filemanager/ubiquityidentitydidchangemessage.md)
- [HTTPCookieStorage.CookiesChangedMessage](httpcookiestorage/cookieschangedmessage.md)
- [Locale.CurrentLocaleDidChangeMessage](locale/currentlocaledidchangemessage.md)
- [NSBundleResourceRequest.LowDiskSpaceMessage](nsbundleresourcerequest/lowdiskspacemessage.md)
- [NSExtensionContext.DidBecomeActiveMessage](nsextensioncontext/didbecomeactivemessage.md)
- [NSExtensionContext.DidEnterBackgroundMessage](nsextensioncontext/didenterbackgroundmessage.md)
- [NSExtensionContext.WillEnterForegroundMessage](nsextensioncontext/willenterforegroundmessage.md)
- [NSExtensionContext.WillResignActiveMessage](nsextensioncontext/willresignactivemessage.md)
- [NSMetadataQuery.DidFinishGatheringMessage](nsmetadataquery/didfinishgatheringmessage.md)
- [NSMetadataQuery.DidStartGatheringMessage](nsmetadataquery/didstartgatheringmessage.md)
- [Port.DidBecomeInvalidMessage](port/didbecomeinvalidmessage.md)
- [Process.DidTerminateMessage](process/didterminatemessage.md)
- [ProcessInfo.PowerStateDidChangeMessage](processinfo/powerstatedidchangemessage.md)
- [ProcessInfo.ThermalStateDidChangeMessage](processinfo/thermalstatedidchangemessage.md)
- [TimeZone.SystemTimeZoneDidChangeMessage](timezone/systemtimezonedidchangemessage.md)
- [UndoManager.CheckpointMessage](undomanager/checkpointmessage.md)
- [UndoManager.DidCloseUndoGroupMessage](undomanager/didcloseundogroupmessage.md)
- [UndoManager.DidOpenUndoGroupMessage](undomanager/didopenundogroupmessage.md)
- [UndoManager.DidRedoChangeMessage](undomanager/didredochangemessage.md)
- [UndoManager.DidUndoChangeMessage](undomanager/didundochangemessage.md)
- [UndoManager.WillCloseUndoGroupMessage](undomanager/willcloseundogroupmessage.md)
- [UndoManager.WillRedoChangeMessage](undomanager/willredochangemessage.md)
- [UndoManager.WillUndoChangeMessage](undomanager/willundochangemessage.md)
- [UserDefaults.DidChangeMessage](userdefaults/didchangemessage.md)
- [UserDefaults.SizeLimitExceededMessage](userdefaults/sizelimitexceededmessage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/message)*