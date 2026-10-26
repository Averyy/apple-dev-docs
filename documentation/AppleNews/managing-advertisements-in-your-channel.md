# Managing Advertisements in Your Channel

**Framework**: Apple News  
**Role**: Article

Set the layout and frequency of ads automatically inserted in an article.

#### Overview

Apple News places ads in any of the following locations:

- Between two `body` components
- Between two paragraphs inside a `body` component
- Between containers
- After the last component — even if the article is shorter than one screen

Ads can’t appear in these locations:

- Between anchored components
- In the first screen of an article

In addition to the location requirements, Apple News makes decisions about ad placement for your articles:

- Both the size of your article and the arrangement of the components affect ad placement.
- Two ads can’t appear in the same viewport, which is the section of the article that’s currently visible within a person’s device frame.

##### Adjust Your Ads Settings

To control the placement of ads in your channel, use News Publisher. For more information, see [Apple News and ads](https://support.apple.com/guide/adguide/apple-news-and-ads-apd070650e01/icloud) in the Ads on Apple News User Guide.

## See Also

### Dynamic Advertising
- [object AutoPlacement](https://developer.apple.com/documentation/applenewsformat/autoplacement)
  The object for automatically placing components within Apple News Format articles.
- [object AdvertisementAutoPlacement](https://developer.apple.com/documentation/applenewsformat/advertisementautoplacement)
  The object for defining the automatic placement of advertisements.
- [object AdvertisingSettings](https://developer.apple.com/documentation/applenewsformat/advertisingsettings)
  The object for defining properties that affect the frequency and placement with which banner advertisements and medium rectangle advertisements are automatically placed in your article.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/managing-advertisements-in-your-channel)*