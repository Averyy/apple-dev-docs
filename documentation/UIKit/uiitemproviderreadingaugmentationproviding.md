# UIItemProviderReadingAugmentationProviding

**Framework**: UIKit  
**Kind**: protocol

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS 10.4+

## Declaration

```swift
protocol UIItemProviderReadingAugmentationProviding
```

## Topics

### Type Properties
- [static var additionalLeadingReadableTypeIdentifiersForItemProvider: [String]](uiitemproviderreadingaugmentationproviding/additionalleadingreadabletypeidentifiersforitemprovider.md)
- [static var additionalTrailingReadableTypeIdentifiersForItemProvider: [String]](uiitemproviderreadingaugmentationproviding/additionaltrailingreadabletypeidentifiersforitemprovider.md)
### Type Methods
- [static func object(withItemProviderData: Data, typeIdentifier: String, requestedClass: AnyClass) throws -> Any](uiitemproviderreadingaugmentationproviding/object(withitemproviderdata:typeidentifier:requestedclass:).md)

## See Also

- [Data delivery with drag and drop](data-delivery-with-drag-and-drop.md)
  Share data between iPad apps during a drag and drop operation using an item provider.
- [class NSItemProvider](../Foundation/NSItemProvider.md)
  An item provider for conveying data or a file between processes during drag-and-drop or copy-and-paste activities, or from a host app to an app extension.
- [protocol NSItemProviderReading : NSObjectProtocol](../Foundation/NSItemProviderReading.md)
  The protocol for implementing a class to allow an item provider to create an instance of the class.
- [protocol NSItemProviderWriting : NSObjectProtocol](../Foundation/NSItemProviderWriting.md)
  The protocol for implementing a class to allow an item provider to retrieve data from an instance of the class.
- [protocol UIItemProviderPresentationSizeProviding](uiitemproviderpresentationsizeproviding.md)
- [protocol UIItemProviderReadingAugmentationDesignating](uiitemproviderreadingaugmentationdesignating.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiitemproviderreadingaugmentationproviding)*