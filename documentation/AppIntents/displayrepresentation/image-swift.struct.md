# DisplayRepresentation.Image

**Framework**: App Intents  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
struct Image
```

## Topics

### Structures
- [DisplayRepresentation.Image.DisplayStyle](./image-swift.struct/displaystyle.md)
  The style with which to display the image for this `DisplayRepresentation`.
### Initializers
- [init(data: Data, isTemplate: Bool?)](./image-swift.struct/init%28data,istemplate%29.md)
  Creates an image object from the specified data.
- [init(data: Data, isTemplate: Bool?, displayStyle: DisplayRepresentation.Image.DisplayStyle)](./image-swift.struct/init%28data,istemplate,displaystyle%29.md)
  Creates an image from the specified data, specifying the display style.
- [init(named: String, isTemplate: Bool?)](./image-swift.struct/init%28named,istemplate%29.md)
  Creates an image object from an image file in the extension’s bundle.
- [init(named: String, isTemplate: Bool?, displayStyle: DisplayRepresentation.Image.DisplayStyle)](./image-swift.struct/init%28named,istemplate,displaystyle%29.md)
  Creates an image from an image file in the extension’s bundle, specifying the display style.
- [init(systemName: String, isTemplate: Bool?)](./image-swift.struct/init%28systemname,istemplate%29.md)
  Creates an image object that contains the specified system symbol image.
- [init?(systemName: String, tintColor: UIColor?, symbolConfiguration: UIImage.SymbolConfiguration?)](./image-swift.struct/init%28systemname,tintcolor,symbolconfiguration%29-3snvy.md)
  Creates an image object backed by the given SF Symbol name, with optional configuration options.
- [init?(systemName: String, tintColor: NSColor?, symbolConfiguration: NSImage.SymbolConfiguration?)](./image-swift.struct/init%28systemname,tintcolor,symbolconfiguration%29-5p911.md)
  Creates an image object backed by the given SF Symbol name, with optional configuration options.
- [init(url: URL, isTemplate: Bool?)](./image-swift.struct/init%28url,istemplate%29.md)
  Creates an image object from an image file in the local file system.
- [init(url: URL, isTemplate: Bool?, displayStyle: DisplayRepresentation.Image.DisplayStyle)](./image-swift.struct/init%28url,istemplate,displaystyle%29.md)
  Creates an image from an image file in the local file system, specifying the display style.
- [init(url: URL, width: Double, height: Double, isTemplate: Bool?)](./image-swift.struct/init%28url,width,height,istemplate%29.md)
  Creates an image object, of the specified size, from an image file in the local file system.
- [init(url: URL, width: Double, height: Double, isTemplate: Bool?, displayStyle: DisplayRepresentation.Image.DisplayStyle)](./image-swift.struct/init%28url,width,height,istemplate,displaystyle%29.md)
  Creates an image, of the specified size, from an image file in the local file system, specifying the display style.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Displaying the content
- [var title: LocalizedStringResource](./title.md)
- [var subtitle: LocalizedStringResource?](./subtitle.md)
- [var image: DisplayRepresentation.Image?](./image-swift.property.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/displayrepresentation/image-swift.struct)*