# treatsFilePackagesAsDirectories

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the panel displays file packages as directories.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var treatsFilePackagesAsDirectories: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the panel displays file packages as directories; if [`false`](https://developer.apple.com/documentation/Swift/false), it will not.

## See Also

- [var allowedContentTypes: [UTType]](nssavepanel/allowedcontenttypes.md)
  An array of types that specify the files types to which you can save.
- [var allowsOtherFileTypes: Bool](nssavepanel/allowsotherfiletypes.md)
  A Boolean value that indicates whether the panel allows the user to save files with a filename extension that’s not in the list of allowed types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/treatsfilepackagesasdirectories)*