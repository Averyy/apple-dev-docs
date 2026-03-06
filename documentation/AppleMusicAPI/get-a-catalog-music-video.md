# Get a Catalog Music Video

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch a music video by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/music-videos/1553279848
```

**Response**:

```json
{
    "data": [
        {
            "id": "1553279848",
            "type": "music-videos",
            "href": "/v1/catalog/us/music-videos/1553279848",
            "attributes": {
                "previews": [
                    {
                        "url": "https://video-ssl.itunes.apple.com/itunes-assets/Video114/v4/c8/14/3c/c8143cb4-e58a-8075-44b0-602f43d7646f/mzvf_2953199973497507158.720w.h264lc.U.p.m4v",
                        "hlsUrl": "https://play.itunes.apple.com/WebObjects/MZPlay.woa/hls/playlist.m3u8?cc=US&a=1553279848&id=231169237&l=en&aec=HD",
                        "artwork": {
                            "width": 1560,
                            "height": 1080,
                            "url": "https://is3-ssl.mzstatic.com/image/thumb/Video124/v4/26/6b/fe/266bfe0f-9d0c-e992-ae86-ce97cb251e40/Job80599ed4-a39e-455a-9f99-5bdc54c44284-109334076-PreviewImage_preview_image_43000_video_sdr-Time1613053183818.png/{w}x{h}bb.jpeg",
                            "bgColor": "cadee0",
                            "textColor1": "101414",
                            "textColor2": "181e1f",
                            "textColor3": "353c3d",
                            "textColor4": "3b4445"
                        }
                    }
                ],
                "artwork": {
                    "width": 640,
                    "height": 360,
                    "url": "https://is1-ssl.mzstatic.com/image/thumb/Video124/v4/3f/1e/6f/3f1e6f35-6960-3f0e-0a0c-8701aa2012d4/dj.bcvxpufw.jpg/{w}x{h}mv.jpeg",
                    "bgColor": "000000",
                    "textColor1": "86bff9",
                    "textColor2": "7cb0ea",
                    "textColor3": "6b98c7",
                    "textColor4": "638dbb"
                },
                "artistName": "Dua Lipa",
                "url": "https://music.apple.com/us/music-video/were-good/1553279848",
                "genreNames": [
                    "Pop"
                ],
                "has4K": false,
                "durationInMillis": 191913,
                "releaseDate": "2021-02-12",
                "name": "We’re Good",
                "isrc": "GB1302001140",
                "playParams": {
                    "id": "1553279848",
                    "kind": "musicVideo"
                },
                "hasHDR": false
            },
            "relationships": {
                "artists": {
                    "href": "/v1/catalog/us/music-videos/1553279848/artists",
                    "data": [
                        {
                            "id": "1031397873",
                            "type": "artists",
                            "href": "/v1/catalog/us/artists/1031397873"
                        }
                    ]
                },
                "albums": {
                    "href": "/v1/catalog/us/music-videos/1553279848/albums",
                    "data": [

                    ]
                }
            }
        }
    ]
}


```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/music-videos/{id}`

## Parameters

- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `include` ([string]): Additional relationships to include in the fetch.
- `views` ([string]): The views to activate for the resource.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object MusicVideos](musicvideos.md)
  A resource object that represents a music video.
- [object MusicVideosResponse](musicvideosresponse.md)
  The response to a music videos request.
- [Get a Catalog Music Video's Relationship Directly by Name](fetch-a-relationship-on-this-resource-by-name-4z79l.md)
  Fetch a music video’s relationship by using its identifier.
- [Get a Catalog Music Video’s Relationship View Directly by Name](fetch-a-view-on-this-resource-by-name-5657g.md)
  Fetch related resources for a single music video’s relationship view.
- [Get Multiple Catalog Music Videos by ID](get-multiple-catalog-music-videos-by-id.md)
  Fetch one or more music videos by using their identifiers.
- [Get Multiple Catalog Music Videos by ISRC](get-multiple-catalog-music-videos-by-isrc.md)
  Fetch one or more music videos by using their International Standard Recording Code (ISRC) values.
- [Get Equivalent Catalog Music Videos by ID](get-equivalent-ids-for-the-albums-8tp4l.md)
  Fetch the equivalent, available content in the storefront for the provided music videos’ identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-a-catalog-music-video)*