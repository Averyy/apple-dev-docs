# Search for places that meet specific criteria to autocomplete a place search

**Framework**: Apple Maps Server API  
**Kind**: httpRequest

Find results that you can use to autocomplete searches.

**Availability**:
- Apple Maps Server API 1.2+

#### Discussion

##### Example

**Request**:

```None
curl -si -H "Authorization: Bearer <maps_access_token>" \
"https://maps-api.apple.com/v1/searchAutocomplete?q=museum&searchLocation=37.7753881,-122.3931773"
```

**Response**:

```json
{
  "results": [
    {
      "completionUrl": "/v1/search?q=Museums%20For%20Art",
      "displayLines": [
        "Museums For Art",
        "Search Nearby"
      ]
    },
    {
      "completionUrl": "/v1/search?q=Museum",
      "displayLines": [
        "Museum",
        "Search Nearby"
      ]
    },
    {
      "completionUrl": "/v1/search?q=Museum%20of%20Modern%20Art%20151%203rd%20St%2C%20San%20Francisco%2C%20CA%20%2094103%2C%20United%20States&metadata=ChwKFE11c2V1bSBvZiBNb2Rlcm4gQXJ0EgQIABAGEjUKMzE1MSAzcmQgU3QsIFNhbiBGcmFuY2lzY28sIENBICA5NDEwMywgVW5pdGVkIFN0YXRlcxgBKiIKEgkAAABAk%2BRCQBEAAACAq5lewBCElsC359Tk1PMBGK5NYggKBm11c2V1bYLxBAZtdXNldW2I8QQA2vEEFgkAAAAgEYb1PxEAAABgZmDCQDICZW7q8QQA",
      "displayLines": [
        "Museum of Modern Art",
        "151 3rd St, San Francisco, CA  94103, United States"
      ],
      "location": {
        "lat": 37.785743713378906,
        "lng": -122.40109252929688
      },
      "structuredAddress": {
        "administrativeArea": "California",
        "subAdministrativeArea": "San Francisco County",
        "administrativeAreaCode": "CA",
        "locality": "San Francisco",
        "postCode": "94103",
        "subLocality": "Financial District South",
        "thoroughfare": "3rd St",
        "subThoroughfare": "151",
        "fullThoroughfare": "151 3rd St",
        "areasOfInterest": [
          "San Francisco Museum of Modern Art"
        ],
        "dependentLocalities": [
          "Financial District South",
          "Yerba Buena",
          "FiDiSo"
        ]
      }
    },
    {
      "completionUrl": "/v1/search?q=de%20Young%20museum%2050%20Hagiwara%20Tea%20Garden%20Dr%2C%20San%20Francisco%2C%20CA%2094118%2C%20United%20States&metadata=ChcKD2RlIFlvdW5nIG11c2V1bRIECAkQBhJDCkE1MCBIYWdpd2FyYSBUZWEgR2FyZGVuIERyLCBTYW4gRnJhbmNpc2NvLCBDQSA5NDExOCwgVW5pdGVkIFN0YXRlcxgBKiIKEgkAAACgv%2BJCQBEAAABA%2F51ewBCn%2FY68hI664YIBGK5NYggKBm11c2V1bYLxBAZtdXNldW2I8QQA2vEEFgkAAADAN5waQBEAAACACwPBQDICZW7q8QQA",
      "displayLines": [
        "de Young museum",
        "50 Hagiwara Tea Garden Dr, San Francisco, CA 94118, United States"
      ],
      "location": {
        "lat": 37.7714729309082,
        "lng": -122.46870422363281
      },
      "structuredAddress": {
        "administrativeArea": "California",
        "subAdministrativeArea": "San Francisco",
        "administrativeAreaCode": "CA",
        "locality": "San Francisco",
        "postCode": "94118",
        "thoroughfare": "Hagiwara Tea Garden Dr",
        "subThoroughfare": "50",
        "fullThoroughfare": "50 Hagiwara Tea Garden Dr",
        "dependentLocalities": [
          "San Francisco",
          "Bay Area",
          "Golden Gate"
        ]
      }
    },
    {
      "completionUrl": "/v1/search?q=Asian%20Art%20Museum%20200%20Larkin%20St%2C%20San%20Francisco%2C%20CA%2094102%2C%20United%20States&metadata=ChgKEEFzaWFuIEFydCBNdXNldW0SBAgKEAYSNwo1MjAwIExhcmtpbiBTdCwgU2FuIEZyYW5jaXNjbywgQ0EgOTQxMDIsIFVuaXRlZCBTdGF0ZXMYASoiChIJAAAA4N%2FjQkARAAAAoKKaXsAQkNqC2ruqrLGyARiuTWIICgZtdXNldW2C8QQGbXVzZXVtiPEEANrxBBYJAAAAACS%2BAEARAAAAQApCn0AyAmVu6vEEAA%3D%3D",
      "displayLines": [
        "Asian Art Museum",
        "200 Larkin St, San Francisco, CA 94102, United States"
      ],
      "location": {
        "lat": 37.780269622802734,
        "lng": -122.41617584228516
      },
      "structuredAddress": {
        "administrativeArea": "California",
        "subAdministrativeArea": "San Francisco",
        "administrativeAreaCode": "CA",
        "locality": "San Francisco",
        "postCode": "94102",
        "subLocality": "Tenderloin",
        "thoroughfare": "Larkin St",
        "subThoroughfare": "200",
        "fullThoroughfare": "200 Larkin St",
        "dependentLocalities": [
          "NoMa",
          "Civic Center",
          "Tenderloin"
        ]
      }
    },
    {
      "completionUrl": "/v1/search?q=Museum%20of%20the%20Eye%20645%20Beach%20St%2C%20San%20Francisco%2C%20CA%2094109%2C%20United%20States&metadata=ChkKEU11c2V1bSBvZiB0aGUgRXllEgQIABAGEjYKNDY0NSBCZWFjaCBTdCwgU2FuIEZyYW5jaXNjbywgQ0EgOTQxMDksIFVuaXRlZCBTdGF0ZXMYASohChIJAAAAwDrnQkARAAAAwOCaXsAQwuvrgpbHydkJGK5NYggKBm11c2V1bYLxBAZtdXNldW2I8QQA2vEEFgkAAACgB7sQQBEAAADgo4BXQDICZW7q8QQA",
      "displayLines": [
        "Museum of the Eye",
        "645 Beach St, San Francisco, CA 94109, United States"
      ],
      "location": {
        "lat": 37.806480407714844,
        "lng": -122.41996765136719
      },
      "structuredAddress": {
        "administrativeArea": "California",
        "subAdministrativeArea": "San Francisco",
        "administrativeAreaCode": "CA",
        "locality": "San Francisco",
        "postCode": "94109",
        "subLocality": "Fisherman’s Wharf",
        "thoroughfare": "Beach St",
        "subThoroughfare": "645",
        "fullThoroughfare": "645 Beach St",
        "dependentLocalities": [
          "Fisherman’s Wharf"
        ]
      }
    },
    {
      "completionUrl": "/v1/search?q=Museum%20of%20Craft%20and%20Design%202569%203rd%20St%2C%20San%20Francisco%2C%20CA%20%2094107%2C%20United%20States&metadata=CiIKGk11c2V1bSBvZiBDcmFmdCBhbmQgRGVzaWduEgQIABAGEjYKNDI1NjkgM3JkIFN0LCBTYW4gRnJhbmNpc2NvLCBDQSAgOTQxMDcsIFVuaXRlZCBTdGF0ZXMYASohChIJAAAAwODgQkARAAAAwNOYXsAQ36Pw1oXM%2F44%2BGK5NYggKBm11c2V1bYLxBAZtdXNldW2I8QQA2vEEFgkAAABgdOQAQBEAAACA67FfQDICZW7q8QQA",
      "displayLines": [
        "Museum of Craft and Design",
        "2569 3rd St, San Francisco, CA  94107, United States"
      ],
      "location": {
        "lat": 37.756858825683594,
        "lng": -122.38792419433594
      },
      "structuredAddress": {
        "administrativeArea": "California",
        "subAdministrativeArea": "San Francisco County",
        "administrativeAreaCode": "CA",
        "locality": "San Francisco",
        "postCode": "94107",
        "subLocality": "Central Waterfront",
        "thoroughfare": "3rd St",
        "subThoroughfare": "2569",
        "fullThoroughfare": "2569 3rd St",
        "dependentLocalities": [
          "Central Waterfront",
          "Dogpatch"
        ]
      }
    },
    {
      "completionUrl": "/v1/search?q=Children%E2%80%99s%20Creativity%20Museum%20221%204th%20St%2C%20San%20Francisco%2C%20CA%20%2094103%2C%20United%20States&metadata=CiYKHkNoaWxkcmVu4oCZcyBDcmVhdGl2aXR5IE11c2V1bRIECBYQBhI1CjMyMjEgNHRoIFN0LCBTYW4gRnJhbmNpc2NvLCBDQSAgOTQxMDMsIFVuaXRlZCBTdGF0ZXMYASohChIJAAAAAETkQkARAAAAoLyZXsAQq5L%2Fh6zB24sgGK5NYggKBm11c2V1bYLxBAZtdXNldW2I8QQA2vEEFgkAAADgtezyPxEAAAAAAPCEQDICZW7q8QQA",
      "displayLines": [
        "Children’s Creativity Museum",
        "221 4th St, San Francisco, CA  94103, United States"
      ],
      "location": {
        "lat": 37.7833251953125,
        "lng": -122.40213775634766
      },
      "structuredAddress": {
        "administrativeArea": "California",
        "subAdministrativeArea": "San Francisco County",
        "administrativeAreaCode": "CA",
        "locality": "San Francisco",
        "postCode": "94103",
        "subLocality": "Yerba Buena",
        "thoroughfare": "4th St",
        "subThoroughfare": "221",
        "fullThoroughfare": "221 4th St",
        "dependentLocalities": [
          "Yerba Buena"
        ]
      }
    },
    {
      "completionUrl": "/v1/search?q=Museum%20of%20the%20African%20Diaspora%20685%20Mission%20St%2C%20San%20Francisco%2C%20CA%20%2094105%2C%20United%20States&metadata=CiYKHk11c2V1bSBvZiB0aGUgQWZyaWNhbiBEaWFzcG9yYRIECAAQBhI5Cjc2ODUgTWlzc2lvbiBTdCwgU2FuIEZyYW5jaXNjbywgQ0EgIDk0MTA1LCBVbml0ZWQgU3RhdGVzGAEqIQoSCQAAAICo5EJAEQAAAMCxmV7AEM%2BAktDw7KnLeRiuTWIICgZtdXNldW2C8QQGbXVzZXVtiPEEANrxBBYJAAAAgBfK9j8RAAAA4KOUcUAyAmVu6vEEAA%3D%3D",
      "displayLines": [
        "Museum of the African Diaspora",
        "685 Mission St, San Francisco, CA  94105, United States"
      ],
      "location": {
        "lat": 37.78639221191406,
        "lng": -122.40147399902344
      },
      "structuredAddress": {
        "administrativeArea": "California",
        "subAdministrativeArea": "San Francisco County",
        "administrativeAreaCode": "CA",
        "locality": "San Francisco",
        "postCode": "94105",
        "subLocality": "Yerba Buena",
        "thoroughfare": "Mission St",
        "subThoroughfare": "685",
        "fullThoroughfare": "685 Mission St",
        "dependentLocalities": [
          "SOMA",
          "South Beach",
          "Financial District South",
          "FiDiSo",
          "Yerba Buena"
        ]
      }
    },
    {
      "completionUrl": "/v1/search?q=Belvedere%20Museum%20Prinz-Eugen-Stra%C3%9Fe%2027%2C%201030%20Vienna%2C%20Austria&metadata=ChgKEEJlbHZlZGVyZSBNdXNldW0SBAgKEAYSLgosUHJpbnotRXVnZW4tU3RyYcOfZSAyNywgMTAzMCBWaWVubmEsIEF1c3RyaWEYASohChIJAAAAgIMYSEARAAAAIIZhMEAQ%2BLufo5P3vKxwGK5NYggKBm11c2V1bYLxBAZtdXNldW2I8QQA2vEEFgkAAABAocvCQBEAAACgEDrBQDICZW7q8QQA",
      "displayLines": [
        "Belvedere Museum",
        "Prinz-Eugen-Straße 27, 1030 Vienna, Austria"
      ],
      "location": {
        "lat": 48.19151306152344,
        "lng": 16.380952835083008
      },
      "structuredAddress": {
        "administrativeArea": "Vienna",
        "subAdministrativeArea": "Vienna",
        "locality": "Vienna",
        "postCode": "1030",
        "subLocality": "3. Bezirk Landstraße",
        "thoroughfare": "Prinz-Eugen-Straße",
        "subThoroughfare": "27",
        "fullThoroughfare": "Prinz-Eugen-Straße 27",
        "areasOfInterest": [
          "Botanischer Garten Der Universität",
          "Maria-theresien-platz and Memorial",
          "Belvedere Palace"
        ],
        "dependentLocalities": [
          "Landstrasse",
          "3. Bezirk Landstraße"
        ]
      }
    },
    {
      "completionUrl": "/v1/search?q=Crocker%20Art%20Museum%20216%20O%20St%2C%20Sacramento%2C%20CA%2095814%2C%20United%20States&metadata=ChoKEkNyb2NrZXIgQXJ0IE11c2V1bRIECAwQBhIvCi0yMTYgTyBTdCwgU2FjcmFtZW50bywgQ0EgOTU4MTQsIFVuaXRlZCBTdGF0ZXMYASohChIJAAAAQOBJQ0ARAAAAoGNgXsAQpd6j5oXVy%2BUvGK5NYggKBm11c2V1bYLxBAZtdXNldW2I8QQA2vEEFgkAAABg9oldQBEAAABgOEmlQDICZW7q8QQA",
      "displayLines": [
        "Crocker Art Museum",
        "216 O St, Sacramento, CA 95814, United States"
      ],
      "location": {
        "lat": 38.57715606689453,
        "lng": -121.5060806274414
      },
      "structuredAddress": {
        "administrativeArea": "California",
        "subAdministrativeArea": "Sacramento",
        "administrativeAreaCode": "CA",
        "locality": "Sacramento",
        "postCode": "95814",
        "subLocality": "Downtown",
        "thoroughfare": "O St",
        "subThoroughfare": "216",
        "fullThoroughfare": "216 O St",
        "dependentLocalities": [
          "Downtown"
        ]
      }
    },
    {
      "completionUrl": "/v1/search?q=Museum%20Parc%20300%203rd%20St%2C%20San%20Francisco%2C%20CA%20%2094107%2C%20United%20States&metadata=ChMKC011c2V1bSBQYXJjEgQIABAGEjUKMzMwMCAzcmQgU3QsIFNhbiBGcmFuY2lzY28sIENBICA5NDEwNywgVW5pdGVkIFN0YXRlcxgBKiEKEgkAAADgSeRCQBEAAACAh5lewBDpy%2BTLvYT3xCIYrk1iCAoGbXVzZXVtgvEEBm11c2V1bYjxBADa8QQWCQAAAMDuhvA%2FEQAAAAApbFpAMgJlburxBAA%3D",
      "displayLines": [
        "Museum Parc",
        "300 3rd St, San Francisco, CA  94107, United States"
      ],
      "location": {
        "lat": 37.783504486083984,
        "lng": -122.39889526367188
      },
      "structuredAddress": {
        "administrativeArea": "California",
        "subAdministrativeArea": "San Francisco County",
        "administrativeAreaCode": "CA",
        "locality": "San Francisco",
        "postCode": "94107",
        "subLocality": "Yerba Buena",
        "thoroughfare": "3rd St",
        "subThoroughfare": "300",
        "fullThoroughfare": "300 3rd St",
        "dependentLocalities": [
          "SOMA",
          "Yerba Buena"
        ]
      }
    },
    {
      "completionUrl": "/v1/search?q=Museum%20Parc%20Cleaners%20707%20Folsom%20St%2C%20San%20Francisco%2C%20CA%20%2094107%2C%20United%20States&metadata=ChwKFE11c2V1bSBQYXJjIENsZWFuZXJzEgQIABAGEjgKNjcwNyBGb2xzb20gU3QsIFNhbiBGcmFuY2lzY28sIENBICA5NDEwNywgVW5pdGVkIFN0YXRlcxgBKiIKEgkAAADgQuRCQBEAAACAi5lewBC24%2Bmk%2B5XkkfcBGK5NYggKBm11c2V1bYLxBAZtdXNldW2I8QQA2vEEFgkAAADgWV7wPxEAAADA9Sg7QDICZW7q8QQA",
      "displayLines": [
        "Museum Parc Cleaners",
        "707 Folsom St, San Francisco, CA  94107, United States"
      ],
      "location": {
        "lat": 37.78329086303711,
        "lng": -122.39913940429688
      },
      "structuredAddress": {
        "administrativeArea": "California",
        "subAdministrativeArea": "San Francisco County",
        "administrativeAreaCode": "CA",
        "locality": "San Francisco",
        "postCode": "94107",
        "subLocality": "Yerba Buena",
        "thoroughfare": "Folsom St",
        "subThoroughfare": "707",
        "fullThoroughfare": "707 Folsom St",
        "dependentLocalities": [
          "Yerba Buena"
        ]
      }
    },
    {
      "completionUrl": "/v1/search?q=San%20Jose%20Museum%20of%20Art%20110%20S%20Market%20St%2C%20San%20Jose%2C%20CA%20%2095113%2C%20United%20States&metadata=Ch4KFlNhbiBKb3NlIE11c2V1bSBvZiBBcnQSBAgJEAYSNQozMTEwIFMgTWFya2V0IFN0LCBTYW4gSm9zZSwgQ0EgIDk1MTEzLCBVbml0ZWQgU3RhdGVzGAEqIgoSCQAAAIC1qkJAEQAAAGD2eF7AEPjE0t6mkKvojQEYrk1iCAoGbXVzZXVtgvEEBm11c2V1bYjxBADa8QQWCQAAAGB6i1BAEQAAAOCj1ZVAMgJlburxBAA%3D",
      "displayLines": [
        "San Jose Museum of Art",
        "110 S Market St, San Jose, CA  95113, United States"
      ],
      "location": {
        "lat": 37.33366394042969,
        "lng": -121.8900375366211
      },
      "structuredAddress": {
        "administrativeArea": "California",
        "subAdministrativeArea": "Santa Clara County",
        "administrativeAreaCode": "CA",
        "locality": "San Jose",
        "postCode": "95113",
        "subLocality": "Downtown San Jose",
        "thoroughfare": "S Market St",
        "subThoroughfare": "110",
        "fullThoroughfare": "110 S Market St",
        "dependentLocalities": [
          "Downtown San Jose",
          "Downtown",
          "Central San Jose"
        ]
      }
    },
    {
      "completionUrl": "/v1/search?q=American%20Bookbinders%20Museum%20&metadata=CiMKG0FtZXJpY2FuIEJvb2tiaW5kZXJzIE11c2V1bRIECBUQBhgBKiEKEgkAAADgAORCQBEAAADgxZlewBCWhKLlqq6d1BQYrk1iCAoGbXVzZXVtgvEEBm11c2V1bYjxBADa8QQWCQAAAGADAfE%2FEQAAAEDhWlJAMgJlburxBAA%3D",
      "displayLines": [
        "American Bookbinders Museum"
      ],
      "location": {
        "lat": 37.78127670288086,
        "lng": -122.40270233154297
      },
      "structuredAddress": {
        "administrativeArea": "California",
        "subAdministrativeArea": "San Francisco County",
        "administrativeAreaCode": "CA",
        "locality": "San Francisco",
        "postCode": "94103",
        "subLocality": "Yerba Buena",
        "thoroughfare": "Clementina St",
        "subThoroughfare": "355",
        "fullThoroughfare": "355 Clementina St",
        "dependentLocalities": [
          "Yerba Buena"
        ]
      }
    }
  ]
}
```

