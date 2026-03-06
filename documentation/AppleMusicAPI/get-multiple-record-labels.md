# Get Multiple Record Labels

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch one or more record labels by using their identifiers.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains the requested resource object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/record-labels?ids=1543990853
```

**Response**:

```json
{
    "data": [
        {
            "id": "1543990853",
            "type": "record-labels",
            "href": "/v1/catalog/us/record-labels/1543990853",
            "attributes": {
                "description": {
                    "standard": "Ninja Tune—formed in 1990 by Matt Black and Jon More (Coldcut)—has established itself as one of the world’s leading independent record labels. Now it’s a bona fide global music institution, synonymous with diverse, uncompromising releases and equally visionary artists—from breaking to GRAMMY-nominated acts—committed to pushing the boundaries of music. (From the label)"
                },
                "url": "https: //music.apple.com/us/label/ninja-tune/1543990853",
                "artwork": {
                    "width": 1080,
                    "height": 1080,
                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/Features114/v4/2b/20/be/2b20be3f-6f19-3701-074e-b233964caaa7/QkwtTVMtV1ctTmluamFfVHVuZS1BREFNX0lEPTE1NDM5OTA4NTMucG5n.png/{w}x{h}bb.jpg",
                    "bgColor": "111111",
                    "textColor1": "93c7d9",
                    "textColor2": "89b6c6",
                    "textColor3": "759caa",
                    "textColor4": "6d8f9b"
                },
                "name": "Ninja Tune"
            }
        }
    ]
}

```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/record-labels`

## Parameters

- `extend` ([string]): A list of attribute extensions to apply to resources in the response.
- `ids` ([string]) *(required)*: The unique identifiers for the record labels. The maximum fetch limit is 100.
- `include` ([string]): Additional relationships to include in the fetch.
- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.

## See Also

- [object RecordLabels](recordlabels.md)
  A resource object that represents a record label.
- [object RecordLabelsResponse](recordlabelsresponse.md)
  The response to a request for record labels.
- [Get a Catalog Record Label](get-a-record-label.md)
  Fetch a record label by using its identifier.
- [Get a Catalog Record Label’s Relationship View Directly by Name](fetch-a-view-on-this-resource-by-name-5uhxd.md)
  Fetch related resources for a single record label’s relationship view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/get-multiple-record-labels)*