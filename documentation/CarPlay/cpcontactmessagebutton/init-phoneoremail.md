# init(phoneOrEmail:)

**Framework**: CarPlay  
**Kind**: init

Creates a contact message button with the provided contact information.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
init(phoneOrEmail: String)
```

#### Return Value

A new contact message button.

#### Discussion

The button displays a system image that communicates its function. CarPlay never displays the contact information you provide. Tapping the button activates Siri and launches the compose message flow using the phone number or email address you provide.

## Parameters

- `phoneOrEmail`: A valid phone number or email address to use in Siri’s compose message flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpcontactmessagebutton/init(phoneoremail:))*