# addTextField(configurationHandler:)

**Framework**: UIKit  
**Kind**: method

Adds a text field to an alert.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addTextField(configurationHandler: ((UITextField) -> Void)? = nil)
```

#### Discussion

Calling this method adds an editable text field to the alert. You can call this method more than once to add additional text fields. The text fields are stacked in the resulting alert.

You can add a text field only if the [`preferredStyle`](uialertcontroller/preferredstyle.md) property is set to [`UIAlertController.Style.alert`](uialertcontroller/style/alert.md).

## Parameters

- `configurationHandler`: A block for configuring the text field prior to displaying the alert. This block has no return value and takes a single parameter corresponding to the text field object. Use that parameter to change the text field properties.

## See Also

- [var textFields: [UITextField]?](uialertcontroller/textfields.md)
  The array of text fields displayed by the alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertcontroller/addtextfield(configurationhandler:))*