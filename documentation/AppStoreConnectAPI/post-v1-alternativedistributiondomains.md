# Add an Alternative Distribution Domain

**Framework**: App Store Connect API  
**Kind**: httpRequest

Add an alternative distribution domain to your account.

**Availability**:
- App Store Connect API 3.4.1+

## Mentions

- [Configuring alternative marketplaces and alternative marketplace apps](configuring-alternative-marketplaces-and-alternative-marketplace-apps.md)
- [Configuring apps for web distribution](configuring-apps-for-web-distribution.md)
- [Creating and configuring keys for web distribution](creating-and-configuring-keys-for-web-distribution.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
POST https://api.appstoreconnect.apple.com/v1/alternativeDistributionDomains
```

**Response**:

```json
{
  “data” : {
    “type” : “alternativeDistributionDomains”,
    “id” : “5b74f5e8-1d7d-48a6-afd3-9441f9027292”,
    “attributes” : {
      “domain” : “example.com”,
      “referenceName” : “exampleREF”,
      “createdDate” : “2024-03-24T07:50:59Z”
    },
    “links” : {
      “self” : “https://api.appstoreconnect.apple.com/v1/alternativeDistributionDomains/f6450d6a-25c7-419d-becb-4d5869b114d1”
    }
  },
  “links” : {
    “self” : “https://api.appstoreconnect.apple.com/v1/alternativeDistributionDomains”
  }
}
```

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/alternativeDistributionDomains`

## See Also

- [Read Alternative Distribution Domain Information](get-v1-alternativedistributiondomains-_id_.md)
  Read information for a specific alternative distribution domain.
- [List Alternative Distribution Domains](get-v1-alternativedistributiondomains.md)
  List all the alternative distribution domains for your account.
- [Delete an Alternative Distribution Domain](delete-v1-alternativedistributiondomains-_id_.md)
  Delete the alternative distribution search domain for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-alternativedistributiondomains)*