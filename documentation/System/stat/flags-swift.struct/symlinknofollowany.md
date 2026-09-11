# symlinkNoFollowAny

**Framework**: System  
**Kind**: property

If the path ends with a symbolic link, return information about the link itself. If *any* symbolic link is encountered during path resolution, return an error.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static var symlinkNoFollowAny: Stat.Flags { get }
```

#### Discussion

The corresponding C constant is `AT_SYMLINK_NOFOLLOW_ANY`.

> **Note**: Only available on Darwin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat/flags-swift.struct/symlinknofollowany)*