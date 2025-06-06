# suggestedName

**Framework**: Foundation  
**Kind**: property

The filename to use when writing the provided data to a file on disk.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
var suggestedName: String? { get set }
```

#### Discussion

Setting this property is recommended when providing [`NSData`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/OldStylePlists/OldStylePLists.html#//apple_ref/doc/uid/20001012-47169) or text data from an item provider.

## See Also

- [var preferredPresentationSize: CGSize](nsitemprovider/preferredpresentationsize.md)
  The ideal presentation size of the item.
- [var preferredPresentationStyle: NSItemProvider.PreferredPresentationStyle](nsitemprovider/preferredpresentationstyle-swift.property.md)
  The preferred style for presenting the item provider’s data.
- [NSItemProvider.PreferredPresentationStyle](nsitemprovider/preferredpresentationstyle-swift.enum.md)
  The presentation styles that determine how a view shows an item provider’s data.
- [var teamData: Data?](nsitemprovider/teamdata.md)
  The collection of data an app uses to hold private team information during drag and drop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/suggestedname)*