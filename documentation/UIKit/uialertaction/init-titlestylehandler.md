# init(title:style:handler:)

**Framework**: UIKit  
**Kind**: init

Create and return an action with the specified title and behavior.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(title: String?, style: UIAlertAction.Style, handler: ((UIAlertAction) -> Void)? = nil)
```

#### Return Value

A new alert action object.

#### Discussion

Actions are enabled by default when you create them.

## Parameters

- `title`: The text to use for the button title. The value you specify should be localized for the user’s current language. This parameter must not be  , except in a tvOS app where a   title may be used with  .
- `style`: Additional styling information to apply to the button. Use the style information to convey the type of action that is performed by the button. For a list of possible values, see the constants in  .
- `handler`: A block to execute when the user selects the action. This block has no return value and takes the selected action object as its only parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertaction/init(title:style:handler:))*