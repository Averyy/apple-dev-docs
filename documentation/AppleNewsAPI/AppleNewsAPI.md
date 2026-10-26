# Apple News API

**Framework**: AppleNewsAPI  
**Kind**: module  
**Role**: Web Service

Publish and manage Apple News Format articles.

## Mentions

- [Getting Started as an Apple News Publisher](../AppleNews/getting-started-as-an-apple-news-publisher.md)

#### Overview

The Apple News API delivers Apple News Format articles to be published in the Apple News app and helps you manage and monitor those articles after they’ve been published.

Based on representational state transfer (REST) technology, the Apple News API has typical RESTful characteristics, which means that it:

- Does operations on a set of resources. Resources are objects that have a type, associated data, and relationships to other resources. In the Apple News API, resources include channels, sections that you’ve set up for your channels (for example, Sports or Politics), and the articles that you want to publish and manage.
- Has stateless operations. Interactions with the create, read, update, and delete (CRUD) operations are handled using only the information that comes with the request — no previous information or state is assumed. Therefore, requests made using the Apple News API must include all information required to complete the operation within the request.

## Topics

### Essentials
- [Getting Ready to Publish and Manage Your Articles](../AppleNews/getting-ready-to-publish-and-manage-your-articles.md)
  Get set up for using the Apple News API.
- [About the Apple News Security Model](../AppleNews/about-the-apple-news-security-model.md)
  Learn how the Apple News API authenticates clients, authorizes your news channel, and enforces confidentiality.
- [About Apple News API Field Types](../AppleNews/about-apple-news-api-field-types.md)
  Understand the standard field types used in the Apple News API.
- [Formatting Strings](../AppleNews/formatting-strings.md)
  Learn how to format strings to pass to the API client.
### Release Notes
- [Apple News API Release Notes](../AppleNews/apple-news-api-release-notes.md)
  Learn about new features that require iOS 26, iPadOS 26, and macOS 26.
### Channel
- [Read Channel Information](./get-channels-_channelid_.md)
  Get details about your channel, including the name, corresponding website, and default section.
- [Read Channel Quota Information](./get-channels-_channelid_-quota.md)
  Get details about your channel’s remaining quota for sending create and update requests, the queue size, and wait time.
- [object Channel](./channel.md)
  See the fields the read channel endpoint returned.
- [object ChannelLinks](./channellinks.md)
  See the links the read channel endpoint returned.
- [object ChannelResponse](./channelresponse.md)
  See which objects make up the channel response.
### Sections
- [List All Sections](./get-channels-_channelid_-sections.md)
  See a list of available sections in your channel.
- [Read Section Information](./get-sections-_sectionid_.md)
  Get information about the specified section, including its name, its channel, and whether it’s a default section.
- [Promote Articles in a Section](./post-sections-_sectionid_-promotedarticles.md)
  Set the list of promoted articles for the specified section.
- [object Section](./section.md)
  See the fields the section endpoints returned.
- [object SectionLinks](./sectionlinks.md)
  See the links the section endpoints returned.
- [object SectionResponse](./sectionresponse.md)
  See which objects make up the section response.
- [object PromoteArticleRequest](./promotearticlerequest.md)
  See the required field for the Promote an Article request.
- [object PromoteArticleResponse](./promotearticleresponse.md)
  See the field the Promote an Article response returned.
### Articles
- [Create an Article](./post-channels-_channelid_-articles.md)
  Publish an article to your channel.
- [Read Article Information](./get-articles-_articleid_.md)
  Retrieve information about an article, such as the revision number and maturity rating.
- [Search Articles in a Channel](./get-channels-_channelid_-articles.md)
  See a list of all articles in a channel that match the specified search criteria.
- [Search Articles in a Section](./get-sections-_sectionid_-articles.md)
  See a list of all articles in a section that match the specified search criteria.
- [Update an Article](./post-articles-_articleid_.md)
  Update an existing article in your channel.
- [Delete an Article](./delete-articles-_articleid_.md)
  Delete the specified article from your channel.
- [object Create Article Metadata Fields](./create-article-metadata-fields.md)
  See the optional metadata fields for the Create an Article Request.
- [object ArticleLinksRequest](./articlelinksrequest.md)
  See the required field for the Create an Article request.
- [object Update Article Metadata Fields](./update-article-metadata-fields.md)
  See the metadata fields for the Update an Article request.
- [object Article](./article.md)
  See the fields the article endpoints returned.
- [object ArticleResponse](./articleresponse.md)
  See which objects make up the Create an Article, Read an Article, and Update an Article responses.
- [object ArticleLinksResponse](./articlelinksresponse.md)
  See the links the article endpoints returned.
- [object SearchResponse](./searchresponse.md)
  See the fields the search article endpoints returned.
- [object Meta](./meta.md)
  See the object that wraps the throttling information that’s returned for the Create an Article and Read an Article endpoints.
- [object Throttling](./throttling.md)
  See the object that wraps the throttling information that’s returned for the Create an Article and Update an Article endpoints.
### Errors
- [About Apple News API Error Messages](../AppleNews/about-apple-news-api-error-messages.md)
  Understand the error message format for the Apple News API.
- [object Warning](./warning.md)
  See the properties of a warning the Apple News API returned.
- [object Error](./error.md)
  See the properties of an error the Apple News API returned.
- [type Code](./code.md)
  See the error codes the Apple News API returned.
- [type Status](./status.md)
  See the HTTP status codes the Apple News API returned.

## See Also

### Article Publication and Management
- [Apple News API Tutorial](../AppleNews/apple-news-api-tutorial.md)
  Request channel data and publish an article using the Apple News API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsapi)*