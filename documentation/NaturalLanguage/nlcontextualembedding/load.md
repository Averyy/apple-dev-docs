# load()

**Framework**: Natural Language  
**Kind**: method

The instance method that loads the embedding model.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func load() throws
```

#### Discussion

The method fails if the necessary assets aren’t on device for the model you specify. Use [`hasAvailableAssets`](nlcontextualembedding/hasavailableassets.md) and [`requestAssets(completionHandler:)`](nlcontextualembedding/requestassets(completionhandler:).md) to manage the assets.

## See Also

- [func unload()](nlcontextualembedding/unload.md)
  The instance method that unloads the embedding model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlcontextualembedding/load())*