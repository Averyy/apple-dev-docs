# PopularityTopChartSongs.Genre

**Framework**: Apple Music Feed  
**Kind**: dictionary  
**Role**: Object

A genre name and its structure.

**Availability**:
- AppleMusicFeed 1.0+

## Declaration

```
object PopularityTopChartSongs.Genre
```

#### Discussion

Genres are hierarchical beginning with the genre `Music`.

#### Data example

The feed export is in Parquet format. This data example is in JSON format for illustrative purposes.

```
{
    "genres": {
        "name": "Rock",
        "path": [
            "Music",
            "Classical",
            "Rock"
        ]
    }
}
```

## Properties

- `name` (string): The name of the genre.
- `path` ([string]): A list of genres in hierarchical order. For example, if `Classical` is a subgenre of `Music`, this value is `[‘Music’, ‘Classical’]`.

## See Also

### Related objects
- [object PopularityTopChartSongs.Rankings](./rankings-data.dictionary.md)
  A song’s ranking in a popularity chart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicfeed/popularitytopchartsongs/genre-data.dictionary)*