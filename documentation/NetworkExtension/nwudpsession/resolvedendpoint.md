# resolvedEndpoint

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The currently targeted remote endpoint.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_connection_copy_current_path(_:)`](../../Network/nw_connection_copy_current_path%28_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
var resolvedEndpoint: NWEndpoint? { get }
```

```objc
@property (nonatomic, readonly, nullable) NWEndpoint * resolvedEndpoint;
```

#### Discussion

Use Key-Value Observing (KVO) to watch this property.

## See Also

### Selecting remote endpoints
- [func tryNextResolvedEndpoint()](./trynextresolvedendpoint%28%29.md)
  Mark the current value of resolvedEndpoint as unusable, and try to switch to the next available endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwudpsession/resolvedendpoint)*