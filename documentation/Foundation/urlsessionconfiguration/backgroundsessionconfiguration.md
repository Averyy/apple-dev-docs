# backgroundSessionConfiguration(_:)

**Framework**: Foundation  
**Kind**: method

Returns a session configuration object that allows HTTP and HTTPS uploads or downloads to be performed in the background.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func backgroundSessionConfiguration(_ identifier: String) -> URLSessionConfiguration
```

#### Return Value

A URL session configuration object that causes upload and download tasks to be performed by the system in a separate process.

## Parameters

- `identifier`: The unique identifier for the configuration object. This parameter must not be   or an empty string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/backgroundsessionconfiguration(_:))*