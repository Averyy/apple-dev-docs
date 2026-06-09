# List Automatically Generated Prices for an App

**Framework**: App Store Connect API  
**Kind**: httpRequest

List the automatically calculated prices for an app generated from a base territory.

**Availability**:
- App Store Connect API 2.3+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/appPriceSchedules/6447402192/automaticPrices
```

**Response**:

```json
{
  "data" : [ {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJBRkciLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJBRkciLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJBR08iLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJBR08iLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJBSUEiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJBSUEiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJBUkUiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJBUkUiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJBUk0iLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJBUk0iLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJBVEciLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJBVEciLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJBVVMiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJBVVMiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJBVVQiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJBVVQiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJBWkUiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJBWkUiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCRUwiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCRUwiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCRU4iLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCRU4iLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCRkEiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCRkEiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCR1IiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCR1IiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCSFIiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCSFIiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCSFMiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCSFMiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCSUgiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCSUgiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCTFIiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCTFIiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCTFoiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCTFoiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCTVUiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCTVUiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCT0wiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCT0wiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCUkEiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCUkEiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCUkIiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCUkIiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCUk4iLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCUk4iLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCVE4iLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCVE4iLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCV0EiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJCV0EiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDSEUiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDSEUiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDSEwiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDSEwiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDSE4iLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDSE4iLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDSVYiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDSVYiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDTVIiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDTVIiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDT0QiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDT0QiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDT0ciLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDT0ciLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDT0wiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDT0wiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDUFYiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDUFYiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDUkkiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDUkkiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDWU0iLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDWU0iLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDWVAiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDWVAiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDWkUiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJDWkUiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJERVUiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJERVUiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJETUEiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJETUEiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJETksiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJETksiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJET00iLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJET00iLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJEWkEiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJEWkEiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJFQ1UiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJFQ1UiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJFR1kiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJFR1kiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJFU1AiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJFU1AiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJFU1QiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJFU1QiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJGSU4iLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJGSU4iLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJGSkkiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJGSkkiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  }, {
    "type" : "appPrices",
    "id" : "eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJGUkEiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9",
    "attributes" : {
      "manual" : false,
      "startDate" : "2023-02-28",
      "endDate" : null
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/appPrices/eyJzIjoiNjQ0NzQwMjE5MiIsInQiOiJGUkEiLCJwIjoiMTAwMDciLCJzZCI6MTY3NzU3MTIwMC4wMDAwMDAwMDAsImVkIjowLjB9"
    }
  } ],
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/appPriceSchedules/6447402192/automaticPrices",
    "next" : "https://api.appstoreconnect.apple.com/v1/appPriceSchedules/6447402192/automaticPrices?cursor=Mg.AKwzESA"
  },
  "meta" : {
    "paging" : {
      "total" : 172,
      "limit" : 50
    }
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appPriceSchedules/{id}/automaticPrices`

## Parameters

- `fields[appPricePoints]` ([string]): Additional fields to include for each app price point resource returned by the response.
- `fields[appPrices]` ([string]): Additional fields to include for each app price resource returned by the response.
- `fields[territories]` ([string]): Additional fields to include for each territory resource returned by the response.
- `filter[endDate]` ([string]): Filter the returned app prices by end date.
- `filter[startDate]` ([string]): Filter the returned app prices by start date.
- `filter[territory]` ([string]): Filter the returned app prices by territory.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The maximum number of app price resources to return.

## See Also

- [Read Price Schedule Information for an App](get-v1-apps-_id_-apppriceschedule.md)
  Read price schedule details for a specific app.
- [Get the app price schedule ID for an app](get-v1-apps-_id_-relationships-apppriceschedule.md)
- [Read an App's Price Schedule Information](get-v1-apppriceschedules-_id_.md)
  List the price schedule details for a specific app.
- [Read the Base Territory for an App's Price Schedule](get-v1-apppriceschedules-_id_-baseterritory.md)
  Read the base territory and currency for a specific app.
- [List Manually Chosen Prices for an App](get-v1-apppriceschedules-_id_-manualprices.md)
  List the prices you chose for a specific app.
- [List automatic price IDs for an app price schedule](get-v1-apppriceschedules-_id_-relationships-automaticprices.md)
- [Get the base territory ID for an app price schedule](get-v1-apppriceschedules-_id_-relationships-baseterritory.md)
- [List manual price IDs for an app price schedule](get-v1-apppriceschedules-_id_-relationships-manualprices.md)
- [Add a Scheduled Price Change to an App](post-v1-apppriceschedules.md)
  Create a scheduled price change for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apppriceschedules-_id_-automaticprices)*