# tryNextResolvedEndpoint()

**Framework**: Network Extension  
**Kind**: method

Mark the current value of resolvedEndpoint as unusable, and try to switch to the next available endpoint.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func tryNextResolvedEndpoint()
```

#### Discussion

This should be used when the caller has attempted to communicate with the current `resolvedEndpoint`, and the caller has determined that it is unusable. If there are no other resolved endpoints, the session will move to the failed state.

## See Also

- [var resolvedEndpoint: NWEndpoint?](nwudpsession/resolvedendpoint.md)
  The currently targeted remote endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwudpsession/trynextresolvedendpoint())*