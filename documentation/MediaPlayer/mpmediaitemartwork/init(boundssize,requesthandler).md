# init(boundsSize:requestHandler:)

**Framework**: Media Player  
**Kind**: init  
**Role**: Initializer

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
init(boundsSize: CGSize, requestHandler: @escaping (CGSize) -> UIImage)
```

*macOS*

```swift
init(boundsSize: CGSize, requestHandler: @escaping (CGSize) -> NSImage)
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
- (instancetype) initWithBoundsSize:(CGSize) boundsSize requestHandler:(UIImage * (^)(CGSize size)) requestHandler;
```

*macOS*

```objc
- (instancetype) initWithBoundsSize:(CGSize) boundsSize requestHandler:(NSImage * (^)(CGSize size)) requestHandler;
```

## Return Value

The newly resized artwork.

## Discussion

The request handler returns the image in the newly requested size. The requested size must be less than the `boundsSize` parameter.

## Parameters

- `boundsSize`: The original size of the artwork.
- `requestHandler`: A handler that the system calls for the requested artwork.

  - **size**: The new size for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork/init(boundssize:requesthandler:))*