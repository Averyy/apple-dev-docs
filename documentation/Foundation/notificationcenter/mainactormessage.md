# NotificationCenter.MainActorMessage

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
protocol MainActorMessage : NotificationCenter.Message
```

## Relationships

### Inherits From
- [NotificationCenter.Message](notificationcenter/message.md)
### Conforming Types
- [Date.SystemClockDidChangeMessage](date/systemclockdidchangemessage.md)
- [FileManager.UbiquityIdentityDidChangeMessage](filemanager/ubiquityidentitydidchangemessage.md)
- [Locale.CurrentLocaleDidChangeMessage](locale/currentlocaledidchangemessage.md)
- [NSExtensionContext.DidBecomeActiveMessage](nsextensioncontext/didbecomeactivemessage.md)
- [NSExtensionContext.DidEnterBackgroundMessage](nsextensioncontext/didenterbackgroundmessage.md)
- [NSExtensionContext.WillEnterForegroundMessage](nsextensioncontext/willenterforegroundmessage.md)
- [NSExtensionContext.WillResignActiveMessage](nsextensioncontext/willresignactivemessage.md)
- [TimeZone.SystemTimeZoneDidChangeMessage](timezone/systemtimezonedidchangemessage.md)
- [UndoManager.CheckpointMessage](undomanager/checkpointmessage.md)
- [UndoManager.DidCloseUndoGroupMessage](undomanager/didcloseundogroupmessage.md)
- [UndoManager.DidOpenUndoGroupMessage](undomanager/didopenundogroupmessage.md)
- [UndoManager.DidRedoChangeMessage](undomanager/didredochangemessage.md)
- [UndoManager.DidUndoChangeMessage](undomanager/didundochangemessage.md)
- [UndoManager.WillCloseUndoGroupMessage](undomanager/willcloseundogroupmessage.md)
- [UndoManager.WillRedoChangeMessage](undomanager/willredochangemessage.md)
- [UndoManager.WillUndoChangeMessage](undomanager/willundochangemessage.md)
- [UserDefaults.SizeLimitExceededMessage](userdefaults/sizelimitexceededmessage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/mainactormessage)*