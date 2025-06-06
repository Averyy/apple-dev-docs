# init(importing:)

**Framework**: Core Transferable  
**Kind**: init

Creates a transfer representation that’s imported by proxy through another transfer representation.

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
init(importing: @escaping (ProxyRepresentation) throws -> Item)
```

## Parameters

- `importing`: A closure that converts the chosen representation into   the transported item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/proxyrepresentation/init(importing:)-pq40)*