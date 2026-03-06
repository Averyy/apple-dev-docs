# Get a Catalog Playlist's Relationship Directly by Name

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch a playlist’s relationship by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/playlists/pl.cb4d1c09a2df4230a78d0395fe1f8fde/curator
```

**Response**:

```json
{
    "data": [
        {
            "id": "976439532",
            "type": "apple-curators",
            "href": "/v1/catalog/us/apple-curators/976439532",
            "attributes": {
                "editorialNotes": {
                    "standard": "Forget about classical music as a genre—think of it as an idea. The idea starts in a composer’s mind, is transferred to a written score, and is faithfully interpreted by performers. This chain—composer, score, performer—reaches back to the ancient Greeks and Romans and continues to define classical music today. For a casual listener, it might evoke iconic images—a pianist hunched over a Steinway, a chorus and orchestra’s euphoric rendering of Beethoven’s "Ode to Joy," a soprano in a Viking helmet singing Wagner’s Brünnhilde—but those images only represent only a few tiles in the ever-expanding mosaic of classical music.\n<br /><br />\nTo make sense of the wildly diverse terrain, classical music is often organized into major historical periods. There are three fairly concrete ones—the Baroque Era (approximately 1600-1750), the Classical Era (approximately 1750-1820), and the Romantic Era (approximately 1820-1910). These are bookended by enigmatic periods on either side: so-called Early Music (which includes music from Western Europe before the 17th century) and music from the 20th century and beyond, which can be referred to by any number of terms, like Contemporary Classical or New Music. But one of the great joys in exploring classical music is tracing its creative currents through the centuries—a lineage carried forward through the ages by revolutionaries like the prolific and pious Johann Sebastian Bach, the tempestuous fire of Ludwig van Beethoven, and the playful genius of Wolfgang Amadeus Mozart. While today’s composers continue to redefine the definitions of classical music, its traditions are courageously safeguarded (and challenged) by the interpretations of great conductors like Herbert von Karajan, Leonard Bernstein, and Pierre Boulez, and timeless recordings of performances by the likes of Yo-Yo Ma, Jascha Heifetz, Luciano Pavarotti, and Glenn Gould. ",
                    "short": "Soloists, symphonies, and the soundtrack of pure emotion. "
                },
                "kind": "Genre",
                "artwork": {
                    "width": 1080,
                    "height": 1080,
                    "url": "https: //is2-ssl.mzstatic.com/image/thumb/Features114/v4/91/24/1d/91241d46-7606-11ae-bcac-1039d8a90911/QkwtTVMtV1ctQ2xhc3NpY2FsLUFEQU1fSUQ9MTE0MjY1MjYxOCAoMTgpLnBuZw.png/{w}x{h}bb.jpg",
                    "bgColor": "4d3383",
                    "textColor1": "f6f4f8",
                    "textColor2": "edeaf2",
                    "textColor3": "d4cee1",
                    "textColor4": "cdc5dc"
                },
                "name": "Apple Music Classical",
                "shortName": "Classical",
                "url": "https: //music.apple.com/us/curator/apple-music-classical/976439532"
            }
        }
    ]
}

```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/playlists/{id}/{relationship}`

## Parameters

- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `include` ([string]): Additional relationships to include in the fetch.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object Playlists](playlists.md)
  A resource object that represents a playlist.
- [object PlaylistsResponse](playlistsresponse.md)
  The response to a playlists request.
- [Get a Catalog Playlist](get-a-catalog-playlist.md)
  Fetch a playlist by using its identifier.
- [Get a Catalog Playlist’s Relationship View Directly by Name](fetch-a-view-on-this-resource-by-name-6i3ek.md)
  Fetch related resources for a single playlist’s relationship view.
- [Get Multiple Catalog Playlists](get-multiple-catalog-playlists.md)
  Fetch one or more playlists by using their identifiers.
- [Get Charts Playlists by Storefront Value](get-charts-playlists-by-storefront-value.md)
  Fetch one or more Charts Playlists by using their Storefront value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/fetch-a-relationship-on-this-resource-by-name-707nb)*