# isRegularFile

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, getter=isRegularFile) BOOL regularFile;
```

#### Discussion

This property contains [`true`](../../Swift/true.md) when the file wrapper object is a regular-file wrapper, otherwise it contains [`false`](../../Swift/false.md). Invocations of [`read(from:options:)`](./read%28from,options%29.md) may change the value of this property if the type of the file on disk has changed.

## See Also

### Querying File Wrappers
- [var isDirectory: Bool](./isdirectory.md)
  This property contains a boolean value indicating whether the file wrapper is a directory file wrapper.
- [var isSymbolicLink: Bool](./issymboliclink.md)
  A boolean that indicates whether the file wrapper object is a symbolic-link file wrapper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/isregularfile)*