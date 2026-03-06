# List all price points for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get all the available price points for a specific app.

**Availability**:
- App Store Connect API 2.3+

## Mentions

- [App Store Connect API 2.3 release notes](app-store-connect-api-2-3-release-notes.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/apps/6447402192/appPricePoints?filter%5Bterritory%5D=USA,CAN&include=territory&limit=5
```

**Response**:

```json
{
  "data" : [ {
    "type" : "appPricePoints",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDAifQ",
    "attributes" : {
      "customerPrice" : "0.0",
      "proceeds" : "0.0"
    },
    "relationships" : {
      "equalizations" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v3/appPricePoints/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDAifQ/relationships/equalizations",
          "related" : "https://api.appstoreconnect.apple.com/v3/appPricePoints/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDAifQ/equalizations"
        }
      },
      "territory" : {
        "data" : {
          "type" : "territories",
          "id" : "CAN"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v3/appPricePoints/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDAifQ"
    }
  }, {
    "type" : "appPricePoints",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDEifQ",
    "attributes" : {
      "customerPrice" : "1.39",
      "proceeds" : "0.97"
    },
    "relationships" : {
      "equalizations" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v3/appPricePoints/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDEifQ/relationships/equalizations",
          "related" : "https://api.appstoreconnect.apple.com/v3/appPricePoints/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDEifQ/equalizations"
        }
      },
      "territory" : {
        "data" : {
          "type" : "territories",
          "id" : "CAN"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v3/appPricePoints/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDEifQ"
    }
  }, {
    "type" : "appPricePoints",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDIifQ",
    "attributes" : {
      "customerPrice" : "2.79",
      "proceeds" : "1.95"
    },
    "relationships" : {
      "equalizations" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v3/appPricePoints/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDIifQ/relationships/equalizations",
          "related" : "https://api.appstoreconnect.apple.com/v3/appPricePoints/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDIifQ/equalizations"
        }
      },
      "territory" : {
        "data" : {
          "type" : "territories",
          "id" : "CAN"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v3/appPricePoints/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDIifQ"
    }
  }, {
    "type" : "appPricePoints",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDMifQ",
    "attributes" : {
      "customerPrice" : "3.99",
      "proceeds" : "2.79"
    },
    "relationships" : {
      "equalizations" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v3/appPricePoints/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDMifQ/relationships/equalizations",
          "related" : "https://api.appstoreconnect.apple.com/v3/appPricePoints/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDMifQ/equalizations"
        }
      },
      "territory" : {
        "data" : {
          "type" : "territories",
          "id" : "CAN"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v3/appPricePoints/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDMifQ"
    }
  }, {
    "type" : "appPricePoints",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDQifQ",
    "attributes" : {
      "customerPrice" : "5.49",
      "proceeds" : "3.84"
    },
    "relationships" : {
      "equalizations" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v3/appPricePoints/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDQifQ/relationships/equalizations",
          "related" : "https://api.appstoreconnect.apple.com/v3/appPricePoints/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDQifQ/equalizations"
        }
      },
      "territory" : {
        "data" : {
          "type" : "territories",
          "id" : "CAN"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v3/appPricePoints/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDQU4iLCJwIjoiMTAwMDQifQ"
    }
  } ],
  "included" : [ {
    "type" : "territories",
    "id" : "CAN",
    "attributes" : {
      "currency" : "CAD"
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/territories/CAN"
    }
  } ],
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/apps/6447402192/appPricePoints?include=territory&filter%5Bterritory%5D=CAN%2CUSA&limit=5",
    "next" : "https://api.appstoreconnect.apple.com/v1/apps/6447402192/appPricePoints?cursor=BQ.AMN1C2M&include=territory&filter%5Bterritory%5D=CAN%2CUSA&limit=5"
  },
  "meta" : {
    "paging" : {
      "total" : 1602,
      "limit" : 5
    }
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/appPricePoints`

## Parameters

- `fields[appPricePoints]` ([string])
- `fields[apps]` ([string])
- `fields[territories]` ([string])
- `filter[territory]` ([string])
- `include` ([string])
- `limit` (integer)

## See Also

- [GET /v1/apps/{id}/relationships/appPricePoints](get-v1-apps-_id_-relationships-apppricepoints.md)
- [Read app price point information](get-v3-apppricepoints-_id_.md)
  Get details about a specific app price point.
- [List app price point equalizations](get-v3-apppricepoints-_id_-equalizations.md)
  List all equivalent app prices points to a base price point.
- [GET /v3/appPricePoints/{id}/relationships/equalizations](get-v3-apppricepoints-_id_-relationships-equalizations.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-apppricepoints)*