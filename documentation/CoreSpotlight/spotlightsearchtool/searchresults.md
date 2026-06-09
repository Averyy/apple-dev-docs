# searchResults

**Framework**: Core Spotlight  
**Kind**: property

An asynchronous stream that delivers the results of a search to your app for processing.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var searchResults: some AsyncSequence<SpotlightSearchTool.SearchReply, Never> { get }
```

## Mentions

- [Making your indexed content available to Foundation Models](making-your-indexed-content-available-to-foundation-models.md)

#### Discussion

Use this property to monitor the search results as the tool generates them. Each time the model calls the Spotlight search tool’s [`call(arguments:)`](https://developer.apple.com/documentation/FoundationModels/Tool/call(arguments:)) method, the tool generates one or more [`SpotlightSearchTool.SearchReply`](spotlightsearchtool/searchreply.md) structures with information about the results. Use this information to track the tool’s behavior while responding to the model’s requests.

Monitor the asynchronous stream using a `for await` loop in a separate task, as shown in the following example:

```swift
let tool = SpotlightSearchTool()
let session = LanguageModelSession(tools: [tool])

Task {
    for await result in tool.searchResults {
        // Process each search result as it arrives.
    }
}

let response = try await session.respond(to: "Show me recent emails from Shelly”)
```

For more information about how to process search results, see [`Making your indexed content available to Foundation Models`](making-your-indexed-content-available-to-foundation-models.md).

## See Also

- [SpotlightSearchTool.SearchReply](spotlightsearchtool/searchreply.md)
  A set of search results with routing metadata for host app consumption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/searchresults)*