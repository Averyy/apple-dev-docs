# CMFormatDescriptionCreate(allocator:mediaType:mediaSubType:extensions:formatDescriptionOut:)

**Framework**: Core Media  
**Kind**: func

Creates a format description for general use.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMFormatDescriptionCreate(allocator: CFAllocator?, mediaType: CMMediaType, mediaSubType: FourCharCode, extensions: CFDictionary?, formatDescriptionOut: UnsafeMutablePointer<CMFormatDescription?>) -> OSStatus
```

#### Return Value

A result code.

#### Discussion

The system uses the default allocator if you don’t specify one. Use this to create any `CMFormatDescription` that is composed solely of extensions, and for which `CFEqual`() of the extensions dictionaries is a valid test for Format Description equality.

Don’t call this method for media types that have specific create functions, such as [`CMAudioFormatDescriptionCreate(allocator:asbd:layoutSize:layout:magicCookieSize:magicCookie:extensions:formatDescriptionOut:)`](cmaudioformatdescriptioncreate(allocator:asbd:layoutsize:layout:magiccookiesize:magiccookie:extensions:formatdescriptionout:).md) and [`CMVideoFormatDescriptionCreate(allocator:codecType:width:height:extensions:formatDescriptionOut:)`](cmvideoformatdescriptioncreate(allocator:codectype:width:height:extensions:formatdescriptionout:).md).

## Parameters

- `allocator`: The allocator to use for creating the  .
- `mediaType`: The type that identifies the media.
- `mediaSubType`: The type that identifies the subtype of the media.
- `extensions`: A dictionary of extensions to attach to the description. May be  .
- `formatDescriptionOut`: Receives the   the function creates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescriptioncreate(allocator:mediatype:mediasubtype:extensions:formatdescriptionout:))*