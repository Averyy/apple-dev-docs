# Spotlight search tool

**Framework**: Core Spotlight

Make your app’s indexed content available to the system’s Foundation models as additional context to use when answering prompts.

#### Overview

Your app’s Spotlight search index provides fast access to your app’s content when you need to find something. The [`SpotlightSearchTool`](spotlightsearchtool.md) provides an efficient way for the Foundation Models framework to access the content in that index and use it to answer prompts. Include this tool in the Foundation Models session you use to run prompts that require your app’s custom content. Configure the search tool as needed to customize its behavior or the search behaviors.

## Topics

### Essentials
- [Making your indexed content available to Foundation Models](making-your-indexed-content-available-to-foundation-models.md)
  Make the content you index for Spotlight available to Foundation models to help generate responses to prompts.
- [Searching indexed content with natural language](searching-indexed-content-with-natural-language.md)
  Give a language model access to your app’s Core Spotlight index to enable natural-language queries over searchable content.
### Tool configuration
- [struct SpotlightSearchTool](spotlightsearchtool.md)
  A tool you use to make your app’s custom data available to Foundation Models.
- [SpotlightSearchTool.Configuration](spotlightsearchtool/configuration-swift.struct.md)
  The configuration data to use when creating a Spotlight search tool.
### Data sources
- [struct SearchSource](searchsource.md)
  A source of data for Spotlight to search.
- [struct CoreSpotlightSource](corespotlightsource.md)
  A search source that retrieves data from the app’s Spotlight index.
- [struct FileSource](filesource.md)
  A search source that retrieves indexed metadata from files and directories visible to Spotlight.
- [struct SearchableItemAttribute](searchableitemattribute.md)
  An attribute from a content item that the Spotlight search tool can include in search results.
### Tool customization
- [protocol CustomStage](customstage.md)
  A custom processing stage in a Spotlight search pipeline.
- [struct SearchPipelineData](searchpipelinedata.md)
  The value that flows between pipeline stages, carrying a typed payload.
- [enum SearchPipelineDataType](searchpipelinedatatype.md)
  Declares the kind of data a pipeline stage accepts or produces.
- [struct ScoredSearchableItem](scoredsearchableitem.md)
  A searchable item paired with a caller-assigned relevance score.
### Contact resolution
- [protocol ContactResolver](contactresolver.md)
  Resolves the current user’s identity for search queries involving people.
- [struct ResolvedContact](resolvedcontact.md)
  Contact information used to match person and organization references in search queries.
### Search results
- [struct SearchCount](searchcount.md)
  A scalar count result (e.g., “47 emails from John”).
- [struct SearchResultsTable](searchresultstable.md)
  Tabulated result data — rows with typed columns for display or spreadsheet export.
- [struct SearchStatistic](searchstatistic.md)
  A scalar statistic derived from search results (sum, average, max, min, median, stddev).
- [struct SearchTextResult](searchtextresult.md)
  LLM-generated text summary or analysis from a pipeline stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlight-search-tool)*