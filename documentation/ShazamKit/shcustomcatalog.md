# SHCustomCatalog

**Framework**: ShazamKit  
**Kind**: class  
**Role**: Class

An object for storing the reference signatures for custom audio recordings and their associated metadata.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class SHCustomCatalog
```

```objc
@interface SHCustomCatalog : SHCatalog
```

#### Overview

Create a custom catalog by adding reference signatures that you generate from audio that you provide. You also add the associated metadata for each signature. Save your custom catalog and share it with others. You can also load a saved catalog.

## Topics

### Creating a custom catalog object
- [init()](./shcustomcatalog/init%28%29.md)
  Creates a new custom catalog object for storing reference audio signatures and their associated metadata.
- [+ new](./shcustomcatalog/new.md)
  Creates a new custom catalog object for storing reference audio signatures and their associated metadata.
### Adding a signature to the catalog
- [func addReferenceSignature(SHSignature, representing: [SHMediaItem]) throws](./shcustomcatalog/addreferencesignature%28_,representing%29.md)
  Adds a reference signature and its associated metadata to a catalog.
### Loading and saving a custom catalog
- [func add(from: URL) throws](./shcustomcatalog/add%28from%29.md)
  Loads a saved custom catalog from a file.
- [func write(to: URL) throws](./shcustomcatalog/write%28to%29.md)
  Saves the custom catalog to a local file.
### Getting the content type
- [static var shazamCustomCatalog: UTType](../UniformTypeIdentifiers/uttype-swift.struct/shazamcustomcatalog.md)
  A type that represents a custom catalog.
- [SHCustomCatalogContentType](../UniformTypeIdentifiers/uttype-c.class/shcustomcatalogcontenttype.md)
  A type representing the @c SHCustomCatalog file format with the .shazamcatalog extension
### Initializers
- [init(dataRepresentation: Data) throws](./shcustomcatalog/init%28datarepresentation%29.md)
  Load a @c SHCustomCatalog from data
### Instance Properties
- [var dataRepresentation: Data](./shcustomcatalog/datarepresentation.md)
  The data representation of this file, it can be written to disk

## Relationships

### Inherits From
- [SHCatalog](./shcatalog.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Create a custom audio catalog
- [Building a Custom Catalog and Matching Audio](./building-a-custom-catalog-and-matching-audio.md)
  Display lesson content that’s synchronized to a learning video by matching the audio to a custom reference signature and associated metadata.
- [ShazamKit Dance Finder with Managed Session](./shazamkit-dance-finder-with-managed-session.md)
  Find a video of dance moves for a specific song by matching the audio to a custom catalog, and show a history of recognized songs.
- [class SHCatalog](./shcatalog.md)
  An abstract base class for storing reference signatures and their associated metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shcustomcatalog)*