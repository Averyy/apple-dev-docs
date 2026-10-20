# libraryType

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The kind of library to create.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var libraryType: MTLLibraryType { get set }
```

```objc
@property (nonatomic, readwrite) MTLLibraryType libraryType;
```

#### Discussion

The default value is [`MTLLibraryType.executable`](../mtllibrarytype/executable.md).

## See Also

### Configuring the library output options
- [var installName: String?](./installname.md)
  For a dynamic library, the name to use when installing the library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcompileoptions/librarytype)*