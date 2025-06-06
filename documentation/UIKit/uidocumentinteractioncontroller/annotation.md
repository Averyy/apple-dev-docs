# annotation

**Framework**: UIKit  
**Kind**: property

Custom property list information for the target file.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var annotation: Any? { get set }
```

#### Discussion

Use this property to pass information about the document type to the app responsible for opening it. Although the type of this object should be one used to contain property list information—namely, [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary), [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray), [`NSData`](https://developer.apple.com/documentation/Foundation/NSData), [`NSString`](https://developer.apple.com/documentation/Foundation/NSString), [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber), or [`NSDate`](https://developer.apple.com/documentation/Foundation/NSDate)—the root object must be an [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary).

## See Also

- [var url: URL?](uidocumentinteractioncontroller/url.md)
  The URL identifying the target file on the local filesystem.
- [var uti: String?](uidocumentinteractioncontroller/uti.md)
  The type of the target file.
- [var name: String?](uidocumentinteractioncontroller/name.md)
  The name of the target file.
- [var icons: [UIImage]](uidocumentinteractioncontroller/icons.md)
  The images associated with the target file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/annotation)*