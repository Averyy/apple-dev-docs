# RCSService.Business.SuggestedAction.Action

**Framework**: TelephonyMessagingKit  
**Kind**: enum  
**Role**: Enumeration

Enumeration specifying the type of action contained.

**Availability**:
- iOS 26.0+

## Declaration

```swift
enum Action
```

## Topics

### Handling URL and phone-dialing actions
- [RCSService.Business.SuggestedAction.Action.openURL(_:)](./action-swift.enum/openurl%28_%29.md)
  URL action.
- [RCSService.Business.OpenURLAction](../openurlaction.md)
  Suggested action to open a URL.
- [case dialPhoneNumber(RCSService.Business.DialPhoneNumberAction)](./action-swift.enum/dialphonenumber%28_%29.md)
  Dialer phone number.
- [RCSService.Business.DialPhoneNumberAction](../dialphonenumberaction.md)
  Suggested action to dial a phone number.
### Handling location actions
- [RCSService.Business.SuggestedAction.Action.showLocation(_:)](./action-swift.enum/showlocation%28_%29.md)
  Show location action.
- [RCSService.Business.ShowLocationAction](../showlocationaction.md)
  Shows a location on a map.
- [RCSService.Business.SuggestedAction.Action.sendLocation](./action-swift.enum/sendlocation.md)
  Send location from device to business.
### Handling calendar event actions
- [case createCalendarEvent(RCSService.Business.CreateCalendarEventAction)](./action-swift.enum/createcalendarevent%28_%29.md)
  Calendar action.
- [RCSService.Business.CreateCalendarEventAction](../createcalendareventaction.md)
  Structure representing an action to create a calendar event.
### Handling composition actions
- [RCSService.Business.SuggestedAction.Action.composeText(_:)](./action-swift.enum/composetext%28_%29.md)
  Compose text action.
- [RCSService.Business.ComposeTextAction](../composetextaction.md)
  Compose a draft text message.
- [case composeRecording(RCSService.Business.ComposeRecordingAction)](./action-swift.enum/composerecording%28_%29.md)
  Compose recording action.
- [RCSService.Business.ComposeRecordingAction](../composerecordingaction.md)
  Compose a draft message with a media recording.
### Handling local behavior actions
- [RCSService.Business.SuggestedAction.Action.sendDeviceSpecifics](./action-swift.enum/senddevicespecifics.md)
  Request specifics about the user’s device.
- [RCSService.Business.SuggestedAction.Action.enableDisplayedNotifications](./action-swift.enum/enabledisplayednotifications.md)
  Ask the user to enable sending displayed notifications.

## Relationships

### Conforms To
- [Decodable](../../../../Swift/decodable.md)
- [Encodable](../../../../Swift/encodable.md)
- [Equatable](../../../../Swift/equatable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)

## See Also

### Accessing suggested action properties
- [let displayText: String](./displaytext.md)
  Display text for action.
- [let action: RCSService.Business.SuggestedAction.Action](./action-swift.property.md)
  The  suggested action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/suggestedaction/action-swift.enum)*