# allowsOtherFileTypes

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the panel allows the user to save files with a filename extension that’s not in the list of allowed types.

**Availability**:
- macOS

## Declaration

```swift
var allowsOtherFileTypes: Bool { get set }
```

```objc
@property BOOL allowsOtherFileTypes;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the panel allows the user to save files with an extension that’s not in the list of allowed types. The default value is [`false`](../../Swift/false.md).

If the user tries to save a filename with a recognized extension that’s not in the list of allowed types, they are presented with a dialog. If the value of this property is [`true`](../../Swift/true.md), then the dialog presents the option of using the extension the user specified.

## See Also

### Configuring the File Types
- [var allowedContentTypes: [UTType]](./allowedcontenttypes.md)
  An array of types that specify the files types to which you can save.
- [var treatsFilePackagesAsDirectories: Bool](./treatsfilepackagesasdirectories.md)
  A Boolean value that indicates whether the panel displays file packages as directories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/allowsotherfiletypes)*