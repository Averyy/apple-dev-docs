# init(exporting:importing:)

**Framework**: Core Transferable  
**Kind**: init

Creates a transfer representation that’s imported and exported by proxy through another transfer representation.

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
init(exporting: @escaping (Item) async throws -> ProxyRepresentation, importing: @escaping (ProxyRepresentation) async throws -> Item)
```

## Parameters

- `exporting`: A closure that converts the item into   desired representation.
- `importing`: A closure that converts the chosen representation   back into the transported item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/proxyrepresentation/init(exporting:importing:)-8q8zv)*