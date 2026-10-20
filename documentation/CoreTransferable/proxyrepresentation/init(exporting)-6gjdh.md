# init(exporting:)

**Framework**: Core Transferable  
**Kind**: init  
**Role**: Initializer

Creates a transfer representation that’s exported by proxy through another transfer representation.

**Availability**:
- iOS 16.1+ - Deprecated in 17.0
- iPadOS 16.1+ - Deprecated in 17.0
- Mac Catalyst 16.1+ - Deprecated in 17.0
- macOS 13.0+ - Deprecated in 14.0
- tvOS 16.1+ - Deprecated in 17.0
- visionOS 1.0+
- watchOS 9.1+ - Deprecated in 10.0

> **Deprecated**: A synchronous exporter should be used instead.

## Declaration

```swift
init(exporting: @escaping @Sendable (Item) async throws -> ProxyRepresentation)
```

## Parameters

- `exporting`: A closure that converts the item into desired representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/proxyrepresentation/init(exporting:)-6gjdh)*