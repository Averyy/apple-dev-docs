# UIItemProviderPresentationSizeProviding

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIItemProviderPresentationSizeProviding : NSObjectProtocol
```

```objc
@protocol UIItemProviderPresentationSizeProviding <NSObject>
```

## Topics

### Determining the presentation size
- [var preferredPresentationSizeForItemProvider: CGSize](./uiitemproviderpresentationsizeproviding/preferredpresentationsizeforitemprovider.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [UIImage](./uiimage.md)

## See Also

### Item providers
- [Data delivery with drag and drop](./data-delivery-with-drag-and-drop.md)
  Share data between iPad apps during a drag and drop operation using an item provider.
- [class NSItemProvider](../Foundation/nsitemprovider.md)
  An item provider for conveying data or a file between processes during drag-and-drop or copy-and-paste activities, or from a host app to an app extension.
- [protocol NSItemProviderReading](../Foundation/nsitemproviderreading.md)
  The protocol for implementing a class to allow an item provider to create an instance of the class.
- [protocol NSItemProviderWriting](../Foundation/nsitemproviderwriting.md)
  The protocol for implementing a class to allow an item provider to retrieve data from an instance of the class.
- [protocol UIItemProviderReadingAugmentationDesignating](./uiitemproviderreadingaugmentationdesignating.md)
- [protocol UIItemProviderReadingAugmentationProviding](./uiitemproviderreadingaugmentationproviding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiitemproviderpresentationsizeproviding)*