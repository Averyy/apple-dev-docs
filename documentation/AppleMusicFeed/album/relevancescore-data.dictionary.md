# Album.RelevanceScore

**Framework**: Apple Music Feed  
**Kind**: dictionary  
**Role**: Object

A score representing album relevance, used to rank albums when surfacing content.

**Availability**:
- AppleMusicFeed 1.0+

## Declaration

```
object Album.RelevanceScore
```

## Overview

A higher score indicates higher relevance. For example, an album with a score of 90 is ranked as more relevant than an album with a score of 50.

## Topics

### Related objects
- [object Album.RelevanceScore.StorefrontOverrides](./relevancescore-data.dictionary/storefrontoverrides-data.dictionary.md)
  A mapping of storefront country code to relevance score.

## Properties

- `defaultScore` (integer): The default relevance score.
- `storefrontOverrides` (Album.RelevanceScore.StorefrontOverrides): A mapping of storefront country codes to relevance scores.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicfeed/album/relevancescore-data.dictionary)*