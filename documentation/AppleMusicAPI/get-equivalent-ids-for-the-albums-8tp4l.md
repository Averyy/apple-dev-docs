# Get Equivalent Catalog Music Videos by ID

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch the equivalent, available content in the storefront for the provided music videos’ identifiers.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/ch/music-videos?filter[equivalents]=1553279848
```

**Response**:

```json
{
    "data": [
        {
            "id": "1552406856",
            "type": "music-videos",
            "href": "/v1/catalog/ch/music-videos/1552406856",
            "attributes": {
                "previews": [
                    {
                        "url": "https: //video-ssl.itunes.apple.com/itunes-assets/Video114/v4/d6/33/c5/d633c5de-0ddb-ad5d-a560-3e9fb35c057b/mzvf_2101846033664580247.720w.h264lc.U.p.m4v",
                        "hlsUrl": "https: //play.itunes.apple.com/WebObjects/MZPlay.woa/hls/playlist.m3u8?cc=CH&a=1552406856&id=230060134&l=de&aec=HD",
                        "artwork": {
                            "width": 1561,
                            "url": "https: //is2-ssl.mzstatic.com/image/thumb/Video114/v4/f0/dc/be/f0dcbea2-4718-c310-d9f6-f16d86ffd699/Jobfaa18d62-b9d3-4e7a-ac99-fc4ca04a9c9a-109210777-PreviewImage_preview_image_45000_video_sdr-Time1612539991665.png/{w}x{h}bb.jpeg",
                            "height": 1080,
                            "textColor3": "a5a69c",
                            "textColor2": "bac0c4",
                            "textColor4": "9a9fa1",
                            "textColor1": "c7c9bd",
                            "bgColor": "1b1b19",
                            "hasP3": false
                        }
                    }
                ],
                "artwork": {
                    "width": 1553,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/Video114/v4/c4/09/a5/c409a5d5-61c1-5a3b-54ca-6bb34af4a7da/21UMGIM09694.crop.jpg/{w}x{h}mv.jpeg",
                    "height": 1072,
                    "textColor3": "c6b490",
                    "textColor2": "d4bb93",
                    "textColor4": "b9a17e",
                    "textColor1": "e5d2a9",
                    "bgColor": "4d3a2c",
                    "hasP3": false
                },
                "artistName": "Dua Lipa",
                "url": "https: //music.apple.com/ch/music-video/were-good/1552406856",
                "genreNames": [
                    "Pop"
                ],
                "has4K": false,
                "durationInMillis": 181033,
                "releaseDate": "2021-02-12",
                "name": "We’re Good",
                "isrc": "GB1302001140",
                "playParams": {
                    "id": "1552406856",
                    "kind": "musicVideo"
                },
                "hasHDR": false
            },
            "relationships": {
                "artists": {
                    "href": "/v1/catalog/ch/music-videos/1552406856/artists",
                    "data": [
                        {
                            "id": "1031397873",
                            "type": "artists",
                            "href": "/v1/catalog/ch/artists/1031397873"
                        }
                    ]
                },
                "albums": {
                    "href": "/v1/catalog/ch/music-videos/1552406856/albums",
                    "data": []
                }
            }
        }
    ],
    "meta": {
        "filters": {
            "equivalents": {
                "1553279848": [
                    {
                        "id": "1552406856",
                        "type": "music-videos",
                        "href": "/v1/catalog/ch/music-videos/1552406856"
                    }
                ]
            }
        }
    }
}

```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/music-videos`

## Parameters

- `filter[equivalents]` ([string]) *(required)*: A filter to apply to the request. The maximum fetch limit is 25.
- `include` ([string]): Additional relationships to include in the fetch.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `restrict` ([string]): A set of restrictions (for example, to restrict explicit content).
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object MusicVideos](musicvideos.md)
  A resource object that represents a music video.
- [object MusicVideosResponse](musicvideosresponse.md)
  The response to a music videos request.
- [Get a Catalog Music Video](get-a-catalog-music-video.md)
  Fetch a music video by using its identifier.
- [Get a Catalog Music Video's Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-4z79l.md)
  Fetch a music video’s relationship by using its identifier.
- [Get a Catalog Music Video’s Relationship View Directly by Name](fetch-a-view-on-this-resource-by-name-5657g.md)
  Fetch related resources for a single music video’s relationship view.
- [Get Multiple Catalog Music Videos by ID](get-multiple-catalog-music-videos-by-id.md)
  Fetch one or more music videos by using their identifiers.
- [Get Multiple Catalog Music Videos by ISRC](get-multiple-catalog-music-videos-by-isrc.md)
  Fetch one or more music videos by using their International Standard Recording Code (ISRC) values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-equivalent-ids-for-the-albums-8tp4l)*