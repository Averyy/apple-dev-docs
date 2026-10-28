# image

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The image content of the frame to be processed.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var image: CIImage { get }
```

```objc
@property (readonly) CIImage * image;
```

## Discussion

Core Image provides several ways to perform your adjustments to this image:

- Create a single [`CIFilter`](../../CoreImage/cifilter-swift.class.md) object, or a chain of filters. Set this image as the [`kCIInputImageKey`](../../CoreImage/kciinputimagekey.md) parameter of the first filter in the chain, and use the last filter’s [`outputImage`](../../CoreImage/cifilter-swift.class/outputimage.md) property to access the result. Each [`CIFilter`](../../CoreImage/cifilter-swift.class.md) object can be a built-in filter or a custom filter subclass that you create.
- Use the [`applyingFilter(_:parameters:)`](../../CoreImage/ciimage/applyingfilter%28_,parameters%29.md) method to conveniently apply one of the many built-in Core Image filters.
- Access pixel buffers directly and apply custom image processing using a custom [`CIImageProcessorKernel`](../../CoreImage/ciimageprocessorkernel.md) subclass.

In all cases, you obtain another [`CIImage`](../../CoreImage/ciimage.md) object representing the result of your adjustments. Return that image from your [`frameProcessor`](../phlivephotoeditingcontext/frameprocessor.md) block. (See the [`frameProcessor`](../phlivephotoeditingcontext/frameprocessor.md) description for example code.)


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephotoframe/image)*