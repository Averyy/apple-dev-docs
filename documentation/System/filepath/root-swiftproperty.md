# root

**Framework**: System  
**Kind**: property

Returns the root of a path if there is one, otherwise `nil`.

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
var root: FilePath.Root? { get set }
```

#### Discussion

On Unix, this will return the leading `/` if the path is absolute and `nil` if the path is relative.

On Windows, for traditional DOS paths, this will return the path prefix up to and including a root directory or a supplied drive or volume. Otherwise, if the path is relative to both the current directory and current drive, returns `nil`.

On Windows, for UNC or device paths, this will return the path prefix up to and including the host and share for UNC paths or the volume for device paths followed by any subsequent separator.

Examples:

- Unix: - `/foo/bar => /`
- `foo/bar  => nil`
- Windows: - `C:\foo\bar                => C:\`
- `C:foo\bar                 => C:`
- `\foo\bar                  => \ `
- `foo\bar                   => nil`
- `\\server\share\file       => \\server\share\`
- `\\?\UNC\server\share\file => \\?\UNC\server\share\`
- `\\.\device\folder         => \\.\device\`

Setting the root to `nil` will remove the root and setting a new root will replace the root.

Example:

```swift
var path: FilePath = "/foo/bar"
path.root = nil // path is "foo/bar"
path.root = "/" // path is "/foo/bar"
```

Example (Windows):

```swift
var path: FilePath = #"\foo\bar"#
path.root = nil         // path is #"foo\bar"#
path.root = "C:"        // path is #"C:foo\bar"#
path.root = #"C:\"#     // path is #"C:\foo\bar"#
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/root-swift.property)*