# preferredPresentationStyle

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The preferred style for presenting the item provider’s data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var preferredPresentationStyle: NSItemProvider.PreferredPresentationStyle { get set }
```

```objc
@property (nonatomic) UIPreferredPresentationStyle preferredPresentationStyle;
```

## Discussion

The default preferred presentation style is `unspecified`.

## See Also

### Configuring the provider
- [var preferredPresentationSize: CGSize](./preferredpresentationsize.md)
  The ideal presentation size of the item.
- [NSItemProvider.PreferredPresentationStyle](./preferredpresentationstyle-swift.enum.md)
  The presentation styles that determine how a view shows an item provider’s data.
- [var suggestedName: String?](./suggestedname.md)
  The filename to use when writing the provided data to a file on disk.
- [var teamData: Data?](./teamdata.md)
  The collection of data an app uses to hold private team information during drag and drop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/preferredpresentationstyle-swift.property)*