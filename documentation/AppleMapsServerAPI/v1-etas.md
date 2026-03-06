# Determine estimated arrival times and distances to one or more destinations

**Framework**: Apple Maps Server API  
**Kind**: httpRequest

Returns the estimated time of arrival (ETA) and distance between starting and ending locations.

**Availability**:
- Apple Maps Server API 1.2+

#### Discussion

##### Example

**Request**:

```None
curl -si -H "Authorization: Bearer <maps_access_token>" "https://maps-api.apple.com/v1/etas?origin=37.331423,-122.030503&destinations=37.32556561130194,-121.94635203581443|37.44176585512703,-122.17259315798667"
```

**Response**:

```json
{
  "etas": [
    {
      "destination": {
        "latitude": 37.32556561130194,
        "longitude": -121.94635203581443
      },
      "transportType": "AUTOMOBILE",
      "distanceMeters": 9550,
      "expectedTravelTimeSeconds": 975,
      "staticTravelTimeSeconds": 540
    },
    {
      "destination": {
        "latitude": 37.44176585512703,
        "longitude": -122.17259315798667
      },
      "transportType": "AUTOMOBILE",
      "distanceMeters": 23286,
      "expectedTravelTimeSeconds": 1336,
      "staticTravelTimeSeconds": 1039
    }
  ]
}
```

## Endpoint

`GET https://maps-api.apple.com/v1/etas`

## Parameters

- `origin` (string) *(required)*: The starting point for estimated arrival time requests, specified as a comma-separated string that contains the latitude and longitude. For example, `origin=37.331423,-122.030503`.
- `destinations` ([string]) *(required)*: Destination coordinates represented as pairs of latitude and longitude separated by a vertical bar character (”|”). For example, `destinations=37.32556561130194,-121.94635203581443|37.44176585512703,-122.17259315798667`. The parameter must specify at least one destination coordinate, but no more than 10 destinations. Specify the location as a comma-separated string that contains the latitude and longitude.
- `transportType` (string): The mode of transportation to use when estimating arrival times.
- `departureDate` (string): The time of departure to use in an estimated arrival time request, in ISO 8601 format in UTC time. For example, `departureDate=2020-09-15T16:42:00Z`. If you don’t specify a departure date, the server uses the current date and time when you make the request.
- `arrivalDate` (string): The intended time of arrival in ISO 8601 format in UTC time.

## See Also

- [Search for directions and estimated travel time between locations](-v1-directions.md)
  Find directions by specific criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemapsserverapi/-v1-etas)*