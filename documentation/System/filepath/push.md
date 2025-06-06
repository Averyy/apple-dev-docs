# push(_:)

**Framework**: System  
**Kind**: method

If `other` does not have a root, append each component of `other`. If `other` has a root, replaces `self` with other.

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
mutating func push(_ other: FilePath)
```

#### Discussion

This operation mimics traversing a directory structure (similar to the `cd` command), where pushing a relative path will append its components and pushing an absolute path will first clear `self`’s existing components.

Example:

```swift
var path: FilePath = "/tmp"
path.push("dir/file.txt") // path is "/tmp/dir/file.txt"
path.push("/bin")         // path is "/bin"
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/push(_:))*