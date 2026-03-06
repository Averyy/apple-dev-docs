# Reverse geocode a location

**Framework**: Apple Maps Server API  
**Kind**: httpRequest

Returns an array of addresses present at the coordinates you provide.

**Availability**:
- Apple Maps Server API 1.2+

#### Discussion

##### Example

**Request**:

```None
curl -si -H "Authorization: Bearer <maps_access_token>" "https://maps-api.apple.com/v1/reverseGeocode?loc=37.3301996%2C-122.0106415"
```

**Response**:

```json
{
  "results": [
    {
      "coordinate": {
        "latitude": 37.3301996,
        "longitude": -122.0106415
      },
      "displayMapRegion": {
        "southLatitude": 37.3257080235794,
        "westLongitude": -122.01629018770203,
        "northLatitude": 37.3346911764206,
        "eastLongitude": -122.00499281229798
      },
      "name": "Apple Park Way",
      "formattedAddressLines": [
        "Apple Park Way",
        "Cupertino, CA  95014",
        "United States"
      ],
      "structuredAddress": {
        "administrativeArea": "California",
        "administrativeAreaCode": "CA",
        "locality": "Cupertino",
        "postCode": "95014",
        "thoroughfare": "Apple Park Way",
        "fullThoroughfare": "Apple Park Way",
        "areasOfInterest": [
          "Apple Park"
        ]
      },
      "country": "United States",
      "countryCode": "US"
    }
  ]
}
```

## Endpoint

`GET https://maps-api.apple.com/v1/reverseGeocode`

## Parameters

- `loc` (string) *(required)*: The coordinate to reverse geocode as a comma-separated string that contains the latitude and longitude. For example: `loc=37.3316851,-122.0300674.`
- `lang` (Lang): The language the server uses when returning the response, specified using a BCP 47 language code. For example, for English, use `lang=en-US`.

## See Also

- [Geocode an address](-v1-geocode.md)
  Returns the latitude and longitude of the address you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemapsserverapi/-v1-reversegeocode)*