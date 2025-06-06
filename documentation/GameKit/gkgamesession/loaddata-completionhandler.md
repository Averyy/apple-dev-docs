# loadData(completionHandler:)

**Framework**: GameKit  
**Kind**: method

Retrieves the game data from the current game session.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func loadData() async throws -> Data
```

## Parameters

- `completionHandler`: A block that is called after the game session data has been loaded.

## See Also

- [func save(Data, completionHandler: (Data?, (any Error)?) -> Void)](gkgamesession/save(_:completionhandler:).md)
  Saves the current game session data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesession/loaddata(completionhandler:))*