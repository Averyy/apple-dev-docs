# icons

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The images associated with the target file.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var icons: [UIImage] { get }
```

```objc
@property (nonatomic, readonly) NSArray<UIImage *> * icons;
```

#### Discussion

This property contains an array of [`UIImage`](../uiimage.md) objects containing the available icons for the given file. The images in the array are sorted from smallest to largest, with the smallest image located at index 0. The returned array always contains at least one image.

The images themselves are provided by the system and determined by the UTI of the file. Apps can register custom icons for their associated files by including the appropriate meta information in their `Info.plist` file. If no custom icon exists, the images in this property represent the generic document icon.

## See Also

### Accessing the target document’s attributes
- [var url: URL?](./url.md)
  The URL identifying the target file on the local filesystem.
- [var uti: String?](./uti.md)
  The type of the target file.
- [var name: String?](./name.md)
  The name of the target file.
- [var annotation: Any?](./annotation.md)
  Custom property list information for the target file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/icons)*