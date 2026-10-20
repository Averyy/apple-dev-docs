# Artist.RelevanceScore.StorefrontOverrides

**Framework**: Apple Music Feed  
**Kind**: dictionary  
**Role**: Object

A mapping of storefront country code to relevance score.

**Availability**:
- AppleMusicFeed 1.0+

## Declaration

```
object Artist.RelevanceScore.StorefrontOverrides
```

#### Overview

Country codes are lowercase ISO 3166-1 alpha-2 codes, for example, `us` or `gb`. When a storefront-specific score is available, use it instead of the default.

## Properties

- `storefront` (string): The storefront that is the key for the map of values.
- `storefrontOverride` (integer): The relevance score for a given storefront.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicfeed/artist/relevancescore-data.dictionary/storefrontoverrides-data.dictionary)*