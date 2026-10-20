# fetchHistory(during:completionHandler:)

**Framework**: Screen Time  
**Kind**: method

Fetches web history that occurred during the date interval you specify.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+

## Declaration

```swift
func fetchHistory(during interval: DateInterval) async throws -> Set<URL>
```

## Parameters

- `interval`: The date interval of web history you want to fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screentime/stwebhistory/fetchhistory(during:completionhandler:))*