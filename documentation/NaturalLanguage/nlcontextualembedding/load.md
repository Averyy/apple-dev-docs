# load()

**Framework**: Natural Language  
**Kind**: method

Loads the embedding model.

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

When you create a contextual embedding, the model isn’t loaded until you need it, by default. Use [`load()`](nlcontextualembedding/load().md) and [`unload()`](nlcontextualembedding/unload().md) to control when to load and unload the model.

The method fails if the necessary assets — for the model you specify — aren’t on device. Use [`hasAvailableAssets`](nlcontextualembedding/hasavailableassets.md) and [`requestAssets(completionHandler:)`](nlcontextualembedding/requestassets(completionhandler:).md) to manage the assets.

## See Also

- [func unload()](nlcontextualembedding/unload.md)
  Unloads the embedding model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlcontextualembedding/load())*