# AlbumPeriodSummaries

**Framework**: Apple Music API  
**Kind**: dictionary

The album for the period summary.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object AlbumPeriodSummaries
```

## Topics

### Dictionaries
- [object AlbumPeriodSummaries.Relationships](albumperiodsummaries/relationships-data.dictionary.md)
  The relationships from album-period-summary to other resources.

## Properties

- `id` (string) *(required)*: The identifier for the album period summaries resource.
- `relationships` (AlbumPeriodSummaries.Relationships): The connection from `artist-period-summary` to other resources.
- `type` (string) *(required)*: The type of resource. This value is always `album-period-summaries`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/albumperiodsummaries)*