# Get a Catalog Song

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch a song by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/songs/1613600188
```

**Response**:

```json
{
    "data": [
        {
            "id": "1613600188",
            "type": "songs",
            "href": "/v1/catalog/us/songs/1613600188",
            "attributes": {
                "albumName": "Emotional Creature",
                "genreNames": [
                    "Alternative",
                    "Music"
                ],
                "trackNumber": 1,
                "durationInMillis": 221000,
                "releaseDate": "2022-06-09",
                "isrc": "USQE92100257",
                "artwork": {
                    "width": 3000,
                    "height": 3000,
                    "url": "https://is1-ssl.mzstatic.com/image/thumb/Music112/v4/df/4e/68/df4e6833-9828-51d7-cdeb-71ecf6d3a23d/810090090962.png/{w}x{h}bb.jpg",
                    "bgColor": "202020",
                    "textColor1": "aea6f6",
                    "textColor2": "b68ef6",
                    "textColor3": "918bcb",
                    "textColor4": "9878cb"
                },
                "composerName": "Anthony Vaccaro, Jon Alvarado, Lili Trifilio & Matt Henkels",
                "playParams": {
                    "id": "1613600188",
                    "kind": "song"
                },
                "url": "https://music.apple.com/us/album/entropy/1613600183?i=1613600188",
                "discNumber": 1,
                "hasLyrics": true,
                "isAppleDigitalMaster": true,
                "name": "Entropy",
                "previews": [
                    {
                        "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview122/v4/72/a3/ab/72a3ab79-0066-f773-6618-7a53adc250b3/mzaf_17921540907592750976.plus.aac.p.m4a"
                    }
                ],
                "artistName": "Beach Bunny"
            },
            "relationships": {
                "artists": {
                    "href": "/v1/catalog/us/songs/1613600188/artists",
                    "data": [
                        {
                            "id": "1147783278",
                            "type": "artists",
                            "href": "/v1/catalog/us/artists/1147783278"
                        }
                    ]
                },
                "albums": {
                    "href": "/v1/catalog/us/songs/1613600188/albums",
                    "data": [
                        {
                            "id": "1613600183",
                            "type": "albums",
                            "href": "/v1/catalog/us/albums/1613600183"
                        }
                    ]
                }
            }
        }
    ]
}
```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/songs/{id}`

## Parameters

- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `include` ([string]): Additional relationships to include in the fetch.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object Songs](songs.md)
  A resource object that represents a song.
- [object SongsResponse](songsresponse.md)
  The response to a songs request.
- [Get a Catalog Song's Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-56rq7.md)
  Fetch a song’s relationship by using its identifier.
- [Get Multiple Catalog Songs by ID](get-multiple-catalog-songs-by-id.md)
  Fetch one or more songs by using their identifiers.
- [Get Multiple Catalog Songs by ISRC](get-multiple-catalog-songs-by-isrc.md)
  Fetch one or more songs by using their International Standard Recording Code (ISRC) values.
- [Get Equivalent Catalog Songs by ID](get-equivalent-ids-for-the-albums-3ce20.md)
  Fetch the equivalent, available content in the storefront for the provided songs’ identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-a-catalog-song)*