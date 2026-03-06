# Geocode an address

**Framework**: Apple Maps Server API  
**Kind**: httpRequest

Returns the latitude and longitude of the address you specify.

**Availability**:
- Apple Maps Server API 1.2+

#### Discussion

##### Example

**Request**:

```None
curl -si -H "Authorization: Bearer <maps_access_token>" "https://maps-api.apple.com/v1/geocode?q=Apple%20Park%2C%20Cupertino%2C%20CA"
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

`GET https://maps-api.apple.com/v1/geocode`

## Parameters

- `q` (string) *(required)*: The address to geocode. For example: `q=1 Apple Park, Cupertino, CA`
- `limitToCountries` ([string]): A comma-separated list of two-letter ISO 3166-1 codes to limit the results to. For example: `limitToCountries=US,CA`. If you specify two or more countries, the results reflect the best available results for some or all of the countries rather than everything related to the query for those countries.
- `lang` (Lang): The language the server should use when returning the response, specified using a BCP 47 language code. For example, for English use `lang=en-US`.
- `searchLocation` (SearchLocation): A location defined by the application as a hint. Specify the location as a comma-separated string containing the latitude and longitude. For example, `searchLocation=37.78,-122.42`.
- `searchRegion` (SearchRegion): A region the app defines as a hint. Specify the region specified as a comma-separated string that describes the region in the form north-latitude, east-longitude, south-latitude, west-longitude. For example, `searchRegion=38,-122.1,37.5,-122.5`.
- `userLocation` (UserLocation): The location of the user, specified as a comma-separated string that contains the latitude and longitude. For example: `userLocation=37.78,-122.42`. Certain APIs, such as Searching, may opt to use the `userLocation`, if specified, as a fallback for the `searchLocation`.

## See Also

- [Reverse geocode a location](-v1-reversegeocode.md)
  Returns an array of addresses present at the coordinates you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemapsserverapi/-v1-geocode)*