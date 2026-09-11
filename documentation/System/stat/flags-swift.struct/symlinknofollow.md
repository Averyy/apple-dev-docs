# symlinkNoFollow

**Framework**: System  
**Kind**: property

If the path ends with a symbolic link, return information about the link itself.

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
static var symlinkNoFollow: Stat.Flags { get }
```

#### Discussion

The corresponding C constant is `AT_SYMLINK_NOFOLLOW`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat/flags-swift.struct/symlinknofollow)*