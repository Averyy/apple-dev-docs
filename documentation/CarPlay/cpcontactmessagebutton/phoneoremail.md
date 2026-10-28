# phoneOrEmail

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The contact’s phone number or email address.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var phoneOrEmail: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * phoneOrEmail;
```

## Discussion

When a user taps a contact message button, Siri launches the compose message flow and uses this property’s value as the recipient’s contact information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpcontactmessagebutton/phoneoremail)*