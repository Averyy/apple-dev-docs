# isEqual(to:)

**Framework**: Network Extension  
**Kind**: method

Comparison method for [`NWPath`](nwpath.md) objects.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func isEqual(to path: NWPath) -> Bool
```

#### Discussion

Returns [`true`](https://developer.apple.com/documentation/Swift/true) if the objects are equal, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise. If two [`NWPath`](nwpath.md) objects are equal, this means that the underlying network configuration (routes, interfaces, address, etc.) are the same between them.

## Parameters

- `path`: Another   object to compare.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwpath/isequal(to:))*