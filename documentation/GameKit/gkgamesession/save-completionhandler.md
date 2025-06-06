# save(_:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Saves the current game session data.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func save(_ data: Data, completionHandler: @escaping (Data?, (any Error)?) -> Void)
```

#### Discussion

The maximum amount of data to be saved is 512K. The `lastModifiedDate` and `lastModifiedPlayer` properties are updated upon completion. When a save conflict appears, the data is not saved to the server. The data property in the completion handler contains the information currently saved to the server. It is up to the developer to decide how to handle save conflicts.

## Parameters

- `data`: A   object containing the information to be saved.
- `completionHandler`: A block that is called after the data has been saved.

## See Also

- [func loadData(completionHandler: (Data?, (any Error)?) -> Void)](gkgamesession/loaddata(completionhandler:).md)
  Retrieves the game data from the current game session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesession/save(_:completionhandler:))*