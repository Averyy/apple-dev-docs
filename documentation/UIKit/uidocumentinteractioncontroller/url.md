# url

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The URL identifying the target file on the local filesystem.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var url: URL? { get set }
```

```objc
@property (strong, nullable) NSURL * URL;
```

## See Also

### Accessing the target document’s attributes
- [var uti: String?](./uti.md)
  The type of the target file.
- [var name: String?](./name.md)
  The name of the target file.
- [var icons: [UIImage]](./icons.md)
  The images associated with the target file.
- [var annotation: Any?](./annotation.md)
  Custom property list information for the target file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/url)*