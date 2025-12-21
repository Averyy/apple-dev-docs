# DisplayRepresentation.Image

**Framework**: App Intents  
**Kind**: struct

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
struct Image
```

## Topics

### Structures
- [DisplayRepresentation.Image.DisplayStyle](displayrepresentation/image-swift.struct/displaystyle.md)
  The style with which to display the image for this `DisplayRepresentation`.
### Initializers
- [init(data: Data, isTemplate: Bool?)](displayrepresentation/image-swift.struct/init(data:istemplate:).md)
  Creates an image object from the specified data.
- [init(data: Data, isTemplate: Bool?, displayStyle: DisplayRepresentation.Image.DisplayStyle)](displayrepresentation/image-swift.struct/init(data:istemplate:displaystyle:).md)
  Creates an image from the specified data, specifying the display style.
- [init(named: String, isTemplate: Bool?)](displayrepresentation/image-swift.struct/init(named:istemplate:).md)
  Creates an image object from an image file in the extension’s bundle.
- [init(named: String, isTemplate: Bool?, displayStyle: DisplayRepresentation.Image.DisplayStyle)](displayrepresentation/image-swift.struct/init(named:istemplate:displaystyle:).md)
  Creates an image from an image file in the extension’s bundle, specifying the display style.
- [init(systemName: String, isTemplate: Bool?)](displayrepresentation/image-swift.struct/init(systemname:istemplate:).md)
  Creates an image object that contains the specified system symbol image.
- [init?(systemName: String, tintColor: UIColor?, symbolConfiguration: UIImage.SymbolConfiguration?)](displayrepresentation/image-swift.struct/init(systemname:tintcolor:symbolconfiguration:)-3snvy.md)
  Creates an image object backed by the given SF Symbol name, with optional configuration options.
- [init?(systemName: String, tintColor: NSColor?, symbolConfiguration: NSImage.SymbolConfiguration?)](displayrepresentation/image-swift.struct/init(systemname:tintcolor:symbolconfiguration:)-5p911.md)
  Creates an image object backed by the given SF Symbol name, with optional configuration options.
- [init(url: URL, isTemplate: Bool?)](displayrepresentation/image-swift.struct/init(url:istemplate:).md)
  Creates an image object from an image file in the local file system.
- [init(url: URL, isTemplate: Bool?, displayStyle: DisplayRepresentation.Image.DisplayStyle)](displayrepresentation/image-swift.struct/init(url:istemplate:displaystyle:).md)
  Creates an image from an image file in the local file system, specifying the display style.
- [init(url: URL, width: Double, height: Double, isTemplate: Bool?)](displayrepresentation/image-swift.struct/init(url:width:height:istemplate:).md)
  Creates an image object, of the specified size, from an image file in the local file system.
- [init(url: URL, width: Double, height: Double, isTemplate: Bool?, displayStyle: DisplayRepresentation.Image.DisplayStyle)](displayrepresentation/image-swift.struct/init(url:width:height:istemplate:displaystyle:).md)
  Creates an image, of the specified size, from an image file in the local file system, specifying the display style.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var title: LocalizedStringResource](displayrepresentation/title.md)
- [var subtitle: LocalizedStringResource?](displayrepresentation/subtitle.md)
- [var image: DisplayRepresentation.Image?](displayrepresentation/image-swift.property.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/displayrepresentation/image-swift.struct)*