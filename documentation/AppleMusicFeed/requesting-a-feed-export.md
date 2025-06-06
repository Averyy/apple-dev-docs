# Requesting a feed export

**Framework**: Apple Music Feed

Create requests for Apple Music Catalog metadata.

#### Overview

To get the data for an Apple Music Feed data set, request information about the latest feed export, use that information to request links to parts of the feed, and then use those links to download the data.

#### Compose a Request

To compose a request, first specify the root path, `https://api.media.apple.com/v1`.

Follow the root path with `/feed/` and the required information for the specific request.

#### Request Metadata for the Latest Feed Export

To request metadata about the latest available export for an Apple Music Feed data set, construct a URL that includes the `feedId` followed by `/latest`.

The possible values for `feedId` are: `album`, `song`, `artist`, `popularityTopChartAlbums`, and `popularityTopChartSongs`.

```None
GET https://api.media.apple.com/v1/feed/album/latest
```

The response returns metadata about the most recent export for the specified `feedId`, including an `id` that you can use to request the data from that export.

```None
"data": [
  {
    "id": "album_2024-02-13T16-01",
    "type": "exports",
    "href": "/v1/feed/exports/album_2024-02-13T16-01"
  }
],
```

#### Request Feed Data Links

To request links to parts of the data for a feed export, construct a URL that includes the `id` of a specific feed export, which you can get from the response above, followed by `/parts`. You can use the `limit` and `offset` parameters to paginate the returned results. For more information, see [`Fetching Resources by Page`](https://developer.apple.comhttps://developer.apple.com/documentation/applemusicapi/fetching_resources_by_page).

```None
GET https://api.media.apple.com/v1/feed/exports/{id}/parts?limit=100&offset=0
```

The response returns `parts` objects as `resources`, each of which includes an `exportLocation` for the data in that part of the feed export.

```None
{
  "data": [
    {
      "id": "0_part_album_2024-03-28T16-01",
      "type": "parts"
    },
    {
      "id": "1_part_album_2024-03-28T16-01",
      "type": "parts"
    },
...
  ],
  "resources": {
    "parts": {
      "0_part_album_2024-03-28T16-01": {
        "id": "0_part_album_2024-03-28T16-01",
        "type": "parts",
        "attributes": {
          "offset": 0,
          "exportLocation": "https://media-feed.cdn-apple.com/Album/version=1/date=2024-03-28/time=16-01/part-00000-eb1af027-79a8-40cb-a2cb-1c21c17e1b9f-c000.gz.parquet?accessKey=1712275437_3609532_apoBXQ4oV3h19tJ17k2OE1ZN44IXaETir8i29FKfGFiaTLlbz9DSIcveAIlQIzYHpxMUty1LkYYGsABcu7YLSFKhVRxq6KVbqUaL6%2BHoGBRzIG%2F%2BNl%2Fz1yc2kAAFvc%2FZTMuquTTYo%2FGjGP660bghGIsesFWapX%2BhmkeRuE3TwB8%3D"
        }
      },
      "1_part_album_2024-03-28T16-01": {
        "id": "1_part_album_2024-03-28T16-01",
        "type": "parts",
        "attributes": {
          "offset": 1,
          "exportLocation": "https://media-feed.cdn-apple.com/Album/version=1/date=2024-03-28/time=16-01/part-00001-eb1af027-79a8-40cb-a2cb-1c21c17e1b9f-c000.gz.parquet?accessKey=1712275437_3913853_kh1V1Ql%2Bv698vW2pDWHh%2F7P7f4dho%2FOOKfLdmGo9nA434tCDnUY34gzzAAZAUywoMU3YpszuWShbYQkakq%2BzxAwj3THpu27jglK%2BQ6x1BGlwHcYcAnb0xJKpoAKhEhFjzwIlos5VoGqdRnUL13mKbIlsHix4Ro3qiH%2B7eGFxoa0%3D"
        }
      },
...
    }
  },
```

#### Download the Feed Data

Use the links that the `parts` response provides to download the feed data. Note that access to these links expires after a specified time.

#### Data Example

The feed exports are in Parquet format. The following data example is in JSON format for illustrative purposes:

```None
{
  "id": "1440935467",
  "name": {
    "en-US": "1989",
    "default": "1989"
  },
  "nameDefault": "1989",
  "namePronunciation": {
    "en-US": "1989",
    "default": "1989"
  },
  "titleVersion": {
    "en-US": "Remastered",
    "default": "Remastered"
  },
  "titleVersionPronunciation": {
    "en-US": "Remastered",
    "default": "Remastered"
  },
  "parentalAdvisoryType": "none",
  "primaryArtists": [
    {
      "id": "159260351",
      "name": "Taylor Swift"
    }
  ],
  "featuredArtists": [
    {
      "id": "159260351",
      "name": "Taylor Swift"
    }
  ],
  "artistRoles": [
    {
      "artistId": "159260351",
      "artistName": "Taylor Swift",
      "roleName": "Composer"
    },
    {
      "artistId": "159260351",
      "artistName": "Taylor Swift",
      "roleName": "Performer"
    }
  ],
  "urlTemplate": "https://music.apple.com/{country-code}/album/1440935467",
  "artworks": {
    "default": [
      {
        "url": "https://is5-ssl.mzstatic.com/image/thumb/Music115/v4/09/01/16/090116af-770e-23da-21a9-6bd30782eda5/00843930013562.rgb.jpg/1400x1400bb.jpg",
        "height": 1400,
        "width": 1400
      }
    ],
    "es-MX": [
      {
        "url": "https://is5-ssl.mzstatic.com/image/thumb/Music115/v4/09/01/16/090116af-770e-23da-21a9-6bd30782eda5/00843930013562.rgb.jpg/1400x1400bb.jpg",
        "height": 1400,
        "width": 1400
      }
    ]
  },
  "releaseDate": {
    "default": "2014-10-27"
  },
  "recordLabels": [
    {
      "name": "Big Machine Records, LLC"
    }
  ],
  "contentProvider": "UMG Global",
  "copyright": "℗ 2014 Apollo A-1 LLC",
  "copyrightPLine": "2014 Apollo A-1 LLC",
  "albumType": "standard",
  "genres": [
    {
      "name": "Pop",
      "path": [
        "Music",
        "Pop"
      ]
    },
    {
      "name": "Music",
      "path": [
        "Music"
      ]
    },
    {
      "name": "Rock",
      "path": [
        "Music",
        "Rock"
      ]
    }
  ],
  "songs": [
    {
      "id": "1440935802"
    },
    {
      "id": "1440935808"
    },
    {
      "id": "1440935812"
    },
    {
      "id": "1440935820"
    },
    {
      "id": "1440935829"
    },
    {
      "id": "1440936016"
    },
    {
      "id": "1440936021"
    },
    {
      "id": "1440936028"
    },
    {
      "id": "1440936036"
    },
    {
      "id": "1440936195"
    },
    {
      "id": "1440936201"
    },
    {
      "id": "1440936203"
    },
    {
      "id": "1440936206"
    }
  ],
  "prices": {
    "us": [
      {
        "price": 10.99,
        "priceType": "buy",
        "currencyCode": "USD",
        "quality": "high-definition"
      },
      {
        "price": 0.0,
        "priceType": "streaming",
        "currencyCode": "USD"
      }
    ]
  },
  "upc": "00843930013562",
  "lastModifiedTime": "2023-04-24T20:39:30.600Z",
  "contentTraits": [
    "compilation"
  ]
}
```

## See Also

- [Generating developer tokens](generating-developer-tokens.md)
  Create a JSON Web Token to authorize your requests to Apple Media Feed API.
- [Interpreting responses](interpreting-responses.md)
  Learn about responses from Apple Media Feed API to your Apple Music Feed requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicfeed/requesting-a-feed-export)*