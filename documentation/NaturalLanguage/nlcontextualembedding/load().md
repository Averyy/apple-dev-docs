# load()

**Framework**: Natural Language  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) loadWithError:(NSError **) error;
```

#### Discussion

The method fails if the necessary assets aren’t on device for the model you specify. Use [`hasAvailableAssets`](./hasavailableassets.md) and [`requestAssets(completionHandler:)`](./requestassets%28completionhandler%29.md) to manage the assets.

## See Also

### Loading and unloading assets
- [func unload()](./unload%28%29.md)
  The instance method that unloads the embedding model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlcontextualembedding/load())*