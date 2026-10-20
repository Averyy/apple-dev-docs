# isDirectory

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

This property contains a boolean value indicating whether the file wrapper is a directory file wrapper.

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
var isDirectory: Bool { get }
```

```objc
@property (readonly, getter=isDirectory) BOOL directory;
```

#### Discussion

This property will contain YES when the file wrapper is a directory file wrapper, otherwise it contains NO.

> **Note**:  Invocations of [`read(from:options:)`](./read%28from,options%29.md) may change the value of this property, if the type of the file on disk has changed.

## See Also

### Querying File Wrappers
- [var isRegularFile: Bool](./isregularfile.md)
  This property contains a boolean value that indicates whether the file wrapper object is a regular-file.
- [var isSymbolicLink: Bool](./issymboliclink.md)
  A boolean that indicates whether the file wrapper object is a symbolic-link file wrapper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/isdirectory)*