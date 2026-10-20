# isSymbolicLink

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A boolean that indicates whether the file wrapper object is a symbolic-link file wrapper.

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
var isSymbolicLink: Bool { get }
```

```objc
@property (readonly, getter=isSymbolicLink) BOOL symbolicLink;
```

#### Discussion

This property contains [`true`](../../Swift/true.md) when the file wrapper object is a symbolic-link file wrapper, [`false`](../../Swift/false.md) otherwise.

Invocations of [`read(from:options:)`](./read%28from,options%29.md) may change the value contained by this property, if the type of the file on disk has changed.

## See Also

### Querying File Wrappers
- [var isRegularFile: Bool](./isregularfile.md)
  This property contains a boolean value that indicates whether the file wrapper object is a regular-file.
- [var isDirectory: Bool](./isdirectory.md)
  This property contains a boolean value indicating whether the file wrapper is a directory file wrapper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/issymboliclink)*