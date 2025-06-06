# isAbsolute

**Framework**: System  
**Kind**: property

Returns true if this path uniquely identifies the location of a file without reference to an additional starting location.

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
var isAbsolute: Bool { get }
```

#### Discussion

On Unix platforms, absolute paths begin with a `/`. `isAbsolute` is equivalent to `root != nil`.

On Windows, absolute paths are fully qualified paths. `isAbsolute` is  equivalent to `root != nil` for traditional DOS paths (e.g. `C:foo` and `\bar` have roots but are not absolute). UNC paths and device paths are always absolute. Traditional DOS paths are absolute only if they begin with a volume or drive followed by a `:` and a separator.

NOTE: This does not perform shell expansion or substitute environment variables; paths beginning with `~` are considered relative.

Examples:

- Unix: - `/usr/local/bin`
- `/tmp/foo.txt`
- `/`
- Windows: - `C:\Users\`
- `\\?\UNC\server\share\bar.exe`
- `\\server\share\bar.exe`


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/isabsolute)*