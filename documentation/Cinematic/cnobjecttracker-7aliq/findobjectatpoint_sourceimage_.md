# findObjectAtPoint:sourceImage:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Instance Method

Finds the bounds of an object at the given point.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
- (CNBoundsPrediction *) findObjectAtPoint:(CGPoint) point sourceImage:(CVPixelBufferRef) sourceImage;
```

## Return Value

A prediction, which includes bounds that can be used to start tracking, or `nil` if no discernible object is detected.

## Discussion

Used to convert a normalized point in an image to a rectangle used to start tracking.

## Parameters

- `point`: The point of interest.
- `sourceImage`: The image buffer containing the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnobjecttracker-7aliq/findobjectatpoint:sourceimage:)*