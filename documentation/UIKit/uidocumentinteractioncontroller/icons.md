# icons

**Framework**: UIKit  
**Kind**: property

The images associated with the target file.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var icons: [UIImage] { get }
```

#### Discussion

This property contains an array of [`UIImage`](uiimage.md) objects containing the available icons for the given file. The images in the array are sorted from smallest to largest, with the smallest image located at index 0. The returned array always contains at least one image.

The images themselves are provided by the system and determined by the UTI of the file. Apps can register custom icons for their associated files by including the appropriate meta information in their `Info.plist` file. If no custom icon exists, the images in this property represent the generic document icon.

## See Also

- [var url: URL?](uidocumentinteractioncontroller/url.md)
  The URL identifying the target file on the local filesystem.
- [var uti: String?](uidocumentinteractioncontroller/uti.md)
  The type of the target file.
- [var name: String?](uidocumentinteractioncontroller/name.md)
  The name of the target file.
- [var annotation: Any?](uidocumentinteractioncontroller/annotation.md)
  Custom property list information for the target file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/icons)*