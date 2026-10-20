# installName

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

For a dynamic library, the name to use when installing the library.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var installName: String? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) NSString * installName;
```

## See Also

### Configuring the library output options
- [var libraryType: MTLLibraryType](./librarytype.md)
  The kind of library to create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcompileoptions/installname)*