# name

**Framework**: UIKit  
**Kind**: property

The name of the target file.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var name: String? { get set }
```

#### Discussion

This property contains the filename without any preceding path information. The default value of this property is derived from the path information in the [`url`](uidocumentinteractioncontroller/url.md) property. You can change the value of this property as needed if you want to associate a different name with the file.

## See Also

- [var url: URL?](uidocumentinteractioncontroller/url.md)
  The URL identifying the target file on the local filesystem.
- [var uti: String?](uidocumentinteractioncontroller/uti.md)
  The type of the target file.
- [var icons: [UIImage]](uidocumentinteractioncontroller/icons.md)
  The images associated with the target file.
- [var annotation: Any?](uidocumentinteractioncontroller/annotation.md)
  Custom property list information for the target file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/name)*