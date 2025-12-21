# shouldFailClosed

**Framework**: Network Extension  
**Kind**: property

A Boolean value that determines how the filter behaves if it fails to make a filtering decision.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var shouldFailClosed: Bool { get set }
```

#### Discussion

If this value is `true`, the filter blocks URLs if the filter is enabled but failed to make any filtering decision. This can be the case when the filter encounters a communication failure with the PIR server. If the value is `false`, URLs are allowed even if the filter failed to make a filtering decision.

This value defaults to `false`.

## See Also

- [var isEnabled: Bool](neurlfiltermanager/isenabled.md)
  A Boolean value that toggles the enabled status of the URL filter.
- [var prefilterFetchInterval: TimeInterval](neurlfiltermanager/prefilterfetchinterval.md)
  The time interval at which the the filter control provider app extension runs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/shouldfailclosed)*