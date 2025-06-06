# init(exporting:)

**Framework**: Core Transferable  
**Kind**: init

Creates a transfer representation that’s exported by proxy through another transfer representation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(exporting: @escaping (Item) throws -> ProxyRepresentation)
```

## Parameters

- `exporting`: A closure that converts the item into   desired representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/proxyrepresentation/init(exporting:)-q3qp)*