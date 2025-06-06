# Using Paginated Endpoints

**Framework**: Devicemanagement

Manage paginated endpoints to efficiently work with large record sets.

#### Overview

To improve performance, the server uses pagination to return smaller discrete subsets of a large result set. When the number of records in a response exceeds a server-controlled limit, the server paginates it. Endpoints that support pagination can accept a `pageIndex` query parameter that indicates the page to return. You can make paginated requests in parallel to reduce the time it takes to retrieve the entire result set.

The following endpoints support pagination:

- [`Get Assets`](get-assets-4ski1.md)
- [`Get Assignments`](get-assignments-9wv1e.md)
- [`Get Users`](get-users-4mwln.md)

You can use versioned endpoints to retrieve only those records with changes since your previous query. Endpoints that support versioning can accept a `sinceVersionId` query parameter. This allows you to keep your data up to date with incremental changes if you’re unable to receive update notifications.

The following endpoints support the `sinceVersionId` query parameter:

- [`Get Assignments`](get-assignments-9wv1e.md)
- [`Get Users`](get-users-4mwln.md)

##### Handle Pagination

Requests for large record sets return paginated responses. You can traverse the pages by supplying the `pageIndex` query parameter in your request.

To use a `pageIndex` to traverse a paginated response:

1. Make an initial request without `pageIndex`, which returns the first page of records.
2. If the number of records exceeds a server-controlled limit (on the order of several hundred), the server includes a `nextPageIndex` field in the response, along with the first page of records. The MDM client passes this value as the `pageIndex` in a subsequent request to get the next page of records. As long as additional pages remain, the server returns a `nextPageIndex` field in the response.
3. After the server returns all records for the request, it no longer includes a `nextPageIndex` field in the response.

A paginated response includes the following fields:

| Response field | Description |
| --- | --- |
| `currentPageIndex` | The current page index of the paginated response. |
| `nextPageIndex` | The next page index in the paginated response. |
| `size` | The number of records on the current page. |
| `totalPages` | The total number of pages in the paginated response. |

> **Note**:  The `pageIndex` is a zero-based integer. A `pageIndex` of `0` returns the first page of results. If you omit it from the request, `pageIndex` defaults to `0`. The last page of results has a `pageIndex` equal to `totalPages`-1.

The following is an example of a request for the first page of records:

```javascript
curl --location --request GET 'https://vpp.itunes.apple.com/mdm/v2/assignments' \
--header 'Authorization: Bearer {cToken}'
```

The response that contains the first page of records looks like the following:

```javascript
{
    "assignments": [
         {
            "adamId": "377298193",
            "serialNumber": "b6817f44-6229-4f1b-ba16-9eef9ebf24c6",
            "pricingParam": "STDQ"
        },
            …
            …
            …
        {
            "adamId": "377298193",
            "serialNumber": "4b3f6bef-bfcd-47e6-ba8c-ad14f3b9d924",
            "pricingParam": "STDQ"
        },
    ],
    "currentPageIndex": 0,
    "nextPageIndex": 1,
    "size": 549,
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "totalPages": 353,
    "uId": "2049025000431439",
    "versionId": "658a45d0-5a7b-11eb-b9e4-d782eaed4cfb"
}
```

The following is an example of a request for the second page of records:

```javascript
curl --location --request GET 'https://vpp.itunes.apple.com/mdm/v2/assignments?pageIndex=1' \
--header 'Authorization: Bearer {cToken}'
```

The response that contains the second page of records looks like the following:

```javascript
{
    "assignments": [
         {
            "adamId": "377298193",
            "serialNumber": "b6817f44-6229-4f1b-ba16-9eef9ebf24c6",
            "pricingParam": "STDQ"
        },
            …
            …
            …
        {
            "adamId": "377298193",
            "serialNumber": "4b3f6bef-bfcd-47e6-ba8c-ad14f3b9d924",
            "pricingParam": "STDQ"
        }
    ],
    "currentPageIndex": 1,
    "nextPageIndex": 2,
    "size": 549,
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "totalPages": 353,
    "uId": "2049025000431439",
    "versionId": "658a45d0-5a7b-11eb-b9e4-d782eaed4cfb"
}
```

The following is an example of a request for the last page of records:

```javascript
curl --location --request GET 'https://vpp.itunes.apple.com/mdm/v2/assignments?pageIndex=352' \
--header 'Authorization: Bearer {cToken}'
```

The response that contains the last page of records looks like the following:

```javascript
{
    "assignments": [
         {
            "adamId": "377298193",
            "serialNumber": "b6817f44-6229-4f1b-ba16-9eef9ebf24c6",
            "pricingParam": "STDQ"
        },
            …
            …
            …
        {
            "adamId": "377298193",
            "serialNumber": "4b3f6bef-bfcd-47e6-ba8c-ad14f3b9d924",
            "pricingParam": "STDQ"
        }
    ],
    "currentPageIndex": 352,
    "size": 549,
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "totalPages": 353,
    "uId": "2049025000431439",
    "versionId": "658a45d0-5a7b-11eb-b9e4-d782eaed4cfb"
}
```

##### Handle Parallel Paginated Requests

Paginated endpoints can accept multiple requests in parallel instead of sequentially, which can significantly reduce the amount of time to request and receive records. For performance reasons, don’t submit more than five requests simultaneously.

