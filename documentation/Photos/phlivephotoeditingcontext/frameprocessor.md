# frameProcessor

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A block to be called by Photos for processing each frame of the Live Photo’s visual content.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var frameProcessor: PHLivePhotoFrameProcessingBlock? { get set }
```

```objc
@property (copy, nullable) PHLivePhotoFrameProcessingBlock frameProcessor;
```

#### Discussion

Use this property to define the image processing to be performed on each frame of the Live Photo. Setting this property does not begin processing; instead, after you call one of the methods listed in Processing an Editing Context’s Live Photo, Photos executes your block repeatedly to process each frame of the Live Photo’s video and still photo content.

In your frame processor block, use the [`image`](../phlivephotoframe/image.md) property of the provided [`PHLivePhotoFrame`](../phlivephotoframe.md) object to access the image to be processed, and return a [`CIImage`](../../CoreImage/ciimage.md) object representing the result of your processing. For example, the following code sets up a processor block to apply a simple sepia-tone filter, then calls the [`saveLivePhoto(to:options:completionHandler:)`](./savelivephoto%28to,options,completionhandler%29.md) method to begin processing the Live Photo for output.

**Swift**:

```swift
 
func processLivePhoto(input: PHContentEditingInput) {
    guard let context = PHLivePhotoEditingContext(livePhotoEditingInput: input)
        else { fatalError("not a Live Photo editing input") }
    context.frameProcessor = { frame, _ in
        return frame.image.applyingFilter("CISepiaTone", withInputParameters: nil)
    }
    let output = PHContentEditingOutput(contentEditingInput: input)
    context.saveLivePhoto(to: output) { success, error in
        if success {
            // use output with PHAssetChangeRequest or PHContentEditingController
        } else {
            print("can't process live photo: \(error)")
        }
    }
}
```

**Objective-C**:

```objc
 
- (void)processLivePhoto:(PHContentEditingInput *)input {
    PHLivePhotoEditingContext *context = [[PHLivePhotoEditingContext alloc] initWithLivePhotoEditingInput:input];
    context.frameProcessor = ^CIImage *(id <PHLivePhotoFrame> frame, NSError **error) {
        return [frame.image imageByApplyingFilter:@"CISepiaTone" withInputParameters:nil];
    }
    PHContentEditingOutput *output = [[PHContentEditingOutput alloc] initWithContentEditingInput: input];
    [context saveLivePhotoToOutput:output options:nil completionHandler:^(PHLivePhoto *livePhoto, NSError *error) {
        if (success) {
            // use output with PHAssetChangeRequest or PHContentEditingController
        } else {
            NSLog(@"can't process: %@", error);
        }
    ];
}
```

## See Also

### Preparing an Editing Context for Processing
- [typealias PHLivePhotoFrameProcessingBlock](../phlivephotoframeprocessingblock.md)
  The signature for a block Photos calls to process Live Photo frames.
- [var audioVolume: Float](./audiovolume.md)
  The audio gain to apply to the processed Live Photo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephotoeditingcontext/frameprocessor)*