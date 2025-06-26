# textContentType(_:)

**Framework**: FamilyControls  
**Kind**: method

Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on an iOS or tvOS device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- tvOS 13.0+

## Declaration

```swift
nonisolated
func textContentType(_ textContentType: UITextContentType?) -> some View
```

#### Discussion

Use this method to set the content type for input text. For example, you can configure a `TextField` for the entry of email addresses:

```swift
TextField("Enter your email", text: $emailAddress)
    .textContentType(.emailAddress)
```

## Parameters

- `textContentType`: One of the content types available in the     structure that identify the semantic meaning expected for a text-entry   area. These include support for email addresses, location names, URLs,   and telephone numbers, to name just a few.

## See Also

- [func keyboardType(UIKeyboardType) -> some View](familyactivitypicker/keyboardtype(_:).md)
  Sets the keyboard type for this view.
- [func disableAutocorrection(Bool?) -> some View](familyactivitypicker/disableautocorrection(_:).md)
  Sets whether to disable autocorrection for this view.
- [func autocapitalization(UITextAutocapitalizationType) -> some View](familyactivitypicker/autocapitalization(_:).md)
  Sets whether to apply auto-capitalization to this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/textcontenttype(_:))*