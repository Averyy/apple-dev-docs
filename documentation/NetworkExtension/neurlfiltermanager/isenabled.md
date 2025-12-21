# isEnabled

**Framework**: Network Extension  
**Kind**: property

A Boolean value that toggles the enabled status of the URL filter.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

#### Discussion

If this value is `true`, the URL filter starts filtering URLs. If `false`, the filter stops filtering.

This value defaults to `false`.

## See Also

- [var shouldFailClosed: Bool](neurlfiltermanager/shouldfailclosed.md)
  A Boolean value that determines how the filter behaves if it fails to make a filtering decision.
- [var prefilterFetchInterval: TimeInterval](neurlfiltermanager/prefilterfetchinterval.md)
  The time interval at which the the filter control provider app extension runs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/isenabled)*