# requestAssets(completionHandler:)

**Framework**: Natural Language  
**Kind**: method

Requests assets for an embedding, if available.

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

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func requestAssets() async throws -> NLContextualEmbedding.AssetsResult
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func requestAssets() async throws -> NLContextualEmbedding.AssetsResult
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

You use a contextual embedding after loading the necessary assets onto the device. Use [`hasAvailableAssets`](nlcontextualembedding/hasavailableassets.md) to determine whether assets are available.

This method returns immediately if the framework knows the state of the assets or if an error occurs.

## Parameters

- `completionHandler`: A completion handler the system calls after it finishes the request.

## See Also

- [NLContextualEmbedding.AssetsResult](nlcontextualembedding/assetsresult.md)
  The status of an asset request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlcontextualembedding/requestassets(completionhandler:))*