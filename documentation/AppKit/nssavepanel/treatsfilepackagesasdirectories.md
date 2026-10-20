# treatsFilePackagesAsDirectories

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the panel displays file packages as directories.

**Availability**:
- macOS

## Declaration

```swift
var treatsFilePackagesAsDirectories: Bool { get set }
```

```objc
@property BOOL treatsFilePackagesAsDirectories;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the panel displays file packages as directories; if [`false`](../../Swift/false.md), it will not.

## See Also

### Configuring the File Types
- [var allowedContentTypes: [UTType]](./allowedcontenttypes.md)
  An array of types that specify the files types to which you can save.
- [var allowsOtherFileTypes: Bool](./allowsotherfiletypes.md)
  A Boolean value that indicates whether the panel allows the user to save files with a filename extension that’s not in the list of allowed types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/treatsfilepackagesasdirectories)*