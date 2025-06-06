# NSItemProvider.PreferredPresentationStyle

**Framework**: Foundation  
**Kind**: enum

The presentation styles that determine how a view shows an item provider’s data.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
enum PreferredPresentationStyle
```

## Topics

### Presentation Styles
- [NSItemProvider.PreferredPresentationStyle.unspecified](nsitemprovider/preferredpresentationstyle-swift.enum/unspecified.md)
  A presentation style indicating that no preferred style is specified.
- [NSItemProvider.PreferredPresentationStyle.inline](nsitemprovider/preferredpresentationstyle-swift.enum/inline.md)
  A presentation style indicating that the item provider data should be presented inline.
- [NSItemProvider.PreferredPresentationStyle.attachment](nsitemprovider/preferredpresentationstyle-swift.enum/attachment.md)
  A presentation style indicating that the item provider data should be presented as an attachment.
### Initializers
- [init?(rawValue: Int)](nsitemprovider/preferredpresentationstyle-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var preferredPresentationSize: CGSize](nsitemprovider/preferredpresentationsize.md)
  The ideal presentation size of the item.
- [var preferredPresentationStyle: NSItemProvider.PreferredPresentationStyle](nsitemprovider/preferredpresentationstyle-swift.property.md)
  The preferred style for presenting the item provider’s data.
- [var suggestedName: String?](nsitemprovider/suggestedname.md)
  The filename to use when writing the provided data to a file on disk.
- [var teamData: Data?](nsitemprovider/teamdata.md)
  The collection of data an app uses to hold private team information during drag and drop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider/preferredpresentationstyle-swift.enum)*