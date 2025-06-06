# textContentType(_:)

**Framework**: RealityKit  
**Kind**: method

Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.

**Availability**:
- macOS 11.0+

## Declaration

```swift
nonisolated
func textContentType(_ textContentType: NSTextContentType?) -> some View
```

#### Discussion

Use this method to set the content type for input text. For example, you can configure a `TextField` for the entry of a username:

```None
TextField("Enter your username", text: $username)
    .textContentType(.username)
```

## Parameters

- `textContentType`: One of the content types available in the     structure that identify the semantic meaning expected for a text-entry   area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewdefaultplaceholder/textcontenttype(_:)-8hp93)*