To make requests for multiple pages in parallel:

1. Make an initial request for the first page of results. The response contains a value for `totalPages`.
2. Submit subsequent requests in parallel by making the same request with different values for `pageIndex` ranging from `1` to `totalPages`-1.

> ❗ **Important**:  The `totalPages` in a result set can change while traversing a paginated result set. This occurs whenever the system modifies underlying data in the result set. When performing parallel requests, it’s important to note whether the value for `totalPages` changes on any paginated response, and to continue to iterate through the result set until you traverse the last page.

##### Handle Versioned Responses

If you’re unable to subscribe to notifications, or are performing an initial sync, use the `sinceVersionId` query parameter to obtain incremental updates to keep the MDM client up to date with changes without having to retrieve all records.

A `versionId` returns in the response of all versioned endpoints. The `versionId` represents the state of a complete data set for an endpoint. The server generates a new `versionId` for an endpoint whenever the system modifies any underlying data for that endpoint. The MDM client can use a `versionId` in future requests to get records with modifications since the generation of that `versionId`. When any writes occur to the underlying data in a fetch, `versionId` updates.

> **Note**:  The `versionId` for an endpoint can change while traversing a paginated result set. Use the `versionId` that returns on the first page of results in a subsequent query to obtain all newly modified records.

To use a `versionId` to obtain modified records:

1. Make an initial request. A `versionId` returns with the response that contains the first page of results.
2. Store this `versionId` temporarily on your server.
3. Iterate through any remaining pages of your initial request to retrieve all current data.
4. To retrieve only those records with modifications since your previous query, make a new request and include the query parameter `sinceVersionId`. Use the `versionId` from your initial request as the value for this parameter. If any newly modified records exist, the response contains a new `versionId` along with those records.
5. Repeat these steps at regular intervals to keep your system up to date with incremental changes.

> ❗ **Important**:  The [`Get Assets`](get-assets-4ski1.md) endpoint returns a `versionId` to indicate when the system modifies underlying data. However, the [`Get Assets`](get-assets-4ski1.md) endpoint doesn’t support the `sinceVersionId` query parameter so you can’t query [`Get Assets`](get-assets-4ski1.md) to obtain only those records with modifications.

The following is an example of a request for the initial data:

```javascript
curl --location --request GET 'https://vpp.itunes.apple.com/mdm/v2/assignments' \
--header 'Authorization: Bearer {cToken}'
```

The response that contains the initial data looks like the following:

```javascript
{
    "assignments": [
         {
            "adamId": "377298193",
            "serialNumber": "b6817f44-6229-4f1b-ba16-9eef9ebf24c6",
            "pricingParam": "STDQ"
        },
            …
            …
            …
        {
            "adamId": "377298193",
            "serialNumber": "4b3f6bef-bfcd-47e6-ba8c-ad14f3b9d924",
            "pricingParam": "STDQ"
        }
    ],
    "currentPageIndex": 0,
    "nextPageIndex": 1,
    "size": 549,
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "totalPages": 353,
    "uId": "2049025000431439",
    "versionId": "658a45d0-5a7b-11eb-b9e4-d782eaed4cfb"
} 
```

The following is an example of a request for the updated data:

```javascript
curl --location --request GET 'https://vpp.itunes.apple.com/mdm/v2/assignments?sinceVersionId=658a45d0-5a7b-11eb-b9e4-d782eaed4cfb' \
--header 'Authorization: Bearer {cToken}'
```

The response that contains the updated data looks like the following:

```javascript
{
    "assignments": [
         {
            "adamId": "377298193",
            "serialNumber": "b6817f44-6229-4f1b-ba16-9eef9ebf24c6",
            "pricingParam": "STDQ"
        },
            …
            …
            …
        {
            "adamId": "377298193",
            "serialNumber": "4b3f6bef-bfcd-47e6-ba8c-ad14f3b9d924",
            "pricingParam": "STDQ"
        }
    ],
    "currentPageIndex": 0,
    "nextPageIndex": 1,
    "size": 1000,
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "totalPages": 10,
    "uId": "2049025000431439",
    "versionId": "87051b80-85f6-11eb-a3ab-95f98468c5f3"
}
```

> **Note**:  Using the `sinceVersionId` query parameter can result in responses with zero records. This isn’t an error or an end signal. It’s just an indication that there aren’t any records with modifications.

## See Also

- [Managing Apps and Books Through Web Services](managing-apps-and-books-through-web-services.md)
  Associate app and book purchases with users or devices.
- [Upgrading to the new App and Book Management API](upgrading-to-the-new-app-and-book-management-api.md)
  Manage devices and content across your organization using the new API version.
- [Apps and Books for Organizations](apps-and-books-for-organizations.md)
  Get details about apps and books to show to your users.
- [Managing Assets](managing-assets.md)
  Retrieve key information to effectively manage assets across an organization’s users and devices.
- [Managing Users](managing-users.md)
  Retrieve key information to effectively manage users across an organization.
- [Subscribing to Notifications](subscribing-to-notifications.md)
  Listen to notifications to keep track of the latest events for an organization.
- [Handling Error Responses](handling-error-responses.md)
  Investigate service request errors and troubleshoot solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/DeviceManagement/using-paginated-endpoints)*