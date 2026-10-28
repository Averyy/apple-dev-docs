# preferredPresentationSize

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The ideal presentation size of the item.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
var preferredPresentationSize: CGSize { get set }
```

*macOS*

```swift
var preferredPresentationSize: NSSize { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic) CGSize preferredPresentationSize;
```

*macOS*

```objc
@property (readonly) NSSize preferredPresentationSize;
```

## Discussion

When displaying the item, the value in this property represents the ideal size at which to display the item. The size in this property may differ from the size in the [`sourceFrame`](./sourceframe.md) rectangle. For images, video, and other content with a natural size, the item automatically derives the size from that content. If the value in this property is [`NSZeroSize`](../nszerosize.md), use the size specified in the [`sourceFrame`](./sourceframe.md) rectangle.

## See Also

### Configuring the provider
- [var preferredPresentationStyle: NSItemProvider.PreferredPresentationStyle](./preferredpresentationstyle-swift.property.md)
  The preferred style for presenting the item provider’s data.
- [NSItemProvider.PreferredPresentationStyle](./preferredpresentationstyle-swift.enum.md)
  The presentation styles that determine how a view shows an item provider’s data.
- [var suggestedName: String?](./suggestedname.md)
  The filename to use when writing the provided data to a file on disk.
- [var teamData: Data?](./teamdata.md)
  The collection of data an app uses to hold private team information during drag and drop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/preferredpresentationsize)*