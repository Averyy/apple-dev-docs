# init(exporting:)

**Framework**: Core Transferable  
**Kind**: init

Creates a transfer representation that’s exported by proxy through another transfer representation.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
init(exporting: @escaping (Item) async throws -> ProxyRepresentation)
```

## Parameters

- `exporting`: A closure that converts the item into   desired representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/proxyrepresentation/init(exporting:)-6gjdh)*