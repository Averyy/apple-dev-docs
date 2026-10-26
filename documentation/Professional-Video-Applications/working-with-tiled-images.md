# Working with tiled images

**Framework**: Professional-Video-Applications  
**Role**: Article

Render only the necessary tiles of an image in your FxPlug plug-in to improve efficiency.

#### Overview

Renders in FxPlug 4 are *tileable*, which means that the input image can be divided into smaller tiles for rendering. This improves the efficiency of your plug-in because the host app only asks for exactly what pixels your plug-in needs to render for each tile, and the plug-in tells the host exactly what pixels your plug-in needs to sample.

Two methods, [`sourceTileRect(_:sourceImageIndex:sourceImages:destinationTileRect:destinationImage:pluginState:at:)`](../professional_video_applications/fxtileableeffect/sourcetilerect%28_,sourceimageindex,sourceimages,destinationtilerect,destinationimage,pluginstate,at%29.md) and [`destinationImageRect(_:sourceImages:destinationImage:pluginState:at:)`](../professional_video_applications/fxtileableeffect/destinationimagerect%28_,sourceimages,destinationimage,pluginstate,at%29.md), help define the expected bounds for source and destination textures. These two sets of pixel bounds are `sourceTileRect` and `destinationImageRect`. They’re also known as region of interest (ROI) and domain of definition (DOD), respectively, in other rendering technologies like [Core Image](../CoreImage/CoreImage.md).

##### Define tiles for rendering

Before the host app can determine if it should tile its rendering, it must first know how a plug-in may transform the bounds of the input. For example, a glow filter expands the source image’s `imagePixelBounds`, and the new bounds need to be calculated and returned as the `destinationImageRect`. However, a color filter doesn’t require a change in bounds and instead simply returns the source image’s bounds as the `destinationImageRect`. For generators that aren’t required to conform to any bounds, you’ll likely set the `destinationImageRect` to `kFxRect_Infinite`.

Based on the `destinationImageRect` and the hardware capabilities, the host app may choose to divide the source image into multiple tiles and request separate renders of each tile on individual threads. This is why most filters require well-defined bounds for `sourceTileRect` and `destinationImageRect`. The host provides the requested `destinationTileRect` and expects the plug-in to calculate and return a `sourceTileRect`. If a filter only adjusts the color of pixels and outputs the new pixels with a 1:1 correspondence, each `sourceTileRect` equals the provided `destinationTileRect`, as in this example.

![An illustration of an input image next to an output image, with the colors inverted on the output image. Each image is divided into a grid of tiles. A highlighted rectangle that represents one example destinationTileRect is drawn on the output image. A corresponding rectangle representing the sourceTileRect is drawn on the input image in the same relative position and size to represent the pixels required to sample the output tile. An arrow is drawn between the two rectangles from destinationTileRect to sourceTileRect. The outside bounds of both the input image and output image are the same size, and an arrow is drawn between them from the input image to the output image.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3666155@2x.png)

Calculating the pixel values for a destination tile may require sampling a larger or smaller area of the source image, such as when blurring an image. In those cases, each `sourceTileRect` must expand to cover the appropriate sample area. In most cases, the `sourceTileRect` calculation mimics the filter’s fragment shader, but only the lower-left and upper-right coordinates of the rectangle need to be calculated. If the image should remain cropped to the source image’s bounds when blurred, then the `destinationImageRect` must be equal to the source image’s `imagePixelBounds`, as in this example.

![An illustration of an input image next to an output image, with the pixels blurred on the output image. Each image is divided into a grid of tiles. A highlighted rectangle that represents one example destinationTileRect is drawn on the output image. A corresponding rectangle representing the sourceTileRect is drawn on the input image in the same relative position, but with a larger size, to represent the pixels required to sample the output tile. An arrow is drawn between the two rectangles from destinationTileRect to sourceTileRect. The outside bounds of both the input image and output image are the same size, and an arrow is drawn between them from the input image to the output image.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3666148@2x.png)

