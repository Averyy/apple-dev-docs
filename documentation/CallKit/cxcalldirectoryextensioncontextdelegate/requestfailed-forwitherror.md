# requestFailed(for:withError:)

**Framework**: CallKit  
**Kind**: method  
**Required**: Yes

Called when a Call Directory app extension request fails.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+

## Declaration

```swift
func requestFailed(for extensionContext: CXCallDirectoryExtensionContext, withError error: any Error)
```

## Parameters

- `extensionContext`: The extension context associated with the failed request.
- `error`: An error object containing information about the request failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcalldirectoryextensioncontextdelegate/requestfailed(for:witherror:))*