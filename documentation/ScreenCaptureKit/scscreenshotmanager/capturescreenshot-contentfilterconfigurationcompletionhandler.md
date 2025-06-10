# captureScreenshot(contentFilter:configuration:completionHandler:)

**Framework**: ScreenCaptureKit  
**Kind**: method

**Availability**:
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
class func captureScreenshot(contentFilter: SCContentFilter, configuration config: SCScreenshotConfiguration) async throws -> SCScreenshotOutput
```

#### Discussion

This method returns an SCScreenshotOutput object containing CGImages of the screenshot requested by the client

## Parameters

- `contentFilter`: Is the filter containing the content to take a screenshot of
- `config`: Is the screenshot configuration containing information on how to format the screenshot
- `completionHandler`: Is the handler that will deliver the SCScreenshotOutput object to the client


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scscreenshotmanager/capturescreenshot(contentfilter:configuration:completionhandler:))*