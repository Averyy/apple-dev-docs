# lastComponent

**Framework**: System  
**Kind**: property

Returns the final component of the path. Returns `nil` if the path is empty or only contains a root.

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
var lastComponent: FilePath.Component? { get }
```

#### Discussion

Note: Even if the final component is a special directory (`.` or `..`), it will still be returned. See `lexicallyNormalize()`.

Examples:

- Unix: - `/usr/local/bin/ => bin`
- `/tmp/foo.txt    => foo.txt`
- `/tmp/foo.txt/.. => ..`
- `/tmp/foo.txt/.  => .`
- `/               => nil`
- Windows: - `C:\Users\                    => Users`
- `C:Users\                     => Users`
- `C:\                          => nil`
- `\Users\                      => Users`
- `\\?\UNC\server\share\bar.exe => bar.exe`
- `\\server\share               => nil`
- `\\?\UNC\server\share\        => nil`


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/lastcomponent)*