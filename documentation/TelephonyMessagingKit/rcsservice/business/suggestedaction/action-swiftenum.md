# RCSService.Business.SuggestedAction.Action

**Framework**: TelephonyMessagingKit  
**Kind**: enum

Enumeration specifying the type of action contained.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
enum Action
```

## Topics

### Handling URL and phone-dialing actions
- [RCSService.Business.SuggestedAction.Action.openURL(_:)](rcsservice/business/suggestedaction/action-swift.enum/openurl(_:).md)
  URL action.
- [RCSService.Business.OpenURLAction](rcsservice/business/openurlaction.md)
  Suggested action to open a URL.
- [case dialPhoneNumber(RCSService.Business.DialPhoneNumberAction)](rcsservice/business/suggestedaction/action-swift.enum/dialphonenumber(_:).md)
  Dialer phone number.
- [RCSService.Business.DialPhoneNumberAction](rcsservice/business/dialphonenumberaction.md)
  Suggested action to dial a phone number.
### Handling location actions
- [RCSService.Business.SuggestedAction.Action.showLocation(_:)](rcsservice/business/suggestedaction/action-swift.enum/showlocation(_:).md)
  Show location action.
- [RCSService.Business.ShowLocationAction](rcsservice/business/showlocationaction.md)
  Shows a location on a map.
- [RCSService.Business.SuggestedAction.Action.sendLocation](rcsservice/business/suggestedaction/action-swift.enum/sendlocation.md)
  Send location from device to business.
### Handling calendar event actions
- [case createCalendarEvent(RCSService.Business.CreateCalendarEventAction)](rcsservice/business/suggestedaction/action-swift.enum/createcalendarevent(_:).md)
  Calendar action.
- [RCSService.Business.CreateCalendarEventAction](rcsservice/business/createcalendareventaction.md)
  Structure representing an action to create a calendar event.
### Handling composition actions
- [RCSService.Business.SuggestedAction.Action.composeText(_:)](rcsservice/business/suggestedaction/action-swift.enum/composetext(_:).md)
  Compose text action.
- [RCSService.Business.ComposeTextAction](rcsservice/business/composetextaction.md)
  Compose a draft text message.
- [case composeRecording(RCSService.Business.ComposeRecordingAction)](rcsservice/business/suggestedaction/action-swift.enum/composerecording(_:).md)
  Compose recording action.
- [RCSService.Business.ComposeRecordingAction](rcsservice/business/composerecordingaction.md)
  Compose a draft message with a media recording.
### Handling local behavior actions
- [RCSService.Business.SuggestedAction.Action.sendDeviceSpecifics](rcsservice/business/suggestedaction/action-swift.enum/senddevicespecifics.md)
  Request specifics about the user’s device.
- [RCSService.Business.SuggestedAction.Action.enableDisplayedNotifications](rcsservice/business/suggestedaction/action-swift.enum/enabledisplayednotifications.md)
  Ask the user to enable sending displayed notifications.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let displayText: String](rcsservice/business/suggestedaction/displaytext.md)
  Display text for action.
- [let action: RCSService.Business.SuggestedAction.Action](rcsservice/business/suggestedaction/action-swift.property.md)
  The  suggested action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/suggestedaction/action-swift.enum)*