## Endpoint

`GET https://maps-api.apple.com/v1/searchAutocomplete`

## Parameters

- `q` (string) *(required)*: The query to autocomplete. For example, `q=eiffel`.
- `excludePoiCategories` ([PoiCategory]): A comma-separated list of strings that describes the points of interest to exclude from the search results. For example, `excludePoiCategories=Restaurant,Cafe`. See [`PoiCategory`](poicategory.md) for a complete list of possible values.
- `includePoiCategories` ([PoiCategory]): A comma-separated list of strings that describes the points of interest to include in the search results. For example, `includePoiCategories=Restaurant,Cafe`. See [`PoiCategory`](poicategory.md) for a complete list of possible values.
- `lang` (Lang): The language the server uses when returning the response, specified using a BCP 47 language code. For example, for English, use `lang=en-US`.
- `limitToCountries` ([string]): A comma-separated list of two-letter ISO 3166-1 codes of the countries to limit the results to. For example, `limitToCountries=US,CA` limits the search to the United States and Canada. If you specify two or more countries, the results reflect the best available results for some or all of the countries rather than everything related to the query for those countries.
- `resultTypeFilter` ([SearchACResultType]): A comma-separated list of strings that describes the kind of result types to include in the response. For example, `resultTypeFilter=Poi`.
- `searchLocation` (SearchLocation): A location the app defines as a hint. Specify the location as a comma-separated string containing the latitude and longitude. For example, `searchLocation=37.78,-122.42`. If you don’t provide a `searchLocation`, the server uses `userLocation` and `searchRegion` as fallback hints.
- `searchRegion` (SearchRegion): A region the app defines as a hint for the search. Specify the region as a comma-separated string that describes the region in the form of a north-latitude, east-longitude, south-latitude, west-longitude string. If you don’t provide `searchLocation`, the server uses `userLocation` and `searchRegion` as fallback hints. For example, `searchRegion=38,-122.1,37.5,-122.5`.
- `userLocation` (UserLocation): The location of the user, specified as a comma-separated string that contains the latitude and longitude. For example, `userLocation=37.78,-122.42`. Certain APIs, such as Search, may opt to use the `userLocation`, if specified, as a fallback for the `searchLocation`.
- `searchRegionPriority` (string): A value that indicates the importance of the configured region.
- `includeAddressCategories` ([AddressCategory]): A comma-separated list of strings that describes the addresses to include in the search results. For example, `includeAddressCategories=SubLocality,PostalCode`. If you use this parameter, you must include `address` in `resultTypeFilter`. See [`AddressCategory`](addresscategory.md) for a complete list of possible values.
- `excludeAddressCategories` ([AddressCategory]): A comma-separated list of strings that describes the addresses to exclude in the search results. For example, `excludeAddressCategories=Country,AdministrativeArea`. If you use this parameter, you must include `address` in `resultTypeFilter`. See [`AddressCategory`](addresscategory.md) for a complete list of possible values.

