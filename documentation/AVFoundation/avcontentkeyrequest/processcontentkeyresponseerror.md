# processContentKeyResponseError(_:)

**Framework**: AVFoundation  
**Kind**: method

Tells the receiver that the app was unable to obtain a content key response.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- macOS 10.12.4+
- tvOS 10.2+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func processContentKeyResponseError(_ error: any Error)
```

## Parameters

- `error`: An   that describes why the content key response failed.

## See Also

- [func processContentKeyResponse(AVContentKeyResponse)](avcontentkeyrequest/processcontentkeyresponse(_:).md)
  Sends the specified content key response to the receiver for processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/processcontentkeyresponseerror(_:))*