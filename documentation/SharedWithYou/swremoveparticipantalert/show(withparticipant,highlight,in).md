# show(withParticipant:highlight:in:)

**Framework**: Shared with You  
**Kind**: method  
**Role**: Type Method

**Availability**:
- macOS 13.0+

## Declaration

```swift
class func show(withParticipant participant: SWPerson, highlight: SWCollaborationHighlight, in window: NSWindow?)
```

```objc
+ (void) showAlertWithParticipant:(SWPerson *) participant highlight:(SWCollaborationHighlight *) highlight inWindow:(NSWindow *) window;
```

## Parameters

- `participant`: The `SWPerson` displayed in the alert.
- `highlight`: The `SWCollaborationHighlight` related to the request.
- `window`: The `NSWindow` to host the alert.

## See Also

### Requesting participant removal
- [class SWRemoveParticipantAlertController](../swremoveparticipantalertcontroller.md)
  The view controller for the remove-participant alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swremoveparticipantalert/show(withparticipant:highlight:in:))*