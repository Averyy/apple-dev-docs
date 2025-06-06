# actions

**Framework**: CarPlay  
**Kind**: property

The actions that the template displays for this contact.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var actions: [CPButton]? { get set }
```

#### Discussion

Assign an array of [`CPButton`](cpbutton.md) objects to this property to update the action buttons that the template displays for this contact. The template can display four buttons maximum. If the array contains more buttons, the template uses only the first four.

Contact actions are optional, and the default value is [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0).

## See Also

- [class CPContactCallButton](cpcontactcallbutton.md)
  A button for calling the contact.
- [class CPContactDirectionsButton](cpcontactdirectionsbutton.md)
  A button for getting directions to the contact’s location.
- [class CPContactMessageButton](cpcontactmessagebutton.md)
  A button that activates Siri and initiates the compose message flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpcontact/actions)*