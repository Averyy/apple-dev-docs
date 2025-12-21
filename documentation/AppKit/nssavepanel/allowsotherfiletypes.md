# allowsOtherFileTypes

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the panel allows the user to save files with a filename extension that’s not in the list of allowed types.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var allowsOtherFileTypes: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the panel allows the user to save files with an extension that’s not in the list of allowed types. The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

If the user tries to save a filename with a recognized extension that’s not in the list of allowed types, they are presented with a dialog. If the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), then the dialog presents the option of using the extension the user specified.

## See Also

- [var allowedContentTypes: [UTType]](nssavepanel/allowedcontenttypes.md)
  An array of types that specify the files types to which you can save.
- [var treatsFilePackagesAsDirectories: Bool](nssavepanel/treatsfilepackagesasdirectories.md)
  A Boolean value that indicates whether the panel displays file packages as directories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/allowsotherfiletypes)*