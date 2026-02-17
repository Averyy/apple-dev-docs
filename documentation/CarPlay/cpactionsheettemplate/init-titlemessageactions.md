# init(title:message:actions:)

**Framework**: CarPlay  
**Kind**: init

Creates an action sheet template.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(title: String?, message: String?, actions: [CPAlertAction])
```

#### Return Value

A newly initialized action sheet template.

## Parameters

- `title`: The title of the action sheet.
- `message`: A descriptive message providing details about the reason for displaying the action sheet.
- `actions`: A list of actions available on the action sheet. The array must contain at least one action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpactionsheettemplate/init(title:message:actions:))*