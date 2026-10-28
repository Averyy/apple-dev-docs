# PHImageContentMode

**Framework**: Photos  
**Kind**: enum  
**Role**: Enumeration

Options for fitting an image’s aspect ratio to a requested size, used by the [`requestImage(for:targetSize:contentMode:options:resultHandler:)`](./phimagemanager/requestimage%28for,targetsize,contentmode,options,resulthandler%29.md) method.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum PHImageContentMode
```

```c
enum PHImageContentMode : NSInteger;
```

## Overview

With either option, the resulting image may not exactly match the target size, depending on the [`deliveryMode`](./phimagerequestoptions/deliverymode.md) and [`resizeMode`](./phimagerequestoptions/resizemode.md) properties of the image request. To serve your request more quickly, Photos may provide a slightly larger image—one that it can generate more easily or one that is already cached.

## Topics

### Constants
- [static var `default`: PHImageContentMode](./phimagecontentmode/default.md)
  Fits the image to the requested size using the default option, [`PHImageContentMode.aspectFit`](./phimagecontentmode/aspectfit.md).
- [PHImageContentMode.aspectFit](./phimagecontentmode/aspectfit.md)
  Scales the image so that its larger dimension fits the target size.
- [PHImageContentMode.aspectFill](./phimagecontentmode/aspectfill.md)
  Scales the image so that it completely fills the target size.
### Initializers
- [init?(rawValue: Int)](./phimagecontentmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [Image Result Info Keys](../PhotoKit/image-result-info-keys.md)
  Keys identifying information about an image loading result, used in the `resultHandler` block with image request methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagecontentmode)*