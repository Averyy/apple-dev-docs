# PagingInformation.Paging

**Framework**: App Store Connect API  
**Kind**: dictionary

Paging details such as the total number of resources and the per-page limit.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object PagingInformation.Paging
```

#### Discussion

Adjust the number of resources returned per page by using the `limit` query parameter in your request. For example, the following request  returns the first 10 testers:

```javascript
GET /v1/betaTesters?limit=10
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/paginginformation/paging-data.dictionary)*