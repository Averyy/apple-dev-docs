# SpotlightSearchTool

**Framework**: Core Spotlight  
**Kind**: struct

A tool you use to make your app’s custom data available to Foundation Models.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct SpotlightSearchTool
```

## Mentions

- [Making your indexed content available to Foundation Models](making-your-indexed-content-available-to-foundation-models.md)

#### Overview

The `SpotlightSearchTool` type implements the protocol that Foundation Models use to run custom tools when resolving prompts. If you implement intelligent features using the Foundation Models framework, you can use this tool to provide your app’s data to the model as additional contextual information. The model can use this additional data to answer questions specific to your app’s content. For example, a note-taking app that runs the prompt “Find my meeting notes from last Tuesday” can use this tool to make its notes available to the model.

Create an instance of `SpotlightSearchTool` before configuring a [`LanguageModelSession`](https://developer.apple.com/documentation/FoundationModels/LanguageModelSession) object to run prompts. Configure the tool with the sources and options you want to use to search your particular content. For example, you can direct the tool to search your app’s Spotlight index, files and directories your app created, or both. Use the tool options to offer guidance on how to perform searches efficiently on your content. The following example shows you how to create and configure this tool with a custom source.

```swift
import CoreSpotlight
import FoundationModels

// Search the app’s Spotlight index and fetch specific attributes for each result.
var csSource = CoreSpotlightSource(fetchAttributes: [.subject, .authorNames, .contentDescription])
csSource.sourceOptions = [.allowMail]
csSource.maximumResultCount = 20

// Create and configure the search tool.
let configuration = SpotlightSearchTool.Configuration(sources: [coreSpotlight(csSource)])
let tool = SpotlightSearchTool(configuration: configuration)

// Set up the Foundation Models session and run a prompt.
let session = LanguageModelSession(tools: [tool])
let response = try await session.respond(to: "Find my notes about the project deadline")
```

## Topics

### Creating the search tool
- [init(configuration: SpotlightSearchTool.Configuration)](spotlightsearchtool/init(configuration:).md)
### Configuring the tool behavior
- [let configuration: SpotlightSearchTool.Configuration](spotlightsearchtool/configuration-swift.property.md)
  The configuration details for the search tool.
- [SpotlightSearchTool.Configuration](spotlightsearchtool/configuration-swift.struct.md)
  The configuration data to use when creating a Spotlight search tool.
- [SpotlightSearchTool.Guide](spotlightsearchtool/guide.md)
  A type you use to offer guidance about what search capabillities to employ during a session.
- [SpotlightSearchTool.GuidanceProfile](spotlightsearchtool/guidanceprofile.md)
  Options for which techniques to use to determine a match.
- [SpotlightSearchTool.GuidanceLevel](spotlightsearchtool/guidancelevel.md)
  Options for how to search your app’s content.
- [SpotlightSearchTool.ContentDomain](spotlightsearchtool/contentdomain.md)
  A content domain that defines which fields and attribute mappings are presented to the model during a focused search session.
- [SpotlightSearchTool.FormatLevel](spotlightsearchtool/formatlevel.md)
  Controls how tool responses are serialized for the model’s context window.
### Getting the search results
- [var searchResults: some AsyncSequence<SpotlightSearchTool.SearchReply, Never>](spotlightsearchtool/searchresults.md)
  An asynchronous stream that delivers the results of a search to your app for processing.
- [SpotlightSearchTool.SearchReply](spotlightsearchtool/searchreply.md)
  A set of search results with routing metadata for host app consumption.
### Getting tool-specific properties
- [var parameters: GenerationSchema](spotlightsearchtool/parameters.md)
  Dynamic schema: use the native tool’s schema based on capabilities.
- [var includesSchemaInInstructions: Bool](spotlightsearchtool/includesschemaininstructions.md)
  On-device uses includesSchemaInInstructions: true; .dynamic uses false (schema in compact notation prose instead).
### Type Aliases
- [SpotlightSearchTool.Arguments](spotlightsearchtool/arguments.md)
  The overlay tool uses GeneratedContent as its Arguments type so the full native schema (FullArguments or RAGSearchArguments) passes through to NativeSpotlightSearchTool without re-encoding.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Tool](../FoundationModels/Tool.md)

## See Also

- [SpotlightSearchTool.Configuration](spotlightsearchtool/configuration-swift.struct.md)
  The configuration data to use when creating a Spotlight search tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool)*