If the filter distorts or convolutes the pixels in the image, it may require a larger or smaller `destinationImageRect`. The `destinationImageRect` calculation is typically the inverse of the plug-in’s fragment shader. The following example shows a filter that increases scale on just the x-axis.

![An illustration of an input image next to an output image, with the pixels scaled larger on the x-axis of the output image. Each image is divided into a grid of tiles. A highlighted rectangle that represents one example destinationTileRect is drawn on the output image. A corresponding rectangle representing the sourceTileRect is drawn on the input image in the same relative position, but with a smaller size, to represent the pixels required to sample the output tile. An arrow is drawn between the two rectangles from destinationTileRect to sourceTileRect. The outside bounds of the output image are larger than the input image, and an arrow is drawn between them from the input image to the output image.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3666154@2x.png)

##### Set the destination rectangle bounds

Your plug-in needs to return one of three types of destination rectangle bounds: infinite bounds (a generator that repeats infinitely), the original bounds (color filter), or bounds that are different from the original bounds (a filter that expands or shrinks the input).

The [`destinationImageRect(_:sourceImages:destinationImage:pluginState:at:)`](../professional_video_applications/fxtileableeffect/destinationimagerect%28_,sourceimages,destinationimage,pluginstate,at%29.md) method gives you your sources, plug-in state, and the render time. From these parameters, you can calculate what the destination rectangle should be. For example, the code below comes from the FxGradientCheckerboard generator example plug-in. For that generator, you return an infinite rectangle ([`kFxRect_Infinite`](../professional_video_applications/kfxrect_infinite.md)) because the checkerboard can be produced at any position, with no natural bounds to conform to.

**Swift**:

```swift
func destinationImageRect(_ destinationImageRect: UnsafeMutablePointer<FxRect>, sourceImages: [FxImageTile], destinationImage: FxImageTile, pluginState: Data?, at renderTime: CMTime) throws {
    destinationImageRect.pointee = kFxRect_Infinite
}
```

**Objective-C**:

```objc
- (BOOL)destinationImageRect:(FxRect *)destinationImageRect
                sourceImages:(NSArray<FxImageTile *> *)sourceImages
            destinationImage:(nonnull FxImageTile *)destinationImage
                 pluginState:(NSData *)pluginState
                      atTime:(CMTime)renderTime
                       error:(NSError * _Nullable *)outError
{
    *destinationImageRect = kFxRect_Infinite;

    return YES;
}
```

If the filter doesn’t change the overall dimensions of the source image, then simply return the original bounds of the source image. The example below is from the FxSimpleColorCorrector example plug-in.

**Swift**:

```swift
func destinationImageRect(_ destinationImageRect: UnsafeMutablePointer<FxRect>, sourceImages: [FxImageTile], destinationImage: FxImageTile, pluginState: Data?, at renderTime: CMTime) throws {
    destinationImageRect.pointee = sourceImages[0].imagePixelBounds
}
```

**Objective-C**:

```objc
- (BOOL)destinationImageRect:(FxRect *)destinationImageRect
                sourceImages:(NSArray<FxImageTile *> *)sourceImages
            destinationImage:(FxImageTile *)destinationImage
                 pluginState:(NSData *)pluginState
                      atTime:(CMTime)renderTime
                       error:(NSError * _Nullable *)outError
{
    *destinationImageRect = sourceImages [ 0 ].imagePixelBounds;

    return YES;
}
```

For a more complicated filter that distorts or transforms the bounds, more has to be done to calculate the destination bounds. In this example from the `SimpleScale` class, found in the same sample project as FxDynamicRegistration, you first use the inverse pixel transform to convert the source image pixel bounds to document space. Then you calculate the new positions of the lower-left and upper-right corners of the image after processing, convert back to pixel space using the pixel transform, and then return the `destinationImageRect`.

**Swift**:

