# removingRoot()

**Framework**: System  
**Kind**: method

Creates a new path containing just the components, i.e. everything after `root`.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func removingRoot() -> FilePath
```

#### Discussion

Returns self if `root == nil`.

Examples:

- Unix: - `/foo/bar => foo/bar`
- `foo/bar  => foo/bar`
- `/        => ""`
- Windows: - `C:\foo\bar                  => foo\bar`
- `foo\bar                     => foo\bar`
- `\\?\UNC\server\share\file   => file`
- `\\?\device\folder\file.exe  => folder\file.exe`
- `\\server\share\file         => file`
- `\                           => ""`


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/removingroot())*