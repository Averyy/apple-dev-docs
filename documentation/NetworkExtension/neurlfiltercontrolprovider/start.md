# start()

**Framework**: Network Extension  
**Kind**: method  
**Required**: Yes

Prepares the filter to start, in response to a call from the framework.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
func start() async throws
```

#### Discussion

Override this method in your conformance to [`NEURLFilterControlProvider`](neurlfiltercontrolprovider.md) and perform whatever steps are necessary to prepare for fetching pre-filter data.

## See Also

- [func stop(reason: NEProviderStopReason) async throws](neurlfiltercontrolprovider/stop(reason:).md)
  Prepares the filter to stop, in response to a call from the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltercontrolprovider/start())*