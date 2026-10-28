# SupportedURLs

**Framework**: AppleNewsFormat  
**Kind**: typealias  
**Role**: Type

Links that go to Apple News, other Apple apps, and external sites.

**Availability**:
- Apple News Format 1.11+

## Declaration

```
string SupportedURLs
```

## Discussion

You can define the following Apple domain links for the `URL` property in [`Text`](./text.md) components:

- A link to an Apple News article. Begin each link with `https://apple.news/`. To link within the document, use an anchor link starting with `#`, followed by the component identifier to which you want to link. To link to a component in another article, you must include an Apple News URL with the `#` and component identifier after it; for example, `https://apple.news/A5vHgPPmQSvuIxPjeXLTdGQ#TextComponent-1`.
- A canonical link element associated with an Apple News article by its `canonicalURL` in [`Metadata`](./metadata.md).
- A link to the iTunes Store, the App Store, Apple Books, Apple Music, or Apple Podcasts you create using a [link generator](https://tools.applemediaservices.com/app-store).
- A link to a ticker symbol in the Stocks app, using the URL format `stocks://?symbol=`*ticker symbol*; for example, `stocks://?symbol=AAPL`.
- A link to Apple Music with the format `music://` or `musics://`.

You can define the following external links for the `URL` property in [`Text`](./text.md) components:

- A universal link. See [Universal Links for Developers](https://developer.apple.com/ios/universal-links/).
- A link to an external site.
- A link to an email address that begins with `mailto:`.
- A link to a hosted calendar that begins with `webcal://</value>`.

## See Also

### Links
- [object LinkAddition](./linkaddition.md)
  The addition object for defining links in text components that don’t use HTML or Markdown formatting.
- [object ComponentLink](./componentlink.md)
  The component addition object for making a component interactive and opening a link to another location in News.
- [object Addition](./addition.md)
  Properties that all addition types share.
- [object ComponentAddition](./componentaddition.md)
  Properties that all types of component additions share.
- [type SupportedInternalURLs](./supportedinternalurls.md)
  Links that go to Apple News and other Apple apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/supportedurls)*