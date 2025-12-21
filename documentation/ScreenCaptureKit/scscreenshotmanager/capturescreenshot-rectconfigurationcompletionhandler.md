# captureScreenshot(rect:configuration:completionHandler:)

**Framework**: ScreenCaptureKit  
**Kind**: method

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
class func captureScreenshot(rect: CGRect, configuration config: SCScreenshotConfiguration) async throws -> SCScreenshotOutput
```

#### Discussion

captureScreenshotWithRect:configuration:completionHandler:

this method returns an SCScreenshotOutput object containing CGImages of the screenshot requested by the client

## Parameters

- `rect`: The rect for the region in points on the screen space for the screen shot, this is display agnostic and supports multiple displays
- `config`: Is the screenshot configuration containing information on how to format the screenshot
- `completionHandler`: Is the handler that will deliver the SCScreenshotOutput object to the client


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scscreenshotmanager/capturescreenshot(rect:configuration:completionhandler:))*