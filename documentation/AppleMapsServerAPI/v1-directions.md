# Search for directions and estimated travel time between locations

**Framework**: Apple Maps Server API  
**Kind**: httpRequest

Find directions by specific criteria.

**Availability**:
- Apple Maps Server API 1.2+

#### Discussion

##### Example

**Request**:

```None
curl -si -H "Authorization: Bearer <maps_access_token>" \
"https://maps-api.apple.com/v1/directions?origin=37.7857,-122.4011&destination=San Francisco City Hall, CA"
```

**Response**:

```json
{
  "destination": {
    "center": {
      "latitude": 37.7753881,
      "longitude": -122.3931773
    },
    "displayMapRegion": {
      "southLatitude": 37.7708965235794,
      "westLongitude": -122.39885983149095,
      "northLatitude": 37.7798796764206,
      "eastLongitude": -122.38749476850906
    },
    "name": "San Francisco Public Library - Mission Bay",
    "formattedAddressLines": [
      "960 4th St",
      "San Francisco, CA  94158",
      "United States"
    ],
    "structuredAddress": {
      "administrativeArea": "California",
      "subAdministrativeArea": "San Francisco County",
      "administrativeAreaCode": "CA",
      "locality": "San Francisco",
      "postCode": "94158",
      "subLocality": "Mission Bay North",
      "thoroughfare": "4th St",
      "subThoroughfare": "960",
      "fullThoroughfare": "960 4th St",
      "dependentLocalities": [
        "Mission Bay North",
        "Mission Bay"
      ]
    },
    "country": "United States",
    "countryCode": "US",
    "telephone": "+14153552838",
    "urls": [
      "https://sfpl.org/locations/mission-bay"
    ]
  },
  "routes": [
    {
      "name": "4th St",
      "distanceMeters": 2033,
      "durationSeconds": 506,
      "transportType": "AUTOMOBILE",
      "stepIndexes": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7
      ],
      "hasTolls": true
    },
    {
      "name": "2nd St",
      "distanceMeters": 2342,
      "durationSeconds": 592,
      "transportType": "AUTOMOBILE",
      "stepIndexes": [
        8,
        9,
        10,
        11,
        12,
        13
      ],
      "hasTolls": true
    },
    {
      "name": "Harrison St",
      "distanceMeters": 2029,
      "durationSeconds": 548,
      "transportType": "AUTOMOBILE",
      "stepIndexes": [
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23
      ],
      "hasTolls": true
    }
  ],
  "steps": [
    {
      "stepPathIndex": 0,
      "distanceMeters": 0,
      "durationSeconds": 0
    },
    {
      "stepPathIndex": 1,
      "distanceMeters": 37,
      "durationSeconds": 11,
      "instructions": "Turn right onto Minna St"
    },
    {
      "stepPathIndex": 2,
      "distanceMeters": 188,
      "durationSeconds": 76,
      "instructions": "Turn right onto New Montgomery St"
    },
    {
      "stepPathIndex": 3,
      "distanceMeters": 127,
      "durationSeconds": 27,
      "instructions": "Turn right onto Howard St"
    },
    {
      "stepPathIndex": 4,
      "distanceMeters": 468,
      "durationSeconds": 104,
      "instructions": "Turn left onto 4th St"
    },
    {
      "stepPathIndex": 5,
      "distanceMeters": 446,
      "durationSeconds": 71,
      "instructions": "Keep right onto 4th St"
    },
    {
      "stepPathIndex": 6,
      "distanceMeters": 136,
      "durationSeconds": 48,
      "instructions": "Keep right onto 4th St"
    },
    {
      "stepPathIndex": 7,
      "distanceMeters": 633,
      "durationSeconds": 169,
      "instructions": "The destination is on your right"
    },
    {
      "stepPathIndex": 8,
      "distanceMeters": 0,
      "durationSeconds": 0
    },
    {
      "stepPathIndex": 9,
      "distanceMeters": 98,
      "durationSeconds": 38,
      "instructions": "Turn right onto Mission St"
    },
    {
      "stepPathIndex": 10,
      "distanceMeters": 279,
      "durationSeconds": 81,
      "instructions": "Turn right onto 2nd St"
    },
    {
      "stepPathIndex": 11,
      "distanceMeters": 1265,
      "durationSeconds": 282,
      "instructions": "Turn right onto King St"
    },
    {
      "stepPathIndex": 12,
      "distanceMeters": 589,
      "durationSeconds": 156,
      "instructions": "Turn left onto 4th St"
    },
    {
      "stepPathIndex": 13,
      "distanceMeters": 112,
      "durationSeconds": 36,
      "instructions": "The destination is on your right"
    },
    {
      "stepPathIndex": 14,
      "distanceMeters": 0,
      "durationSeconds": 0
    },
    {
      "stepPathIndex": 15,
      "distanceMeters": 37,
      "durationSeconds": 11,
      "instructions": "Turn right onto Minna St"
    },
    {
      "stepPathIndex": 16,
      "distanceMeters": 188,
      "durationSeconds": 76,
      "instructions": "Turn right onto New Montgomery St"
    },
    {
      "stepPathIndex": 17,
      "distanceMeters": 127,
      "durationSeconds": 26,
      "instructions": "Turn right onto Howard St"
    },
    {
      "stepPathIndex": 18,
      "distanceMeters": 50,
      "durationSeconds": 18,
      "instructions": "Turn left onto Hawthorne St"
    },
    {
      "stepPathIndex": 19,
      "distanceMeters": 384,
      "durationSeconds": 107,
      "instructions": "Turn right onto Harrison St"
    },
    {
      "stepPathIndex": 20,
      "distanceMeters": 414,
      "durationSeconds": 87,
      "instructions": "Turn left onto 4th St"
    },
    {
      "stepPathIndex": 21,
      "distanceMeters": 61,
      "durationSeconds": 6,
      "instructions": "Keep right onto 4th St"
    },
    {
      "stepPathIndex": 22,
      "distanceMeters": 136,
      "durationSeconds": 48,
      "instructions": "Keep right onto 4th St"
    },
    {
      "stepPathIndex": 23,
      "distanceMeters": 633,
      "durationSeconds": 169,
      "instructions": "The destination is on your right"
    }
  ],
  "stepPaths": [
    [
      {
        "latitude": 37.7856,
        "longitude": -122.401214
      }
    ],
    [
      {
        "latitude": 37.7856,
        "longitude": -122.401214
      },
      {
        "latitude": 37.785801,
        "longitude": -122.401471
      },
      {
        "latitude": 37.785831,
        "longitude": -122.401509
      }
    ],
    [
      {
        "latitude": 37.785831,
        "longitude": -122.401509
      },
      {
        "latitude": 37.786005,
        "longitude": -122.401285
      },
      {
        "latitude": 37.786275,
        "longitude": -122.40093
      },
      {
        "latitude": 37.786346,
        "longitude": -122.400838
      },
      {
        "latitude": 37.786593,
        "longitude": -122.400526
      },
      {
        "latitude": 37.786625,
        "longitude": -122.400485
      },
      {
        "latitude": 37.78699,
        "longitude": -122.400029
      },
      {
        "latitude": 37.78702,
        "longitude": -122.39999
      }
    ],
    [
      {
        "latitude": 37.78702,
        "longitude": -122.39999
      },
      {
        "latitude": 37.786642,
        "longitude": -122.399515
      },
      {
        "latitude": 37.786247,
        "longitude": -122.399017
      },
      {
        "latitude": 37.786214,
        "longitude": -122.398975
      }
    ],
    [
      {
        "latitude": 37.786214,
        "longitude": -122.398975
      },
      {
        "latitude": 37.785894,
        "longitude": -122.399378
      },
      {
        "latitude": 37.785449,
        "longitude": -122.399937
      },
      {
        "latitude": 37.785385,
        "longitude": -122.400022
      },
      {
        "latitude": 37.785029,
        "longitude": -122.40049
      },
      {
        "latitude": 37.784492,
        "longitude": -122.401168
      },
      {
        "latitude": 37.783892,
        "longitude": -122.401953
      },
      {
        "latitude": 37.78385,
        "longitude": -122.401977
      },
      {
        "latitude": 37.783381,
        "longitude": -122.402571
      },
      {
        "latitude": 37.783279,
        "longitude": -122.4027
      },
      {
        "latitude": 37.783247,
        "longitude": -122.402741
      }
    ],
    [
      {
        "latitude": 37.783247,
        "longitude": -122.402741
      },
      {
        "latitude": 37.782702,
        "longitude": -122.402001
      },
      {
        "latitude": 37.78264,
        "longitude": -122.401905
      },
      {
        "latitude": 37.782475,
        "longitude": -122.401684
      },
      {
        "latitude": 37.782045,
        "longitude": -122.401162
      },
      {
        "latitude": 37.781964,
        "longitude": -122.401089
      },
      {
        "latitude": 37.781595,
        "longitude": -122.400624
      },
      {
        "latitude": 37.7814,
        "longitude": -122.40038
      },
      {
        "latitude": 37.781224,
        "longitude": -122.400163
      },
      {
        "latitude": 37.780806,
        "longitude": -122.399633
      },
      {
        "latitude": 37.780458,
        "longitude": -122.399179
      },
      {
        "latitude": 37.780424,
        "longitude": -122.399139
      }
    ],
    [
      {
        "latitude": 37.780424,
        "longitude": -122.399139
      },
      {
        "latitude": 37.780349,
        "longitude": -122.39914
      },
      {
        "latitude": 37.780322,
        "longitude": -122.399118
      },
      {
        "latitude": 37.779613,
        "longitude": -122.398242
      },
      {
        "latitude": 37.779583,
        "longitude": -122.398206
      },
      {
        "latitude": 37.779525,
        "longitude": -122.398136
      }
    ],
    [
      {
        "latitude": 37.779525,
        "longitude": -122.398136
      },
      {
        "latitude": 37.779381,
        "longitude": -122.39798
      },
      {
        "latitude": 37.779083,
        "longitude": -122.397609
      },
      {
        "latitude": 37.778715,
        "longitude": -122.397147
      },
      {
        "latitude": 37.778292,
        "longitude": -122.39661
      },
      {
        "latitude": 37.778146,
        "longitude": -122.39641
      },
      {
        "latitude": 37.777681,
        "longitude": -122.395824
      },
      {
        "latitude": 37.777433,
        "longitude": -122.395515
      },
      {
        "latitude": 37.777077,
        "longitude": -122.395067
      },
      {
        "latitude": 37.77639,
        "longitude": -122.394196
      },
      {
        "latitude": 37.776182,
        "longitude": -122.393998
      },
      {
        "latitude": 37.775764,
        "longitude": -122.393485
      },
      {
        "latitude": 37.775721,
        "longitude": -122.393403
      },
      {
        "latitude": 37.775503,
        "longitude": -122.393056
      }
    ],
    [
      {
        "latitude": 37.7856,
        "longitude": -122.401214
      }
    ],
    [
      {
        "latitude": 37.7856,
        "longitude": -122.401214
      },
      {
        "latitude": 37.785831,
        "longitude": -122.401509
      },
      {
        "latitude": 37.786194,
        "longitude": -122.401958
      },
      {
        "latitude": 37.786227,
        "longitude": -122.402
      }
    ],
    [
      {
        "latitude": 37.786227,
        "longitude": -122.402
      },
      {
        "latitude": 37.786309,
        "longitude": -122.401901
      },
      {
        "latitude": 37.786356,
        "longitude": -122.4019
      },
      {
        "latitude": 37.786857,
        "longitude": -122.401265
      },
      {
        "latitude": 37.78745,
        "longitude": -122.400514
      },
      {
        "latitude": 37.787984,
        "longitude": -122.399844
      },
      {
        "latitude": 37.788016,
        "longitude": -122.399804
      }
    ],
    [
      {
        "latitude": 37.788016,
        "longitude": -122.399804
      },
      {
        "latitude": 37.787976,
        "longitude": -122.399753
      },
      {
        "latitude": 37.787588,
        "longitude": -122.399279
      },
      {
        "latitude": 37.787208,
        "longitude": -122.398802
      },
      {
        "latitude": 37.786773,
        "longitude": -122.398256
      },
      {
        "latitude": 37.786648,
        "longitude": -122.398099
      },
      {
        "latitude": 37.786342,
        "longitude": -122.397714
      },
      {
        "latitude": 37.785968,
        "longitude": -122.397245
      },
      {
        "latitude": 37.785814,
        "longitude": -122.397053
      },
      {
        "latitude": 37.785549,
        "longitude": -122.39672
      },
      {
        "latitude": 37.784909,
        "longitude": -122.395914
      },
      {
        "latitude": 37.784796,
        "longitude": -122.395772
      },
      {
        "latitude": 37.784385,
        "longitude": -122.395262
      },
      {
        "latitude": 37.784319,
        "longitude": -122.395183
      },
      {
        "latitude": 37.78424,
        "longitude": -122.395082
      },
      {
        "latitude": 37.784022,
        "longitude": -122.394811
      },
      {
        "latitude": 37.783959,
        "longitude": -122.394731
      },
      {
        "latitude": 37.783511,
        "longitude": -122.39417
      },
      {
        "latitude": 37.783078,
        "longitude": -122.393621
      },
      {
        "latitude": 37.782823,
        "longitude": -122.393301
      },
      {
        "latitude": 37.782655,
        "longitude": -122.393089
      },
      {
        "latitude": 37.782459,
        "longitude": -122.392841
      },
      {
        "latitude": 37.782277,
        "longitude": -122.392612
      },
      {
        "latitude": 37.781851,
        "longitude": -122.392078
      },
      {
        "latitude": 37.780622,
        "longitude": -122.390546
      },
      {
        "latitude": 37.779965,
        "longitude": -122.389717
      },
      {
        "latitude": 37.779936,
        "longitude": -122.38968
      }
    ],
    [
      {
        "latitude": 37.779936,
        "longitude": -122.38968
      },
      {
        "latitude": 37.779399,
        "longitude": -122.390377
      },
      {
        "latitude": 37.779116,
        "longitude": -122.390744
      },
      {
        "latitude": 37.779074,
        "longitude": -122.390798
      },
      {
        "latitude": 37.778972,
        "longitude": -122.390929
      },
      {
        "latitude": 37.77819,
        "longitude": -122.391929
      },
      {
        "latitude": 37.777876,
        "longitude": -122.392291
      },
      {
        "latitude": 37.777362,
        "longitude": -122.392939
      },
      {
        "latitude": 37.777296,
        "longitude": -122.393024
      },
      {
        "latitude": 37.777262,
        "longitude": -122.393069
      },
      {
        "latitude": 37.776946,
        "longitude": -122.393506
      },
      {
        "latitude": 37.776509,
        "longitude": -122.394049
      },
      {
        "latitude": 37.77648,
        "longitude": -122.394085
      },
      {
        "latitude": 37.77639,
        "longitude": -122.394196
      },
      {
        "latitude": 37.776182,
        "longitude": -122.393998
      }
    ],
    [
      {
        "latitude": 37.776182,
        "longitude": -122.393998
      },
      {
        "latitude": 37.776122,
        "longitude": -122.393927
      },
      {
        "latitude": 37.775764,
        "longitude": -122.393485
      },
      {
        "latitude": 37.775721,
        "longitude": -122.393403
      },
      {
        "latitude": 37.775503,
        "longitude": -122.393056
      }
    ],
    [
      {
        "latitude": 37.7856,
        "longitude": -122.401214
      }
    ],
    [
      {
        "latitude": 37.7856,
        "longitude": -122.401214
      },
      {
        "latitude": 37.785801,
        "longitude": -122.401471
      },
      {
        "latitude": 37.785831,
        "longitude": -122.401509
      }
    ],
    [
      {
        "latitude": 37.785831,
        "longitude": -122.401509
      },
      {
        "latitude": 37.786005,
        "longitude": -122.401285
      },
      {
        "latitude": 37.786275,
        "longitude": -122.40093
      },
      {
        "latitude": 37.786346,
        "longitude": -122.400838
      },
      {
        "latitude": 37.786593,
        "longitude": -122.400526
      },
      {
        "latitude": 37.786625,
        "longitude": -122.400485
      },
      {
        "latitude": 37.78699,
        "longitude": -122.400029
      },
      {
        "latitude": 37.78702,
        "longitude": -122.39999
      }
    ],
    [
      {
        "latitude": 37.78702,
        "longitude": -122.39999
      },
      {
        "latitude": 37.786642,
        "longitude": -122.399515
      },
      {
        "latitude": 37.786247,
        "longitude": -122.399017
      },
      {
        "latitude": 37.786214,
        "longitude": -122.398975
      }
    ],
    [
      {
        "latitude": 37.786214,
        "longitude": -122.398975
      },
      {
        "latitude": 37.785894,
        "longitude": -122.399378
      }
    ],
    [
      {
        "latitude": 37.785894,
        "longitude": -122.399378
      },
      {
        "latitude": 37.785565,
        "longitude": -122.398968
      },
      {
        "latitude": 37.785354,
        "longitude": -122.398702
      },
      {
        "latitude": 37.785224,
        "longitude": -122.39854
      },
      {
        "latitude": 37.785195,
        "longitude": -122.398503
      },
      {
        "latitude": 37.78467,
        "longitude": -122.39783
      },
      {
        "latitude": 37.784085,
        "longitude": -122.397093
      },
      {
        "latitude": 37.783473,
        "longitude": -122.396339
      },
      {
        "latitude": 37.783442,
        "longitude": -122.396302
      }
    ],
    [
      {
        "latitude": 37.783442,
        "longitude": -122.396302
      },
      {
        "latitude": 37.782864,
        "longitude": -122.397031
      },
      {
        "latitude": 37.782569,
        "longitude": -122.397405
      },
      {
        "latitude": 37.78205,
        "longitude": -122.398062
      },
      {
        "latitude": 37.781805,
        "longitude": -122.398364
      },
      {
        "latitude": 37.781249,
        "longitude": -122.399072
      },
      {
        "latitude": 37.781224,
        "longitude": -122.399105
      },
      {
        "latitude": 37.78084,
        "longitude": -122.399589
      },
      {
        "latitude": 37.780806,
        "longitude": -122.399633
      }
    ],
    [
      {
        "latitude": 37.780806,
        "longitude": -122.399633
      },
      {
        "latitude": 37.780753,
        "longitude": -122.399559
      },
      {
        "latitude": 37.780458,
        "longitude": -122.399179
      },
      {
        "latitude": 37.780424,
        "longitude": -122.399139
      }
    ],
    [
      {
        "latitude": 37.780424,
        "longitude": -122.399139
      },
      {
        "latitude": 37.780349,
        "longitude": -122.39914
      },
      {
        "latitude": 37.780322,
        "longitude": -122.399118
      },
      {
        "latitude": 37.779613,
        "longitude": -122.398242
      },
      {
        "latitude": 37.779583,
        "longitude": -122.398206
      },
      {
        "latitude": 37.779525,
        "longitude": -122.398136
      }
    ],
    [
      {
        "latitude": 37.779525,
        "longitude": -122.398136
      },
      {
        "latitude": 37.779381,
        "longitude": -122.39798
      },
      {
        "latitude": 37.779083,
        "longitude": -122.397609
      },
      {
        "latitude": 37.778715,
        "longitude": -122.397147
      },
      {
        "latitude": 37.778292,
        "longitude": -122.39661
      },
      {
        "latitude": 37.778146,
        "longitude": -122.39641
      },
      {
        "latitude": 37.777681,
        "longitude": -122.395824
      },
      {
        "latitude": 37.777433,
        "longitude": -122.395515
      },
      {
        "latitude": 37.777077,
        "longitude": -122.395067
      },
      {
        "latitude": 37.77639,
        "longitude": -122.394196
      },
      {
        "latitude": 37.776182,
        "longitude": -122.393998
      },
      {
        "latitude": 37.775764,
        "longitude": -122.393485
      },
      {
        "latitude": 37.775721,
        "longitude": -122.393403
      },
      {
        "latitude": 37.775503,
        "longitude": -122.393056
      }
    ]
  ]
}
```

