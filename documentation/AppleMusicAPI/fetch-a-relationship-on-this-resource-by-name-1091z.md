# Get a Catalog Curator's Relationship Directly by Name

**Framework**: Apple Music API  
**Kind**: httpRequest

Fetch a curator’s relationship by using its identifier.

**Availability**:
- Apple Music 1.0+

#### Discussion

If successful, the HTTP status code is 200 (OK) and the `data` array contains a single [`Curators.Relationships`](curators/relationships-data.dictionary.md) object. If unsuccessful, the HTTP status code indicates the error and the details are in the `errors` array. For more information, see [`Handling Requests and Responses`](handling-requests-and-responses.md).

##### Example

**Request**:

```None
https://api.music.apple.com/v1/catalog/us/curators/976439455/playlists
```

**Response**:

```json
{
    "next": "/v1/catalog/us/curators/976439455/playlists?offset=10",
    "data": [
        {
            "id": "pl.cdb488a4f4f546faa7ca2949ebc0a7c2",
            "type": "playlists",
            "href": "/v1/catalog/us/playlists/pl.cdb488a4f4f546faa7ca2949ebc0a7c2",
            "attributes": {
                "curatorName": "Pitchfork",
                "artwork": {
                    "width": 2400,
                    "height": 2400,
                    "url": "https: //is4-ssl.mzstatic.com/image/thumb/SG-MQ-US-032-Image000001/v4/7e/74/8f/7e748fdf-248a-d7b5-0e37-75980d1da98b/image/{w}x{h}cc.jpg"
                },
                "playParams": {
                    "id": "pl.cdb488a4f4f546faa7ca2949ebc0a7c2",
                    "kind": "playlist",
                    "versionHash": "5d1cf672abdfb71313e69bfd88baa7a376a18e062a5822e16fcde900e76fc698"
                },
                "playlistType": "external",
                "lastModifiedDate": "2022-03-08T17: 05: 56Z",
                "url": "https: //music.apple.com/us/playlist/pitchfork-music-festival-2022/pl.cdb488a4f4f546faa7ca2949ebc0a7c2",
                "isChart": false,
                "name": "Pitchfork Music Festival 2022"
            }
        },
        {
            "id": "pl.adc9cc99b91649188b6ea75d39048836",
            "type": "playlists",
            "href": "/v1/catalog/us/playlists/pl.adc9cc99b91649188b6ea75d39048836",
            "attributes": {
                "curatorName": "Pitchfork",
                "artwork": {
                    "width": 2400,
                    "height": 2400,
                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/ifkK6yLt6LF4IFv16R158g/{w}x{h}bb.jpg",
                    "bgColor": "efebe0",
                    "textColor1": "020202",
                    "textColor2": "282827",
                    "textColor3": "31302e",
                    "textColor4": "504f4c"
                },
                "playParams": {
                    "id": "pl.adc9cc99b91649188b6ea75d39048836",
                    "kind": "playlist",
                    "versionHash": "e04d48180c081089983de2c2e4c1e5be0ca299d93b7d9486e3069e515042300f"
                },
                "playlistType": "external",
                "lastModifiedDate": "2022-01-28T16: 12: 39Z",
                "url": "https: //music.apple.com/us/playlist/rising-week-2022/pl.adc9cc99b91649188b6ea75d39048836",
                "isChart": false,
                "name": "Rising Week 2022"
            }
        },
        {
            "id": "pl.63a00809de2b49d493e631a4c36f420b",
            "type": "playlists",
            "href": "/v1/catalog/us/playlists/pl.63a00809de2b49d493e631a4c36f420b",
            "attributes": {
                "curatorName": "Pitchfork",
                "artwork": {
                    "width": 2400,
                    "height": 2400,
                    "url": "https: //is1-ssl.mzstatic.com/image/thumb/U4Wbe1zy4i5_UZ1ueH_9bg/{w}x{h}bb.jpg",
                    "bgColor": "030608",
                    "textColor1": "eaeaea",
                    "textColor2": "cec7c3",
                    "textColor3": "bcbcbd",
                    "textColor4": "a5a09d"
                },
                "playParams": {
                    "id": "pl.63a00809de2b49d493e631a4c36f420b",
                    "kind": "playlist",
                    "versionHash": "77e3c808250857d238b38716b99c54f4bdeff54ba93dd6c908b816ff4a2ac90b"
                },
                "playlistType": "external",
                "lastModifiedDate": "2021-12-16T17: 00: 50Z",
                "url": "https: //music.apple.com/us/playlist/the-50-best-albums-of-2020/pl.63a00809de2b49d493e631a4c36f420b",
                "isChart": false,
                "name": "The 50 Best Albums of 2020"
            }
        },
        {
            "id": "pl.00e28caf8a7849cfb7c7174d877ee2c3",
            "type": "playlists",
            "href": "/v1/catalog/us/playlists/pl.00e28caf8a7849cfb7c7174d877ee2c3",
            "attributes": {
                "curatorName": "Pitchfork",
                "artwork": {
                    "width": 2400,
                    "height": 2400,
                    "url": "https: //is5-ssl.mzstatic.com/image/thumb/6PC-tQXZ3SlzuIhL0CBnkA/{w}x{h}bb.jpg",
                    "bgColor": "f7f8f2",
                    "textColor1": "000000",
                    "textColor2": "211f1f",
                    "textColor3": "313130",
                    "textColor4": "4c4a49"
                },
                "playParams": {
                    "id": "pl.00e28caf8a7849cfb7c7174d877ee2c3",
                    "kind": "playlist",
                    "versionHash": "8bc75c620332e9d9a512da972092be93659ff2ad1c3ce0c7919170c3d194063f"
                },
                "playlistType": "external",
                "lastModifiedDate": "2021-12-09T17: 20: 04Z",
                "url": "https: //music.apple.com/us/playlist/ambient-jazzs-quiet-forceful-return/pl.00e28caf8a7849cfb7c7174d877ee2c3",
                "isChart": false,
                "name": "Ambient Jazz’s Quiet, Forceful Return"
            }
        },
        {
            "id": "pl.5e3c099ec06a40e0baf7a478f4523a36",
            "type": "playlists",
            "href": "/v1/catalog/us/playlists/pl.5e3c099ec06a40e0baf7a478f4523a36",
            "attributes": {
                "curatorName": "Pitchfork",
                "artwork": {
                    "width": 2400,
                    "height": 2400,
                    "url": "https: //is4-ssl.mzstatic.com/image/thumb/42uUj-qytQ6fvlCsFEtHyg/{w}x{h}bb.jpg",
                    "bgColor": "23402c",
                    "textColor1": "ebcad0",
                    "textColor2": "e9bae2",
                    "textColor3": "c3afaf",
                    "textColor4": "c1a1be"
                },
                "playParams": {
                    "id": "pl.5e3c099ec06a40e0baf7a478f4523a36",
                    "kind": "playlist",
                    "versionHash": "07328232bbf2e8f0ee1e953e4b13406cfeebcaa1c2928f5895d495433ff7011e"
                },
                "playlistType": "external",
                "lastModifiedDate": "2021-12-08T16: 50: 42Z",
                "url": "https: //music.apple.com/us/playlist/the-31-best-rock-albums-of-2021/pl.5e3c099ec06a40e0baf7a478f4523a36",
                "isChart": false,
                "name": "The 31 Best Rock Albums of 2021"
            }
        },
        {
            "id": "pl.cad86725f64949f699753a3264a8d15f",
            "type": "playlists",
            "href": "/v1/catalog/us/playlists/pl.cad86725f64949f699753a3264a8d15f",
            "attributes": {
                "curatorName": "Pitchfork",
                "artwork": {
                    "width": 2400,
                    "height": 2400,
                    "url": "https: //is2-ssl.mzstatic.com/image/thumb/U0X0LkT0uKK0hEpKBD6P_A/{w}x{h}bb.jpg",
                    "bgColor": "151412",
                    "textColor1": "c3f932",
                    "textColor2": "c6cef5",
                    "textColor3": "a0cb2b",
                    "textColor4": "a2a9c8"
                },
                "playParams": {
                    "id": "pl.cad86725f64949f699753a3264a8d15f",
                    "kind": "playlist",
                    "versionHash": "0b82f12a8b3bb16dbffc29337dc9b2ec72b3dfcc3755dfbbafda5e16480e936f"
                },
                "playlistType": "external",
                "lastModifiedDate": "2021-12-07T22: 41: 52Z",
                "url": "https: //music.apple.com/us/playlist/pitchforks-50-best-albums-of-2021/pl.cad86725f64949f699753a3264a8d15f",
                "isChart": false,
                "name": "Pitchfork’s 50 Best Albums of 2021"
            }
        },
        {
            "id": "pl.b2622a1393fb48a4b30badf8333b057a",
            "type": "playlists",
            "href": "/v1/catalog/us/playlists/pl.b2622a1393fb48a4b30badf8333b057a",
            "attributes": {
                "curatorName": "Pitchfork",
                "artwork": {
                    "width": 2400,
                    "height": 2400,
                    "url": "https: //is4-ssl.mzstatic.com/image/thumb/TyM9aRI3jmw0GH4r3DiKPw/{w}x{h}bb.jpg",
                    "bgColor": "211312",
                    "textColor1": "fad6a1",
                    "textColor2": "e6a25d",
                    "textColor3": "cfaf84",
                    "textColor4": "be854e"
                },
                "playParams": {
                    "id": "pl.b2622a1393fb48a4b30badf8333b057a",
                    "kind": "playlist",
                    "versionHash": "4b4a77d0581b1b86bc841c559a81a3a780435ae7e3be631d8a8a53c0d74a2bd4"
                },
                "playlistType": "external",
                "lastModifiedDate": "2021-12-07T21: 53: 13Z",
                "url": "https: //music.apple.com/us/playlist/pitchforks-100-best-songs-of-2021/pl.b2622a1393fb48a4b30badf8333b057a",
                "isChart": false,
                "name": "Pitchfork’s 100 Best Songs of 2021"
            }
        },
        {
            "id": "pl.4e23a527944048639ce79981261e353e",
            "type": "playlists",
            "href": "/v1/catalog/us/playlists/pl.4e23a527944048639ce79981261e353e",
            "attributes": {
                "curatorName": "Pitchfork",
                "artwork": {
                    "width": 2400,
                    "height": 2400,
                    "url": "https: //is3-ssl.mzstatic.com/image/thumb/SG-MQ-US-032-Image000001/v4/57/4d/c4/574dc4a7-2604-3e96-0571-ce5aa6a11ca3/image/{w}x{h}cc.jpg"
                },
                "playParams": {
                    "id": "pl.4e23a527944048639ce79981261e353e",
                    "kind": "playlist",
                    "versionHash": "a26234004c21be279e6cd872d26633015a5739518f402764126fced0cdafdf9a"
                },
                "playlistType": "external",
                "lastModifiedDate": "2021-10-12T21: 26: 12Z",
                "url": "https: //music.apple.com/us/playlist/pitchforks-25-next-list-the-artists-shaping-where/pl.4e23a527944048639ce79981261e353e",
                "isChart": false,
                "name": "Pitchfork’s 25 Next List: The Artists Shaping Where Music Will Go From Here"
            }
        },
        {
            "id": "pl.2023e3553fe2477b90a2eb53e2283323",
            "type": "playlists",
            "href": "/v1/catalog/us/playlists/pl.2023e3553fe2477b90a2eb53e2283323",
            "attributes": {
                "curatorName": "Pitchfork",
                "artwork": {
                    "width": 2400,
                    "height": 2400,
                    "url": "https: //is4-ssl.mzstatic.com/image/thumb/SG-MQ-US-032-Image000001/v4/e8/59/d2/e859d22c-bbfd-dd75-e405-b87fbf7d54f9/image/{w}x{h}cc.jpg"
                },
                "playParams": {
                    "id": "pl.2023e3553fe2477b90a2eb53e2283323",
                    "kind": "playlist",
                    "versionHash": "1952ff8e8fc60a0d6435da190fa26862ff4d2affb4ce223427728219d7687210"
                },
                "playlistType": "external",
                "lastModifiedDate": "2021-05-17T17: 32: 28Z",
                "url": "https: //music.apple.com/us/playlist/pitchfork-music-festival-2021/pl.2023e3553fe2477b90a2eb53e2283323",
                "isChart": false,
                "name": "Pitchfork Music Festival 2021"
            }
        },
        {
            "id": "pl.5c54c63960e14a9da6d0d43cc3b69561",
            "type": "playlists",
            "href": "/v1/catalog/us/playlists/pl.5c54c63960e14a9da6d0d43cc3b69561",
            "attributes": {
                "curatorName": "Pitchfork",
                "artwork": {
                    "width": 2400,
                    "height": 2400,
                    "url": "https: //is5-ssl.mzstatic.com/image/thumb/8b8IGALXaL7taHPAg-Z8Ig/{w}x{h}bb.jpg",
                    "bgColor": "bbb7b4",
                    "textColor1": "080605",
                    "textColor2": "2a2828",
                    "textColor3": "2b2928",
                    "textColor4": "474544"
                },
                "playParams": {
                    "id": "pl.5c54c63960e14a9da6d0d43cc3b69561",
                    "kind": "playlist",
                    "versionHash": "fd7f3ad7ba991532b15832be4692a5e8b215dc38b39dd0cf341d2100633a2c21"
                },
                "playlistType": "external",
                "lastModifiedDate": "2021-04-22T14: 58: 57Z",
                "url": "https: //music.apple.com/us/playlist/what-can-music-do-during-climate-collapse/pl.5c54c63960e14a9da6d0d43cc3b69561",
                "isChart": false,
                "name": "What Can Music Do During Climate Collapse?"
            }
        }
    ]
}

```

## Endpoint

`GET https://api.music.apple.com/v1/catalog/{storefront}/curators/{id}/{relationship}`

## Parameters

- `l` (string): The localization to use, specified by a language tag. The possible values are in the `supportedLanguageTags` array belonging to the `Storefront` object specified by `storefront`. Otherwise, the default is `defaultLanguageTag` in `Storefront`.
- `include` ([string]): Additional relationships to include in the fetch.
- `limit` (integer): The number of objects or number of objects in the specified relationship returned.
- `extend` ([string]): A list of attribute extensions to apply to resources in the response.

## See Also

- [object Curators](curators.md)
  A resource object that represents a curator.
- [object CuratorsResponse](curatorsresponse.md)
  The response to a request for curators.
- [Get a Catalog Curator](get-a-catalog-curator.md)
  Fetch a curator by using the curator’s identifier.
- [Get Multiple Catalog Curators](get-multiple-catalog-curators.md)
  Fetch one or more curators by using their identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/fetch-a-relationship-on-this-resource-by-name-1091z)*