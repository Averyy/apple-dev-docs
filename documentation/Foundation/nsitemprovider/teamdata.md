# teamData

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The collection of data an app uses to hold private team information during drag and drop.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var teamData: Data? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSData * teamData;
```

## See Also

### Configuring the provider
- [var preferredPresentationSize: CGSize](./preferredpresentationsize.md)
  The ideal presentation size of the item.
- [var preferredPresentationStyle: NSItemProvider.PreferredPresentationStyle](./preferredpresentationstyle-swift.property.md)
  The preferred style for presenting the item provider’s data.
- [NSItemProvider.PreferredPresentationStyle](./preferredpresentationstyle-swift.enum.md)
  The presentation styles that determine how a view shows an item provider’s data.
- [var suggestedName: String?](./suggestedname.md)
  The filename to use when writing the provided data to a file on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/teamdata)*