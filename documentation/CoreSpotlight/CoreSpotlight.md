# Core Spotlight

**Framework**: Core Spotlight  
**Kind**: module

Add search capabilities to your app, and index your content so people can find it from Spotlight and Safari.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- visionOS 1.0+

#### Overview

Help people access activities and items within your app by adding details about those items to a Core Spotlight index. The framework provides APIs to add your content to an index, and search for items in that index. You decide what content makes sense to index, but typically you index anything that someone might look for in your app. For example, you might index photos, contacts, the items someone purchased, or data they see in your interface. You can then use Core Spotlight to search for your indexed content and display those results in your app.

Your app is responsible for indexing your app’s content and maintaining those indexes. You can index content when your app runs, or provide an app extension to index content when the system requests it. You can index any content your app manages, including files and other content that your app isn’t currently displaying. The indexes you create using Core Spotlight remain on device, and are private to the owner of the device. Devices don’t share indexed data with Apple, or synchronize that data with the person’s other devices.

In addition to indexing content, iOS provides additional strategies for making your app’s content searchable:

- Use the search-related properties of [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) to add items to the on-device index, with the option to identify the items as eligible for public indexing. Learn more about [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) in [`Index Activities and Navigation Points`](https://developer.apple.comhttps://developer.apple.com/library/content/documentation/General/Conceptual/AppSearch/Activities.html#//apple_ref/doc/uid/TP40016308-CH6-SW1).
- Use web markup to index content on your web server in Apple’s server-side index, which makes the data available to all iOS users in Spotlight and Safari search results. For more information, see [`Mark Up Web Content`](https://developer.apple.comhttps://developer.apple.com/library/content/documentation/General/Conceptual/AppSearch/WebContent.html#//apple_ref/doc/uid/TP40016308-CH8-SW1) in [`App Search Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/content/documentation/General/Conceptual/AppSearch/index.html).

## Topics

### Essentials
- [Adding your app’s content to Spotlight indexes](adding-your-app-s-content-to-spotlight-indexes.md)
  Create a description for your app’s content and add it to a Spotlight index to make it searchable.
- [Enabling Apple Intelligence summarization and prioritization](enable-apple-intelligence-summaries.md)
  Summarize and prioritize app content using Spotlight extensions.
### Searchable items
- [class CSSearchableItem](cssearchableitem.md)
  The details of your app-specific content that someone might search for on their devices.
- [class CSSearchableItemAttributeSet](cssearchableitemattributeset.md)
  The detailed metadata for a searchable item.
- [class CSCustomAttributeKey](cscustomattributekey.md)
  A key associated with a custom attribute for a searchable item.
- [class CSLocalizedString](cslocalizedstring.md)
  An object that displays localized text in search results related to your app.
- [class CSPerson](csperson.md)
  An object that represents a person in the context of search results.
### Indexes
- [class CSSearchableIndex](cssearchableindex.md)
  An on-device index for your app’s searchable content.
- [protocol CSSearchableIndexDelegate](cssearchableindexdelegate.md)
  A protocol that defines methods a delegate object or app extension uses to handle communication from the on-device index.
### Spotlight app extensions
- [Regenerating your app’s indexes on demand](regenerating-your-app-s-indexes-on-demand.md)
  Create an app extension to maintain your app’s indexes and regenerate them as needed.
- [class CSIndexExtensionRequestHandler](csindexextensionrequesthandler.md)
  An interface that implements an index-maintenance app extension.
- [class CSImportExtension](csimportextension.md)
  An object that provides searchable attributes for file types that the app supports.
### Queries
- [Building a search interface for your app](building-a-search-interface-for-your-app.md)
  Add a search interface to your app to execute Spotlight queries and offer suggested text completions.
- [Searching for information in your app](searching-for-information-in-your-app.md)
  Search for app-specific content and refine search results using predicates and filters.
- [class CSUserQuery](csuserquery.md)
  A type you use to initiate searches from your interface and offer suggested text completions.
- [class CSUserQueryContext](csuserquerycontext.md)
  The configuration details to apply to a user query.
- [class CSSearchQuery](cssearchquery.md)
  A type you use to programmatically search the indexed app content.
- [class CSSearchQueryContext](cssearchquerycontext.md)
  The behavior configuration to use for a search query.
- [class CSSuggestion](cssuggestion.md)
  The kind of suggestion to use in a query.
### Errors
- [struct CSIndexError](csindexerror.md)
  Index errors returned by Core Spotlight.
- [struct CSSearchQueryError](cssearchqueryerror.md)
  Search query errors returned by Core Spotlight.
- [CSIndex Errors](csindex-errors.md)
  Index error codes and error domain.
- [CSSearchQuery Errors](cssearchquery-errors.md)
  Search query error codes and error domain.
### Version
- [var CoreSpotlightAPIVersion: Int32](corespotlightapiversion.md)
  The API version number for Core Spotlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreSpotlight)*