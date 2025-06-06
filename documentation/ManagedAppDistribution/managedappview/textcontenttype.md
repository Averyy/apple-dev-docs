# textContentType(_:)

**Framework**: ManagedAppDistribution  
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

```None
TextField("Enter your email", text: $emailAddress)
    .textContentType(.emailAddress)
```

## Parameters

- `textContentType`: One of the content types available in the     structure that identify the semantic meaning expected for a text-entry   area. These include support for email addresses, location names, URLs,   and telephone numbers, to name just a few.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedappview/textcontenttype(_:))*