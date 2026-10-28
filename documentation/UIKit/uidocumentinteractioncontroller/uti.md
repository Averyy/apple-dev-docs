# uti

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The type of the target file.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var uti: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * UTI;
```

## Discussion

The value of this property is used to determine which apps are capable of opening the document. The default value is determined automatically whenever possible. However, if the document is a custom type that cannot be determined readily, the value of this property may be `nil`. If you know the type of the document, you can set the value of this property explicitly.

## See Also

### Accessing the target document’s attributes
- [var url: URL?](./url.md)
  The URL identifying the target file on the local filesystem.
- [var name: String?](./name.md)
  The name of the target file.
- [var icons: [UIImage]](./icons.md)
  The images associated with the target file.
- [var annotation: Any?](./annotation.md)
  Custom property list information for the target file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/uti)*