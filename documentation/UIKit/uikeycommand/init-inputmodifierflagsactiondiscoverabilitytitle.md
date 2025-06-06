# init(input:modifierFlags:action:discoverabilityTitle:)

**Framework**: UIKit  
**Kind**: init

Creates a key command object that matches the specified input and has a title.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+

## Declaration

```swift
@MainActor
convenience init(input: String, modifierFlags: UIKeyModifierFlags, action: Selector, discoverabilityTitle: String)
```

#### Return Value

The initialized key command object.

#### Discussion

After creating a key command object, you can add it to a view controller using the [`addKeyCommand(_:)`](uiviewcontroller/addkeycommand(_:).md) method of the view controller. You can also override any responder class and return the key command directly from the responder’s [`keyCommands`](uiresponder/keycommands.md) property.

## Parameters

- `input`: The keys that a person must press. The string must contain one or more characters corresponding to the keys a person pressed. For a list of special characters that don’t have a textual representation, see  .
- `modifierFlags`: The bit mask of modifier keys that a person must press. You can use this parameter to specify which modifier keys (Command, Option, and so on) a person must also press. You may specify more than one modifier key. For a list of possible values, see  .
- `action`: The action method to execute on the responder object.
- `discoverabilityTitle`: An elaborated title that explains the purpose of the key command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeycommand/init(input:modifierflags:action:discoverabilitytitle:))*