# AVMetadataItemFilter

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that filters selected information from a metadata item.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class AVMetadataItemFilter
```

```objc
@interface AVMetadataItemFilter : NSObject
```

## Overview

Filter instances are opaque, unmodifiable objects, that you create with the [`forSharing()`](./avmetadataitemfilter/forsharing%28%29.md) class method.

## Topics

### Creating a metadata item filter
- [class func forSharing() -> AVMetadataItemFilter](./avmetadataitemfilter/forsharing%28%29.md)
  Returns a metadata filter to use for sharing assets.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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

### Metadata
- [Retrieving media metadata](./retrieving-media-metadata.md)
  Load descriptive metadata for media assets and their tracks.
- [class AVMetadataItem](./avmetadataitem.md)
  A metadata item for an audiovisual asset or one of its tracks.
- [class AVMutableMetadataItem](./avmutablemetadataitem.md)
  A mutable metadata item for an audiovisual asset or for one of its tracks.
- [struct AVMetadataIdentifier](./avmetadataidentifier.md)
  A structure that defines identifiers for metadata formats.
- [struct AVMetadataKey](./avmetadatakey.md)
  A structure that defines a metadata key.
- [struct AVMetadataKeySpace](./avmetadatakeyspace.md)
  A structure that defines a metadata key space.
- [struct AVMetadataExtraAttributeKey](./avmetadataextraattributekey.md)
  A structure that defines keys for extra metadata attributes.
- [struct AVMetadataFormat](./avmetadataformat.md)
  A structure that defines metadata formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitemfilter)*