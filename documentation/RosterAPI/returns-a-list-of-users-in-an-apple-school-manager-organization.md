# List users

**Framework**: Roster API  
**Kind**: httpRequest

List users in an Apple School Manager organization.

**Availability**:
- Roster API 1.0.0+

#### Discussion

##### Example

**Request**:

```None
curl "https://api-school.apple.com/rosterapi/v1/users?role=Student&limit=1" \
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

`GET https://api-school.apple.com/rosterapi/v1/users`

## Parameters

- `limit` (string): The maximum amount of user objects to return. The default is 100.
- `pageToken` (string): A token to retrieve the next set of records when the number of users is greater than the `limit` parameter.
- `role` (string): The role of the user in the organization.

## See Also

- [Read a user](returns-a-specific-user-in-an-apple-school-manager-organization.md)
  Read a user in an Apple School Manager organization.
- [object User](user.md)
  A user in an Apple School Manager organization.
- [object RoleLocation](rolelocation.md)
  A mapping between a role assumed by a user in an Apple School Manager organization, and the corresponding location.
- [List users in a class](returns-a-users-for-an-apple-school-manager-class.md)
  List users in a class of an Apple School Manager organization.
- [object Users](users.md)
  A list of users, with a token for pagination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/rosterapi/returns-a-list-of-users-in-an-apple-school-manager-organization)*