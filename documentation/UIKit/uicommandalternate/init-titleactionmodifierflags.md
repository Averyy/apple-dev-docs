# init(title:action:modifierFlags:)

**Framework**: UIKit  
**Kind**: init

Creates a command alternative with the specified title, action, and modifier flags.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(title: String, action: Selector, modifierFlags: UIKeyModifierFlags)
```

#### Return Value

A command alternative object.

## Parameters

- `title`: The command alternative’s title.
- `action`: The action to take after a person selects the alternative command.
- `modifierFlags`: The bit mask of modifier keys that a person must press. You can use this parameter to specify which modifier keys (Command, Option, and so on) a person must also press. You may specify more than one modifier key. For a list of possible values, see  .

## See Also

- [init?(coder: NSCoder)](uicommandalternate/init(coder:).md)
  Creates a command alternative from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicommandalternate/init(title:action:modifierflags:))*