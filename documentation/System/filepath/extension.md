# extension

**Framework**: System  
**Kind**: property

The extension of the file or directory last component.

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
var `extension`: String? { get set }
```

#### Discussion

If `lastComponent` is `nil` or one of the special path components `.` or `..`, `get` returns `nil` and `set` does nothing.

If `lastComponent` does not contain a `.` anywhere, or only at the start, `get` returns `nil` and `set` will append a `.` and `newValue` to `lastComponent`.

Otherwise `get` returns everything after the last `.` and `set` will replace the extension.

Examples:

- `/tmp/foo.txt                  => txt`
- `/Applications/Foo.app/        => app`
- `/Applications/Foo.app/bar.txt => txt`
- `/tmp/foo.tar.gz               => gz`
- `/tmp/.hidden                  => nil`
- `/tmp/.hidden.                 => ""`
- `/tmp/..                       => nil`

Example:

```swift
var path = "/tmp/file"
path.extension = "txt" // path is "/tmp/file.txt"
path.extension = "o"   // path is "/tmp/file.o"
path.extension = nil    // path is "/tmp/file"
path.extension = ""     // path is "/tmp/file."
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/extension)*