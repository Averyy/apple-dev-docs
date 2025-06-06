# isRegularFile

**Framework**: Foundation  
**Kind**: property

This property contains a boolean value that indicates whether the file wrapper object is a regular-file.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isRegularFile: Bool { get }
```

#### Discussion

This property contains [`true`](https://developer.apple.com/documentation/swift/true) when the file wrapper object is a regular-file wrapper, otherwise it contains [`false`](https://developer.apple.com/documentation/swift/false). Invocations of [`read(from:options:)`](filewrapper/read(from:options:).md) may change the value of this property if the type of the file on disk has changed.

## See Also

- [var isDirectory: Bool](filewrapper/isdirectory.md)
  This property contains a boolean value indicating whether the file wrapper is a directory file wrapper.
- [var isSymbolicLink: Bool](filewrapper/issymboliclink.md)
  A boolean that indicates whether the file wrapper object is a symbolic-link file wrapper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/isregularfile)*