```swift
func destinationImageRect(_ destinationImageRect: UnsafeMutablePointer<FxRect>, sourceImages: [FxImageTile], destinationImage: FxImageTile, pluginState: Data?, at renderTime: CMTime) throws {

    let scale  = pluginState!.withUnsafeBytes { (ptr: UnsafePointer<Double>) -> Double in
        return ptr.pointee
    }
    
    var ll = FxPoint2D(x: Double(sourceImages[0].imagePixelBounds.left), y: Double(sourceImages[0].imagePixelBounds.bottom))
    var ur = FxPoint2D(x: Double(sourceImages[0].imagePixelBounds.right), y: Double(sourceImages[0].imagePixelBounds.top))
    
    // Convert from input pixel space to document space.
    ll = sourceImages[0].inversePixelTransform.transform2DPoint(ll)
    ur = sourceImages[0].inversePixelTransform.transform2DPoint(ur)
    
    // Subtract off the center.
    let imageCenter = FxPoint2D(x: (ll.x + ur.x) / 2.0, y: (ll.y + ur.y) / 2.0)
    ll = SubtractPoints(ll, imageCenter)
    ur = SubtractPoints(ur, imageCenter)
    
    // Perform the scaling.
    ll = MultiplyPointsByScalar(ll, scale)
    ur = MultiplyPointsByScalar(ur, scale)
    
    // Add back in the center.
    ll = AddPoints(ll, imageCenter)
    ur = AddPoints(ur, imageCenter)

    // Convert back to output pixel space.
    ll = destinationImage.pixelTransform.transform2DPoint(ll)
    ur = destinationImage.pixelTransform.transform2DPoint(ur)
    
    // Save to the output rectangle.
    destinationImageRect.pointee.left = Int32(floor(ll.x))
    destinationImageRect.pointee.right = Int32(ceil(ur.x))
    destinationImageRect.pointee.bottom = Int32(floor(ll.y))
    destinationImageRect.pointee.top = Int32(ceil(ur.y))
}
```

**Objective-C**:

```objc
- (BOOL)destinationImageRect:(FxRect *)destinationImageRect
                sourceImages:(NSArray<FxImageTile *> *)sourceImages
            destinationImage:(nonnull FxImageTile *)destinationImage
                 pluginState:(NSData *)pluginState
                      atTime:(CMTime)renderTime
                       error:(NSError * _Nullable *)outError
{
    double scale = 1.5;
    [pluginState getBytes:&scale
                   length:sizeof(scale)];
    
    FxPoint2D   ll  = { sourceImages [ 0 ].imagePixelBounds.left, sourceImages [ 0 ].imagePixelBounds.bottom };
    FxPoint2D   ur  = { sourceImages [ 0 ].imagePixelBounds.right, sourceImages [ 0 ].imagePixelBounds.top };
    
    // Convert from input pixel space to document space.
    ll = [sourceImages [ 0 ].inversePixelTransform transform2DPoint:ll];
    ur = [sourceImages [ 0 ].inversePixelTransform transform2DPoint:ur];
    
    // Subtract off the center.
    FxPoint2D   imageCenter = { (ll.x + ur.x) / 2.0, (ll.y + ur.y) / 2.0 };
    ll = SubtractPoints(ll, imageCenter);
    ur = SubtractPoints(ur, imageCenter);
    
    // Perform the scaling.
    ll = MultiplyPointsByScalar(ll, scale);
    ur = MultiplyPointsByScalar(ur, scale);
    
    // Add back in the center.
    ll = AddPoints(ll, imageCenter);
    ur = AddPoints(ur, imageCenter);
    
    // Convert back to output pixel space.
    ll = [destinationImage.pixelTransform transform2DPoint:ll];
    ur = [destinationImage.pixelTransform transform2DPoint:ur];

    // Save to the output rectangle.
    destinationImageRect->left = (SInt32)(floor(ll.x));
    destinationImageRect->right = (SInt32)(ceil(ur.x));
    destinationImageRect->bottom = (SInt32)(floor(ll.y));
    destinationImageRect->top = (SInt32)(ceil(ur.y));
    
    return YES;
}
```

