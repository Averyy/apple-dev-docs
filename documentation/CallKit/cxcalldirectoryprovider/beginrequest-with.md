# beginRequest(with:)

**Framework**: CallKit  
**Kind**: method

Tells the extension to prepare for a host app’s request.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+

## Declaration

```swift
func beginRequest(with context: CXCallDirectoryExtensionContext)
```

## Mentions

- [Identifying and blocking calls](identifying-and-blocking-calls.md)

#### Discussion

An extension prepares for a host app’s request by getting the context passed in this method and requesting related data items, if appropriate. This method is received after the extension is initialized, but before the principal object is asked to do anything with the context.

## Parameters

- `context`: A   object that represents the context in which the host app makes the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcalldirectoryprovider/beginrequest(with:))*