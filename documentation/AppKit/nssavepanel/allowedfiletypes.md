# allowedFileTypes

**Framework**: AppKit  
**Kind**: property

An array of filename extensions or UTIs that represent the allowed file types for the panel.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
var allowedFileTypes: [String]? { get set }
```

#### Discussion

Use this property to specify the file types for the user to select from. A file type can be a common filename extension, or a UTI. The default value of this property is `nil`, which indicates that any file type can be used. If you specify an empty array for this parameter, the Save panel raises an exception.

If the user doesn’t select a type, the panel uses the first item in the `allowedFileTypes` array. If [`allowsOtherFileTypes`](nssavepanel/allowsotherfiletypes.md) is [`true`](https://developer.apple.com/documentation/swift/true), and the user enters a filename extension that doesn’t match one of the types in the array, AppKit prompts the user to confirm the choice.

[`NSOpenPanel`](nsopenpanel.md): In versions of macOS earlier than v10.6, this property is ignored. For applications that link against v10.6 and higher, this property determines which files the open panel enables. Don’t use the deprecated methods to show the open panel (that is, the methods that take a `types:` parameter) because they will overwrite this value. The allowed file types can be changed while the panel is running (for example, from an accessory view). This is also known as the “enabled file types.” A `nil` value indicates that all files should be enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/allowedfiletypes)*