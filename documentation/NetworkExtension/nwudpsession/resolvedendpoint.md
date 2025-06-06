# resolvedEndpoint

**Framework**: Network Extension  
**Kind**: property

The currently targeted remote endpoint.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var resolvedEndpoint: NWEndpoint? { get }
```

#### Discussion

Use Key-Value Observing (KVO) to watch this property.

## See Also

- [func tryNextResolvedEndpoint()](nwudpsession/trynextresolvedendpoint.md)
  Mark the current value of resolvedEndpoint as unusable, and try to switch to the next available endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwudpsession/resolvedendpoint)*