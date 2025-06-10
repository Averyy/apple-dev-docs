# stop(reason:)

**Framework**: Network Extension  
**Kind**: method  
**Required**: Yes

Prepares the filter to stop, in response to a call from the framework.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
func stop(reason: NEProviderStopReason) async throws
```

#### Discussion

Override this method in your conformance to [`NEURLFilterControlProvider`](neurlfiltercontrolprovider.md) and perform whatever steps are necessary to prepare for the URL filter stopping.

## Parameters

- `reason`: An   that indicates why the framework is stopping the filter.

## See Also

- [func start() async throws](neurlfiltercontrolprovider/start.md)
  Prepares the filter to start, in response to a call from the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltercontrolprovider/stop(reason:))*