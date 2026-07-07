# prefilterFetchInterval

**Framework**: Network Extension  
**Kind**: property

The time interval at which the the filter control provider app extension runs.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var prefilterFetchInterval: TimeInterval { get set }
```

#### Discussion

This value determines how frequently the [`NEURLFilterControlProvider`](neurlfiltercontrolprovider.md) can download prefilter Bloom filter data on to the device. Your implementation should allow some slight deviation between the scheduled time and the actual execution of the fetch.

This value defaults to `86400` seconds, which is one day. The minimum value allowed is `2700` seconds (45 minutes).

## See Also

- [var isEnabled: Bool](neurlfiltermanager/isenabled.md)
  A Boolean value that toggles the enabled status of the URL filter.
- [var shouldFailClosed: Bool](neurlfiltermanager/shouldfailclosed.md)
  A Boolean value that determines how the filter behaves if it fails to make a filtering decision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/prefilterfetchinterval)*