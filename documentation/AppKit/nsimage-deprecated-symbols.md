# Deprecated symbols

**Framework**: AppKit  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

## Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated class methods
- [class func imageFileTypes() -> [String]](./nsimage/imagefiletypes%28%29.md)
  Returns an array of strings identifying the image types supported by the registered image representation objects.
- [class func imageUnfilteredFileTypes() -> [String]](./nsimage/imageunfilteredfiletypes%28%29.md)
  Returns an array of strings identifying the file types supported directly by the registered image representation objects.
- [class func imagePasteboardTypes() -> [NSPasteboard.PasteboardType]](./nsimage/imagepasteboardtypes%28%29.md)
  Returns an array of strings identifying the pasteboard types supported directly by the registered image representation objects.
- [class func imageUnfilteredPasteboardTypes() -> [NSPasteboard.PasteboardType]](./nsimage/imageunfilteredpasteboardtypes%28%29.md)
  Returns an array of strings identifying the pasteboard types supported directly by the registered image representation objects.
### Deprecated instance methods
- [func lockFocus()](./nsimage/lockfocus%28%29.md)
  Prepares the image to receive drawing commands.
- [func lockFocusFlipped(Bool)](./nsimage/lockfocusflipped%28_%29.md)
  Prepares the image to receive drawing commands using the specified flipped state.
- [func unlockFocus()](./nsimage/unlockfocus%28%29.md)
  Removes the focus from the image.
- [convenience init(iconRef: IconRef)](./nsimage/init%28iconref%29.md)
  Initializes the image object with a Carbon-style icon resource.
- [- lockFocusOnRepresentation:](./nsimage/lockfocusonrepresentation_.md)
  Prepares the specified image representation to receive drawing commands.
- [- bestRepresentationForDevice:](./nsimage/bestrepresentationfordevice_.md)
  Returns the best representation for the device with the specified characteristics.
- [- compositeToPoint:operation:](./nsimage/compositetopoint_operation_.md)
  Composites the entire image to the specified point in the current coordinate system.
- [- compositeToPoint:fromRect:operation:](./nsimage/compositetopoint_fromrect_operation_.md)
  Composites a portion of the image to the specified point in the current coordinate system.
- [- compositeToPoint:fromRect:operation:fraction:](./nsimage/compositetopoint_fromrect_operation_fraction_.md)
  Composites a portion of the image at the specified opacity to the current coordinate system.
- [- compositeToPoint:operation:fraction:](./nsimage/compositetopoint_operation_fraction_.md)
  Composites the entire image at the specified opacity in the current coordinate system.
- [- dissolveToPoint:fraction:](./nsimage/dissolvetopoint_fraction_.md)
  Composites the entire image to the specified location using the source-over operator.
- [- dissolveToPoint:fromRect:fraction:](./nsimage/dissolvetopoint_fromrect_fraction_.md)
  Composites a portion of the image to the specified location using the source-over operator.
- [- setScalesWhenResized:](./nsimage/setscaleswhenresized_.md)
  Sets whether to scale different-sized image representations to fit the image’s size.
- [- scalesWhenResized](./nsimage/scaleswhenresized.md)
  Returns a Boolean value that indicates whether to scale image representations to fit the image’s size.
- [- setDataRetained:](./nsimage/setdataretained_.md)
  Sets whether the image retains its source image data.
- [- isDataRetained](./nsimage/isdataretained.md)
  Returns a Boolean value that incidates whether the image retains its source image data.
- [- setCachedSeparately:](./nsimage/setcachedseparately_.md)
  Sets whether each image representation uses a separate offscreen window to cache its contents.
- [- isCachedSeparately](./nsimage/iscachedseparately.md)
  Returns a Boolean value that indicates whether each image representation caches its contents in a separate offscreen window.
- [- setCacheDepthMatchesImageDepth:](./nsimage/setcachedepthmatchesimagedepth_.md)
  Sets whether the image’s offscreen window caches use the same bit depth as the image data itself.
- [- cacheDepthMatchesImageDepth](./nsimage/cachedepthmatchesimagedepth.md)
  Returns a Boolean value that indicates whether an image’s offscreen window caches use the same bit depth as the image data itself.
- [- setFlipped:](./nsimage/setflipped_.md)
  Sets whether the polarity of the y axis is inverted when drawing an image.
- [- isFlipped](./nsimage/isflipped.md)
  Returns a Boolean value that indicates whether the image uses a flipped coordinate system.
### Deprecated methods
- [- cancelIncrementalLoad](./nsimage/cancelincrementalload.md)
  Cancels the current download operation, if any, for an incrementally loaded image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage-deprecated-symbols)*