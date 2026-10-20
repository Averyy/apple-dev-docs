# isEqual(to:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Comparison method for [`NWPath`](../nwpath.md) objects.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_path_is_equal(_:_:)`](../../Network/nw_path_is_equal%28_,_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
func isEqual(to path: NWPath) -> Bool
```

```objc
- (BOOL) isEqualToPath:(NWPath *) path;
```

#### Discussion

Returns [`true`](../../Swift/true.md) if the objects are equal, [`false`](../../Swift/false.md) otherwise. If two [`NWPath`](../nwpath.md) objects are equal, this means that the underlying network configuration (routes, interfaces, address, etc.) are the same between them.

## Parameters

- `path`: Another [`NWPath`](../nwpath.md) object to compare.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwpath/isequal(to:))*