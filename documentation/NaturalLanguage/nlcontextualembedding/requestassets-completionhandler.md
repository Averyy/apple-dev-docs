# requestAssets(completionHandler:)

**Framework**: Natural Language  
**Kind**: method

Requests embedding model assets and downloads them if available.

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
func requestAssets() async throws -> NLContextualEmbedding.AssetsResult
```

#### Asynchronous Alternative

You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func requestAssets() async throws -> NLContextualEmbedding.AssetsResult
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

#### Discussion

You use a contextual embedding after loading the necessary assets onto the device. Use [`hasAvailableAssets`](nlcontextualembedding/hasavailableassets.md) to determine whether assets are available. This method returns immediately if the framework knows the state of the assets or if an error occurs.

## Parameters

- `completionHandler`: A closure that notifies your app when the asset request completes.

## See Also

- [NLContextualEmbedding.AssetsResult](nlcontextualembedding/assetsresult.md)
  The availability of the contextual embedding model assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlcontextualembedding/requestassets(completionhandler:))*