## Endpoint

`GET https://maps-api.apple.com/v1/directions`

## Parameters

- `origin` (string) *(required)*: The starting location as an address, or coordinates you specify as latitude, longitude. For example, `origin=37.7857,-122.4011`
- `destination` (string) *(required)*: The destination as an address, or coordinates you specify as latitude, longitude. For example, `destination=San Francisco City Hall, CA`
- `arrivalDate` (string): The date and time to arrive at the destination in ISO 8601 format in UTC time. For example, `2023-04-15T16:42:00Z`. You can specify only `arrivalDate` or `departureDate`. If you don’t specify either option, the `departureDate` defaults to *now*, which the server interprets as the current time.
- `avoid` ([DirectionsAvoid]): A comma-separated list of the features to avoid when calculating direction routes. For example, `avoid=Tolls`. See [`DirectionsAvoid`](directionsavoid.md) for a complete list of possible values.
- `departureDate` (string): The date and time to depart from the origin in ISO 8601 format in UTC time. For example, `2023-04-15T16:42:00Z`. You can only specify `arrivalDate` or `departureDate`. If you don’t specify either option, the `departureDate` defaults to *now*, which the server interprets as the current time.
- `lang` (Lang): The language the server uses when returning the response, specified using a BCP 47 language code. For example, for English, use `lang=en-US`.
- `requestsAlternateRoutes` (boolean): When you set this to `true`, the server returns additional routes, when available. For example, `requestsAlternateRoutes=true.`
- `searchLocation` (SearchLocation): A `searchLocation` the app defines as a hint for the query input for `origin` or `destination`. Specify the location as a comma-separated string that contains the latitude and longitude. For example, `37.7857,-122.4011`. If you don’t provide a `searchLocation`, the server uses `userLocation` and searchLocation as fallback hints.
- `searchRegion` (SearchRegion): A region the app defines as a hint for the query input for `origin` or `destination`. Specify the region as a comma-separated string that describes the region in the form of a north-latitude, east-longitude, south-latitude, west-longitude string. For example, 38,-122.1,37.5,-122.5. If you don’t provide a `searchLocation`, the server uses `userLocation` and `searchRegion` as fallback hints.
- `transportType` (string): The mode of transportation the server returns directions for.
- `userLocation` (UserLocation): The location of the user, specified as a comma-separated string that contains the latitude and longitude. For example, `userLocation=37.78,-122.42`. If you don’t provide a `searchLocation`, the server uses `userLocation` and `searchRegion` as fallback hints.

## See Also

- [Determine estimated arrival times and distances to one or more destinations](-v1-etas.md)
  Returns the estimated time of arrival (ETA) and distance between starting and ending locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemapsserverapi/-v1-directions)*