# Get All Library Songs

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch all the library songs in alphabetical order.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array.

This endpoint requires a music user token. For more information, see [`User Authentication for MusicKit`](user-authentication-for-musickit.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/me/library/songs
```

**Response**:

```json
{    
    "next": "/v1/me/library/albums?offset=3",
    "data": [
        {
            "id": "i.PkdJNdAIrQozOW",
            "type": "library-songs",
            "href": "/v1/me/library/songs/i.PkdJNdAIrQozOW",
            "attributes": {
                "albumName": "Un Verano Sin Ti",
                "discNumber": 1,
                "genreNames": [
                    "Latin"
                ],
                "trackNumber": 10,
                "hasLyrics": true,
                "durationInMillis": 213061,
                "releaseDate": "2022-05-06",
                "name": "Efecto",
                "artistName": "Bad Bunny",
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https://is5-ssl.mzstatic.com/image/thumb/Music112/v4/3e/04/eb/3e04ebf6-370f-f59d-ec84-2c2643db92f1/196626945068.jpg/{w}x{h}bb.jpg"
                },
                "playParams": {
                    "id": "i.PkdJNdAIrQozOW",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1622045954",
                    "reportingId": "1622045954"
                }
            }
        },
        {
            "id": "i.LVk4NkKT2bV0qR",
            "type": "library-songs",
            "href": "/v1/me/library/songs/i.LVk4NkKT2bV0qR",
            "attributes": {
                "discNumber": 1,
                "albumName": "Emotional Creature",
                "genreNames": [
                    "Alternative"
                ],
                "trackNumber": 1,
                "hasLyrics": true,
                "releaseDate": "2022-06-09",
                "durationInMillis": 221000,
                "name": "Entropy",
                "artistName": "Beach Bunny",
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https://is1-ssl.mzstatic.com/image/thumb/Music112/v4/df/4e/68/df4e6833-9828-51d7-cdeb-71ecf6d3a23d/810090090962.png/{w}x{h}bb.jpg"
                },
                "playParams": {
                    "id": "i.LVk4NkKT2bV0qR",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1613600188",
                    "reportingId": "1613600188"
                }
            }
        },
        {
            "id": "i.QvzgN9kHEBxbzJ",
            "type": "library-songs",
            "href": "/v1/me/library/songs/i.QvzgN9kHEBxbzJ",
            "attributes": {
                "albumName": "Palaces",
                "discNumber": 1,
                "genreNames": [
                    "Electronic"
                ],
                "trackNumber": 6,
                "hasLyrics": false,
                "releaseDate": "2022-05-20",
                "durationInMillis": 254868,
                "name": "Get U",
                "artistName": "Flume",
                "artwork": {
                    "width": 1200,
                    "height": 1200,
                    "url": "https://is5-ssl.mzstatic.com/image/thumb/Music112/v4/ce/8c/7b/ce8c7bc8-e070-7faa-1d58-157e4550e483/653738991029.png/{w}x{h}bb.jpg"
                },
                "playParams": {
                    "id": "i.QvzgN9kHEBxbzJ",
                    "kind": "song",
                    "isLibrary": true,
                    "reporting": true,
                    "catalogId": "1605983206",
                    "reportingId": "1605983206"
                }
            }
        }
    ],
    "meta": {
        "total": 100
    }
}


```

## Endpoint

`GET https://api.music.apple.com/v1/me/library/songs`

## Parameters

- `include` ([string]): Additional relationships to include in the fetch.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.
- `offset` (string): The next page or group of objects to fetch.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object LibrarySongs](librarysongs.md)
  A resource object that represents a library song.
- [object LibrarySongsResponse](librarysongsresponse.md)
  The response to a library songs request.
- [Get a Library Song](get-a-library-song.md)
  Fetch a library song by using its identifier.
- [Get a Library Song's Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-9xvg6.md)
  Fetch a library song’s relationship by using its identifier.
- [Get Multiple Library Songs](get-multiple-library-songs.md)
  Fetch one or more library songs by using their identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-all-library-songs)*