##### Determine the source tile area required to render

Use the [`sourceTileRect(_:sourceImageIndex:sourceImages:destinationTileRect:destinationImage:pluginState:at:)`](../professional_video_applications/fxtileableeffect/sourcetilerect%28_,sourceimageindex,sourceimages,destinationtilerect,destinationimage,pluginstate,at%29.md) method to specify how much of the source image you require, given a known destination rectangle to render.

Your plug-in has one of the following three source rectangle requirements: no source rectangle definition necessary (a generator), a source rectangle that’s equal to the destination tile (a color filter), or a well-defined source rectangle (a distortion or convolution filter).

In this first example, `sourceTileRect` is set to [`kFxRect_Empty`](../professional_video_applications/kfxrect_empty.md) because generators typically don’t sample pixels from a source. This example comes from the FxGradientCheckerboard generator example plugin-in, where you don’t need any source to produce the checkerboard because you don’t need to sample or process any source pixels. This is the easiest case to handle.

**Swift**:

```swift
func sourceTileRect(_ sourceTileRect: UnsafeMutablePointer<FxRect>, sourceImageIndex: UInt, sourceImages: [FxImageTile], destinationTileRect: FxRect, destinationImage: FxImageTile, pluginState: Data?, at renderTime: CMTime) throws {
    sourceTileRect.pointee = kFxRect_Empty;
}
```

**Objective-C**:

```objc
- (BOOL)sourceTileRect:(FxRect *)sourceTileRect
      sourceImageIndex:(NSUInteger)sourceImageIndex
          sourceImages:(NSArray<FxImageTile *> *)sourceImages
   destinationTileRect:(FxRect)destinationTileRect
      destinationImage:(FxImageTile *)destinationImage
           pluginState:(NSData *)pluginState
                atTime:(CMTime)renderTime
                 error:(NSError * _Nullable *)outError
{
    *sourceTileRect = kFxRect_Empty;

    return YES;
}
```

This second example is from the DynamicRegBrightness filter in the FxDynamicRegistration example plug-in. In this case, the plug-in is simply filtering the color values of the source pixels and passing them back out, with a 1:1 pixel correspondence. Thus, the source pixels required are all contained within the destination tile.

**Swift**:

```swift
func sourceTileRect(_ sourceTileRect: UnsafeMutablePointer<FxRect>, sourceImageIndex: UInt, sourceImages: [FxImageTile], destinationTileRect: FxRect, destinationImage: FxImageTile, pluginState: Data?, at renderTime: CMTime) throws {
    sourceTileRect.pointee = destinationTileRect;
}
```

**Objective-C**:

```objc
- (BOOL)sourceTileRect:(FxRect *)sourceTileRect
      sourceImageIndex:(NSUInteger)sourceImageIndex
          sourceImages:(NSArray<FxImageTile *> *)sourceImages
   destinationTileRect:(FxRect)destinationTileRect
      destinationImage:(FxImageTile *)destinationImage
           pluginState:(NSData *)pluginState
                atTime:(CMTime)renderTime
                 error:(NSError * _Nullable *)outError
{
    *sourceTileRect = destinationTileRect;

    return YES;
}
```

In the final example of this method, look at the `SimpleScale` class, found in the same sample project as FxDynamicRegistration. The input method is far more complicated because it requires a well-defined source rectangle, and it’s using pixel transforms and a scale operation to show what it would look like to return a non-trivial `sourceTileRect`. Each step is commented and shows how the final bounds are determined.

**Swift**:

