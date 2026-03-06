# Get Catalog Top Charts Genres

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch all genres for the current top charts.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains an array of `Genre` objects. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/genres
```

**Response**:

```json
{
    "data": [
        {
            "attributes": {
                "name": "Music"
            },
            "href": "/v1/catalog/us/genres/34",
            "id": "34",
            "type": "genres"
        },
        {
            "attributes": {
                "name": "Alternative"
            },
            "href": "/v1/catalog/us/genres/20",
            "id": "20",
            "type": "genres"
        },
        {
            "attributes": {
                "name": "Blues"
            },
            "href": "/v1/catalog/us/genres/2",
            "id": "2",
            "type": "genres"
        },
        {
            "attributes": {
                "name": "Children's Music"
            },
            "href": "/v1/catalog/us/genres/4",
            "id": "4",
            "type": "genres"
        },
        {
            "attributes": {
                "name": "Christian & Gospel"
            },
            "href": "/v1/catalog/us/genres/22",
            "id": "22",
            "type": "genres"
        },
        {
            "attributes": {
                "name": "Classical"
            },
            "href": "/v1/catalog/us/genres/5",
            "id": "5",
            "type": "genres"
        },
        {
            "attributes": {
                "name": "Comedy"
            },
            "href": "/v1/catalog/us/genres/3",
            "id": "3",
            "type": "genres"
        },
        {
            "attributes": {
                "name": "Country"
            },
            "href": "/v1/catalog/us/genres/6",
            "id": "6",
            "type": "genres"
        },
        {
            "attributes": {
                "name": "Dance"
            },
            "href": "/v1/catalog/us/genres/17",
            "id": "17",
            "type": "genres"
        },
        {
            "attributes": {
                "name": "Electronic"
            },
            "href": "/v1/catalog/us/genres/7",
            "id": "7",
            "type": "genres"
        },
        {
            "attributes": {
                "name": "Fitness & Workout"
            },
            "href": "/v1/catalog/us/genres/50",
            "id": "50",
            "type": "genres"
        },
        {
            "attributes": {
                "name": "Hip-Hop/Rap"
            },
            "href": "/v1/catalog/us/genres/18",
            "id": "18",
            "type": "genres"
        },
        {
            "attributes": {
                "name": "Jazz"
            },
            "href": "/v1/catalog/us/genres/11",
            "id": "11",
            "type": "genres"
        },
        {
            "attributes": {
                "name": "K-Pop"
            },
            "href": "/v1/catalog/us/genres/51",
            "id": "51",
            "type": "genres"
        },
        {
            "attributes": {
                "name": "Latino"
            },
            "href": "/v1/catalog/us/genres/12",
            "id": "12",
            "type": "genres"
        },
        {
            "attributes": {
                "name": "Metal"
            },
            "href": "/v1/catalog/us/genres/1153",
            "id": "1153",
            "type": "genres"
        },
        {
            "attributes": {
                "name": "Music Videos"
            },
            "href": "/v1/catalog/us/genres/31",
            "id": "31",
            "type": "genres"
        },
        {
            "attributes": {
                "name": "Pop"
            },
            "href": "/v1/catalog/us/genres/14",
            "id": "14",
            "type": "genres"
        },
        {
            "attributes": {
                "name": "R&B/Soul"
            },
            "href": "/v1/catalog/us/genres/15",
            "id": "15",
            "type": "genres"
        },
        {
            "attributes": {
                "name": "Reggae"
            },
            "href": "/v1/catalog/us/genres/24",
            "id": "24",
            "type": "genres"
        },
        {
            "attributes": {
                "name": "Rock"
            },
            "href": "/v1/catalog/us/genres/21",
            "id": "21",
            "type": "genres"
        },
        {
            "attributes": {
                "name": "Singer/Songwriter"
            },
            "href": "/v1/catalog/us/genres/10",
            "id": "10",
            "type": "genres"
        },
        {
            "attributes": {
                "name": "Soundtrack"
            },
            "href": "/v1/catalog/us/genres/16",
            "id": "16",
            "type": "genres"
        },
        {
            "attributes": {
                "name": "World"
            },
            "href": "/v1/catalog/us/genres/19",
            "id": "19",
            "type": "genres"
        }
    ]
}
```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/genres`

## Parameters

- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.
- `offset` (string): The next page or group of objects to fetch.
- `include` ([string]): Additional relationships to include in the fetch.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object Genres](genres.md)
  A resource object that represents a music genre.
- [object GenresResponse](genresresponse.md)
  The response to a genres request.
- [Get a Catalog Genre](get-a-genre.md)
  Fetch a genre by using its identifier.
- [Get Multiple Catalog Genres](get-multiple-genres.md)
  Fetch one or more genres for a specific storefront.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-all-genres)*