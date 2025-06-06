# CMMuxedFormatDescriptionCreate(allocator:muxType:extensions:formatDescriptionOut:)

**Framework**: Core Media  
**Kind**: func

Creates a format description for a muxed media stream.

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
func CMMuxedFormatDescriptionCreate(allocator: CFAllocator?, muxType: CMMuxedStreamType, extensions: CFDictionary?, formatDescriptionOut: UnsafeMutablePointer<CMMuxedFormatDescription?>) -> OSStatus
```

#### Return Value

A result code. Returns `noErr` if successful.

#### Discussion

A muxed format description does not know the formats of the sub-streams within the muxed stream. That information will only be discoverable by the demuxer software (or other software which understands the details of the muxed bitstream) which will need to produce separate format descriptions for each of its output streams. The caller owns the returned `CMFormatDescription`, and must release it when done with it. All input parameters are copied (the extensions are deep-copied).  The caller can deallocate them or re-use them after making this call.

## Parameters

- `allocator`:   to be used. Pass   or   to use the default allocator.
- `muxType`: Type of the muxed stream (e.g.   for MPEG-2 transport stream). This is the media subtype, and will be returned if you subsequently call   (or  ).
- `extensions`: Dictionary of extension key/value pairs. Keys are always of type  . Values are always property list objects (i.e..  ,  ,  ,  ,  ,  , or  ). Can be  .
- `formatDescriptionOut`: On output, returns newly created muxed 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmuxedformatdescriptioncreate(allocator:muxtype:extensions:formatdescriptionout:))*