```swift
func sourceTileRect(_ sourceTileRect: UnsafeMutablePointer<FxRect>, sourceImageIndex: UInt, sourceImages: [FxImageTile], destinationTileRect: FxRect, destinationImage: FxImageTile, pluginState: Data?, at renderTime: CMTime) throws {
    let scale  = pluginState!.withUnsafeBytes { (ptr: UnsafePointer<Double>) -> Double in
        return ptr.pointee
    }
    
    // Get output pixel space coordinates.
    var ll = FxPoint2D(x: Double(destinationTileRect.left), y: Double(destinationTileRect.bottom))
    var ur = FxPoint2D(x: Double(destinationTileRect.right), y: Double(destinationTileRect.top))
    
    // Convert to document space.
    ll = destinationImage.inversePixelTransform.transform2DPoint(ll)
    ur = destinationImage.inversePixelTransform.transform2DPoint(ur)
    
    // Convert the whole output rectangle to document space.
    var oll = FxPoint2D(x: Double(destinationImage.imagePixelBounds.left), y: Double(destinationImage.imagePixelBounds.bottom))
    var our = FxPoint2D(x: Double(destinationImage.imagePixelBounds.right), y: Double(destinationImage.imagePixelBounds.top))
    oll = destinationImage.inversePixelTransform.transform2DPoint(oll)
    our = destinationImage.inversePixelTransform.transform2DPoint(our)

    // Subtract off the document space center.
    let documentSpaceCenter = FxPoint2D(x: (oll.x + our.x) / 2.0, y: (oll.y + our.y) / 2.0)
    ll = SubtractPoints(ll, documentSpaceCenter)
    ur = SubtractPoints(ur, documentSpaceCenter)
    
    // Scale appropriately.
    ll = MultiplyPointsByScalar(ll, 1.0 / scale)
    ur = MultiplyPointsByScalar(ur, 1.0 / scale)
    
    // Add in the document space center.
    ll = AddPoints(ll, documentSpaceCenter)
    ur = AddPoints(ur, documentSpaceCenter)
    
    // Convert to input pixel space.
    ll = sourceImages[0].pixelTransform.transform2DPoint(ll)
    ur = sourceImages[0].pixelTransform.transform2DPoint(ur)
    
    // Save it in the input tile rectangle.
    sourceTileRect.pointee.left = Int32(floor(ll.x))
    sourceTileRect.pointee.right = Int32(ceil(ur.x))
    sourceTileRect.pointee.bottom = Int32(floor(ll.y))
    sourceTileRect.pointee.top = Int32(ceil(ur.y))
}

private func AddPoints(_ a: FxPoint2D, _ b: FxPoint2D) -> FxPoint2D {
    let result = FxPoint2D(x: a.x + b.x, y: a.y + b.y)
    return result
}

private func SubtractPoints(_ a: FxPoint2D, _ b: FxPoint2D) -> FxPoint2D {
    let result = FxPoint2D(x: a.x - b.x, y: a.y - b.y)
    return result
}

private func MultiplyPointsByScalar(_ a: FxPoint2D, _ scalar: Double) -> FxPoint2D {
    let result = FxPoint2D(x: Double(a.x) * scalar, y: Double(a.y) * scalar)
    return result
}
```

**Objective-C**:

