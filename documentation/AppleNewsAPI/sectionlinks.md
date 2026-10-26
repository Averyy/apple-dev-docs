# SectionLinks

**Framework**: AppleNewsAPI  
**Kind**: dictionary  
**Role**: Object

See the links the section endpoints returned.

**Availability**:
- Apple News API 1.0+

## Declaration

```
object SectionLinks
```

## Properties

- `channel` (string): The URL of the channel in which this section appears.
- `self` (string): The URL at which you can read the article.

## Relationships

### Inherited By
- [SectionResponse](./sectionresponse.md)

## See Also

### Sections
- [List All Sections](./get-channels-_channelid_-sections.md)
  See a list of available sections in your channel.
- [Read Section Information](./get-sections-_sectionid_.md)
  Get information about the specified section, including its name, its channel, and whether it’s a default section.
- [Promote Articles in a Section](./post-sections-_sectionid_-promotedarticles.md)
  Set the list of promoted articles for the specified section.
- [object Section](./section.md)
  See the fields the section endpoints returned.
- [object SectionResponse](./sectionresponse.md)
  See which objects make up the section response.
- [object PromoteArticleRequest](./promotearticlerequest.md)
  See the required field for the Promote an Article request.
- [object PromoteArticleResponse](./promotearticleresponse.md)
  See the field the Promote an Article response returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsapi/sectionlinks)*