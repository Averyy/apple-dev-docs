# typeIdentifierHint

**Framework**: Core Image  
**Kind**: property

The uniform type identifier string to use in cases where a file’s format cannot be conclusively determined based solely on its contents.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static let typeIdentifierHint: CIImageOption
```

#### Discussion

The value of this key should be an `NSString` containing a hint. It is most commonly needed for some RAW file formats which can also be
interpreted as TIFF files.

This option is only supported by these APIs:

- `/CIImage/imageWithContentsOfURL:options:`
- `/CIImage/initWithContentsOfURL:options:`
- `/CIImage/imageWithData:options:`
- `/CIImage/initWithData:options:`

> **Note**: The key `kCGImageSourceTypeIdentifierHint` key can also be used for this purpose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageoption/typeidentifierhint)*