```objc
- (BOOL)sourceTileRect:(FxRect *)sourceTileRect
      sourceImageIndex:(NSUInteger)sourceImageIndex
          sourceImages:(NSArray<FxImageTile *> *)sourceImages
   destinationTileRect:(FxRect)destinationTileRect
      destinationImage:(FxImageTile *)destinationImage
           pluginState:(NSData *)pluginState
                atTime:(CMTime)renderTime
                 error:(NSError * _Nullable *)outError
{
    double scale = 1.5;
    [pluginState getBytes:&scale
                   length:sizeof(scale)];
    
    // Get output pixel space coordinates.
    FxPoint2D   ll = { destinationTileRect.left, destinationTileRect.bottom };
    FxPoint2D   ur = { destinationTileRect.right, destinationTileRect.top };
    
    // Convert to document space.
    ll = [destinationImage.inversePixelTransform transform2DPoint:ll];
    ur = [destinationImage.inversePixelTransform transform2DPoint:ur];
    
    // Convert the whole output rectangle to document space.
    FxPoint2D   oll = { destinationImage.imagePixelBounds.left, destinationImage.imagePixelBounds.bottom };
    FxPoint2D   our = { destinationImage.imagePixelBounds.right, destinationImage.imagePixelBounds.top };
    oll = [destinationImage.inversePixelTransform transform2DPoint:oll];
    our = [destinationImage.inversePixelTransform transform2DPoint:our];
    
    // Subtract off the document space center.
    FxPoint2D   documentSpaceCenter    = { (oll.x + our.x) / 2.0, (oll.y + our.y) / 2.0 };
    ll = SubtractPoints(ll, documentSpaceCenter);
    ur = SubtractPoints(ur, documentSpaceCenter);
    
    // Scale appropriately.
    ll = MultiplyPointsByScalar(ll, 1.0 / scale);
    ur = MultiplyPointsByScalar(ur, 1.0 / scale);
    
    // Add in the document space center.
    ll = AddPoints(ll, documentSpaceCenter);
    ur = AddPoints(ur, documentSpaceCenter);
    
    // Convert to input pixel space.
    ll = [sourceImages [ 0 ].pixelTransform transform2DPoint:ll];
    ur = [sourceImages [ 0 ].pixelTransform transform2DPoint:ur];
    
    // Save it in the input tile rectangle.
    sourceTileRect->left = floor(ll.x);
    sourceTileRect->right = ceil(ur.x);
    sourceTileRect->bottom = floor(ll.y);
    sourceTileRect->top = ceil(ur.y);
    
    return YES;
}

static FxPoint2D AddPoints(const FxPoint2D a, const FxPoint2D b)
{
    FxPoint2D   result = { a.x + b.x, a.y + b.y };
    return result;
}

static FxPoint2D SubtractPoints(const FxPoint2D a, const FxPoint2D b)
{
    FxPoint2D   result = { a.x - b.x, a.y - b.y };
    return result;
}

static FxPoint2D MultiplyPointsByScalar(const FxPoint2D a, const double scalar)
{
    FxPoint2D   result = { a.x * scalar, a.y * scalar };
    return result;
}
```

For a more sophisticated example of how to handle transformations, see the `SimpleScale` code sample in the `FxDynamicRegistration` sample project.

> ❗ **Important**:  Setting the [`kFxPropertyKey_NeedsFullBuffer`](../professional_video_applications/kfxpropertykey_needsfullbuffer.md) property key to `YES` indicates to the host that the plug-in requires the entire image to do its processing, and therefore the host won’t tile the input. Your plug-in may be unable to render large image inputs if tiling is not implemented.

## Topics

### Exchanging Image Tiles Between Host and Plug-in
- [class FxImageTile](../professional_video_applications/fximagetile.md)
  An image tile object that is passed between an out-of-process FxPlug plug-in and a host application.
- [class FxImageTileRequest](../professional_video_applications/fximagetilerequest.md)
  An image tile request object that is passed between an out-of-process FxPlug plug-in and a host application.

## See Also

### Rendering
- [Rendering in FxPlug](./rendering-in-fxplug.md)
  Use Metal or other frameworks to render images with your FxPlug plug-in.
- [Communicating with the plug-in state](./communicating-with-the-plug-in-state.md)
  Prepare the necessary information, such as parameter values, for your FxPlug plug-in to render.
- [Optimizing FxPlug plug-ins](./optimizing-fxplug-plug-ins.md)
  Maintain consistent rendering at all resolutions and aspect ratios by using pixel transforms.
- [protocol FxTileableEffect](../professional_video_applications/fxtileableeffect.md)
  The designated initializer for your plug-in for rendering only certain portions of the plug-in’s output, referred to as tiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/working-with-tiled-images)*