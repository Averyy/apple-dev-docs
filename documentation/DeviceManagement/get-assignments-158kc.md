# Get Assignments

**Framework**: Device Management  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of assignments currently assigned to a user or device.

**Availability**:
- VPP License Management 1.1+

> **Deprecated**: This legacy API is currently in maintenance mode. Apple won’t add any new functionality to it.

## Discussion

### Example Request and Response

**Request**:

```
{
  "adamIdStr" : "361304891",
  "clientUserIdStr" : "user1",
  "sToken" : "h40Gte9aQnZFDNM39IUkRPCsQDxBxbZB4Wy34pxefOuQkeeb3h2a5Rlopo4KDn3MrFKf4CM3OY+WGAoZ1cD6iZ6yzsMk1+5PVBNc66YS6ZQ="
}
```

**Response**:

```json
{
  "assignments" : [ {
    "adamIdStr" : "361304891",
    "clientUserIdStr" : "user1",
    "pricingParam" : "STDQ"
  } ],
  "assignmentsInCurrentPage" : 1,
  "currentPageIndex" : 0,
  "expirationMillis" : 1860422147836,
  "location" : {
    "locationId" : 22222222222,
    "locationName" : "LocationName"
  },
  "status" : 0,
  "totalAssignments" : 1,
  "totalPages" : 1,
  "uId" : "100978"
}
```

## Topics

### Request and Response
- [object VppAssignmentRequest](./vppassignmentrequest.md)
  The request for a list of assignments.
- [object VppAssignmentsResponse](./vppassignmentsresponse.md)
  The response that contains a list of assignments.

## Endpoint

`POST https://vpp.itunes.apple.com/mdm/getAssignments`

## Request Body

**Content-Type**: `application/json`  
**Type**: `VppAssignmentRequest`

The request for a list of assignments.

## Responses

- `200` OK (`VppAssignmentsResponse`, `application/json`): The response that contains a list of assignments.

## See Also

### Asset and license management
- [Get Assets](./get-assets-44p83.md)
  Get the set of assets managed by your organization.
- [Get Licenses](./get-licenses.md)
  Get the set of licenses managed by your organization.
- [Manage Licenses](./manage-licenses.md)
  Associate and disassociate licenses with users and devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/get-assignments-158kc)*