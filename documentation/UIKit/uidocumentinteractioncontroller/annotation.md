# annotation

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Custom property list information for the target file.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var annotation: Any? { get set }
```

```objc
@property (nonatomic, strong, nullable) id annotation;
```

## Discussion

Use this property to pass information about the document type to the app responsible for opening it. Although the type of this object should be one used to contain property list information—namely, [`NSDictionary`](../../Foundation/nsdictionary.md), [`NSArray`](../../Foundation/nsarray.md), [`NSData`](../../Foundation/nsdata.md), [`NSString`](../../Foundation/nsstring.md), [`NSNumber`](../../Foundation/nsnumber.md), or [`NSDate`](../../Foundation/nsdate.md)—the root object must be an [`NSDictionary`](../../Foundation/nsdictionary.md).

## See Also

### Accessing the target document’s attributes
- [var url: URL?](./url.md)
  The URL identifying the target file on the local filesystem.
- [var uti: String?](./uti.md)
  The type of the target file.
- [var name: String?](./name.md)
  The name of the target file.
- [var icons: [UIImage]](./icons.md)
  The images associated with the target file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/annotation)*