## See Also

- [type AddressCategory](addresscategory.md)
  Search categories related to political geographical boundaries.
- [type SearchACResultType](searchacresulttype.md)
  An enumerated string that indicates the result type for the search request.
- [type SearchResultType](searchresulttype.md)
  An enumerated string that indicates the result type for the search autocomplete request.
- [object AlternateIdsResponse](alternateidsresponse.md)
  A list of alternate Place IDs and associated errors.
- [object AlternateIdsResponse.AlternateIds](alternateidsresponse/alternateids.md)
  Contains a list of alternate Place IDs for a given Place ID.
- [object PlacesResponse](placesresponse.md)
  A list of Place IDs and errors.
- [object PlacesResponse.PlaceLookupError](placesresponse/placelookuperror.md)
  An error associated with a lookup call.
- [Search for places that match specific criteria](-v1-search.md)
  Find places by name or by specific search criteria.
- [Search for a place using an identifier](-v1-place-:id.md)
  Obtain a Place object for a given Place ID.
- [Search for places using mulitple identifiers](-v1-place.md)
  Obtain a set of Place objects for a given set of Place IDs.
- [Obtain a list of alternate place identifiers](-v1-place-alternateids.md)
  Get a list of alternate Place IDs given one or more Place IDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemapsserverapi/-v1-searchautocomplete)*