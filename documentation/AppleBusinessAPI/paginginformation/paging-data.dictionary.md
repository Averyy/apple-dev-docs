# PagingInformation.Paging

**Framework**: AppleBusinessAPI  
**Kind**: dictionary  
**Role**: Object

Paging details, such as the total number of resources and the per-page limit.

**Availability**:
- Apple Business API 2.6+

## Declaration

```
object PagingInformation.Paging
```

## Properties

- `limit` (integer) *(required)*: The maximum number of resources to return per page.
- `nextCursor` (string): The cursor to use for the next request, in case of pagination.
- `total` (integer): **(Optional)** The total number of resources to return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/paginginformation/paging-data.dictionary)*