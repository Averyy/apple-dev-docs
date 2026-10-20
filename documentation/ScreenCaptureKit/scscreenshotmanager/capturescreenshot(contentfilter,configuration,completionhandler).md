# captureScreenshot(contentFilter:configuration:completionHandler:)

**Framework**: ScreenCaptureKit  
**Kind**: method  
**Role**: Type Method

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
class func captureScreenshot(contentFilter: SCContentFilter, configuration config: SCScreenshotConfiguration, completionHandler: (@Sendable (SCScreenshotOutput?, (any Error)?) -> Void)? = nil)
```

```swift
class func captureScreenshot(contentFilter: SCContentFilter, configuration config: SCScreenshotConfiguration) async throws -> SCScreenshotOutput
```

```objc
+ (void) captureScreenshotWithFilter:(SCContentFilter *) contentFilter configuration:(SCScreenshotConfiguration *) config completionHandler:(void (^)(SCScreenshotOutput *output, NSError *error)) completionHandler;
```

#### Discussion

captureScreenshotWithFilter:configuration:completionHandler:

this method returns an SCScreenshotOutput object containing CGImages of the screenshot requested by the client

## Parameters

- `contentFilter`: Is the filter containing the content to take a screenshot of
- `config`: Is the screenshot configuration containing information on how to format the screenshot
- `completionHandler`: Is the handler that will deliver the SCScreenshotOutput object to the client


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scscreenshotmanager/capturescreenshot(contentfilter:configuration:completionhandler:))*