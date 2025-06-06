# init(boundsSize:requestHandler:)

**Framework**: Media Player  
**Kind**: init

Creates a new image from existing artwork with the specified bounds.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
init(boundsSize: CGSize, requestHandler: @escaping (CGSize) -> NSImage)
```

#### Return Value

The newly resized artwork.

#### Discussion

The request handler returns the image in the newly requested size. The requested size must be less than the `boundsSize` parameter.

## Parameters

- `boundsSize`: The original size of the artwork.
- `requestHandler`: A handler that the system calls for the requested artwork.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork/init(boundssize:requesthandler:))*