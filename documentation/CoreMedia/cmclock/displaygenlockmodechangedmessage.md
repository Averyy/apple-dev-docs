# CMClock.DisplayGenlockModeChangedMessage

**Framework**: Core Media  
**Kind**: struct  
**Role**: Structure

A message delivered when the display mode changes from genlock to non-genlock or vice versa.

**Availability**:
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
struct DisplayGenlockModeChangedMessage
```

## Topics

### Instance Properties
- [let isAnyDisplaySynchronizedToLockedGenlockSignal: Bool](./displaygenlockmodechangedmessage/isanydisplaysynchronizedtolockedgenlocksignal.md)
  Indicates whether at least one display is synchronized to a locked external genlock signal.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../../Foundation/notificationcenter/mainactormessage.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmclock/displaygenlockmodechangedmessage)*