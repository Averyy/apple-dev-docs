# ArtistPeriodSummaries

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

The artist for the period summary.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object ArtistPeriodSummaries
```

## Topics

### Dictionaries
- [object ArtistPeriodSummaries.Relationships](./artistperiodsummaries/relationships-data.dictionary.md)
  The relationships from [`ArtistPeriodSummaries`](./artistperiodsummaries.md) to other resources.

## Properties

- `id` (string) *(required)*: The identifier for the artist period summaries resource.
- `relationships` (ArtistPeriodSummaries.Relationships): The [`ArtistPeriodSummaries.Relationships`](./artistperiodsummaries/relationships-data.dictionary.md) relationship.
- `type` (string) *(required)*: The type of the resource.

  **Allowed Values**: `artist-period-summaries`


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/artistperiodsummaries)*