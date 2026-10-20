# List users in a class

**Framework**: Roster API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List users in a class of an Apple School Manager organization.

**Availability**:
- Roster API 1.0.0+

## Mentions

- [Obtaining information about people and classes](./obtaining-information-about-people-and-classes.md)

#### Discussion

##### Example

**Request**:

```
curl "https://api-school.apple.com/rosterapi/v1/classes/1234/users?role=Student&limit=1" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}"
```

**Response**:

```json
{
  "users": [
    {
      "id": "1234",
      "email": "user@example.edu",
      "givenName": "Finny",
      "middleName": "Kim",
      "familyName": "Ho",
      "grade": "10",
      "roleLocationMapping": [
        {
          "roleName": "Student",
          "locationId": "LO:1234"
        }
      ],
      "dateCreated": "2022-04-25T16:00:45Z",
      "dateLastModified": "2022-04-25T16:00:45Z"
    }
  ],
  "moreToFollow": true,
  "nextPageToken": "3da541559918a808c2402bba5012f6c60b27661c"
}
```

## Endpoint

`GET https://api-school.apple.com/rosterapi/v1/classes/{classId}/users`

## Parameters

### Path Parameters

- `classId` (string) *(required)*: A unique class identifier. Use an identifier from the `id` field of [`Class`](./class.md).

### Query Parameters

- `limit` (string): The maximum number of user records to return. The default limit is 100.
- `role` (string): The role of the user in the class.

  **Allowed Values**: `Student`, `Instructor`
- `pageToken` (string): A token to retrieve the next set of records when the number of users is greater than the `limit` parameter.

## Responses

- `200` OK (`Users`, `application/json`): The request was successful.
- `401` Unauthorized: The access token was invalid.
- `403` Forbidden: Access to the requested user was forbidden.
- `404` Not Found: The server didn’t find a class with the given `classId` in the organization.
- `429`: The client made too many requests. The response includes an `X-Retry-After` header that indicates the number of seconds to wait before making another request.
- `500` Internal Server Error: The server encountered an internal error.

## See Also

### Information about users
- [Read a user](./returns-a-specific-user-in-an-apple-school-manager-organization.md)
  Read a user in an Apple School Manager organization.
- [object User](./user.md)
  A user in an Apple School Manager organization.
- [object RoleLocation](./rolelocation.md)
  A mapping between a role assumed by a user in an Apple School Manager organization, and the corresponding location.
- [List users](./returns-a-list-of-users-in-an-apple-school-manager-organization.md)
  List users in an Apple School Manager organization.
- [object Users](./users.md)
  A list of users, with a token for pagination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/rosterapi/returns-a-users-for-an-apple-school-manager-class)*