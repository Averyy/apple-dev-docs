# captureImage(in:completionHandler:)

**Framework**: ScreenCaptureKit  
**Kind**: method

**Availability**:
- Mac Catalyst 18.2+
- macOS 15.2+

## Declaration

```swift
class func captureImage(in rect: CGRect) async throws -> CGImage
```

#### Discussion

captureImageInRect:completionHandler:

this method returns an image containing the contents of the rectangle in points, specified in display space

## Parameters

- `rect`: The rect for the region in points on the screen space for the screen shot, this is display agnostic and supports multiple displays
- `completionHandler`: Is the handler that will deliver the screenshot to the client


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scscreenshotmanager/captureimage(in:completionhandler:))*