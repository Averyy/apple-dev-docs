# allowedContentTypes

**Framework**: AppKit  
**Kind**: property

An array of types that specify the files types to which you can save.

**Availability**:
- macOS 11.0+

## Declaration

```swift
@MainActor
var allowedContentTypes: [UTType] { get set }
```

#### Discussion

Defaults to an empty array that indicates that you can use any file type. If you don’t provide an extension, the system uses the first preferred extension in the array for the save panel. If you specify a type that isn’t in the array and [`allowsOtherFileTypes`](nssavepanel/allowsotherfiletypes.md) is `YES`, the system presents another dialog when prompting you to save.

## See Also

- [var allowsOtherFileTypes: Bool](nssavepanel/allowsotherfiletypes.md)
  A Boolean value that indicates whether the panel allows the user to save files with a filename extension that’s not in the list of allowed types.
- [var treatsFilePackagesAsDirectories: Bool](nssavepanel/treatsfilepackagesasdirectories.md)
  A Boolean value that indicates whether the panel displays file packages as directories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/allowedcontenttypes)*