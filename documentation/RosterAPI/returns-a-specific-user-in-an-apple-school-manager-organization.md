# Read a user

**Framework**: Roster API  
**Kind**: httpRequest

Read a user in an Apple School Manager organization.

**Availability**:
- Roster API 1.0.0+

## Mentions

- [Integrating with Roster API and Sign in with Apple](integrating-with-roster-api-and-sign-in-with-apple.md)

#### Discussion

Access to the `users` resource requires authorization to the `edu.users.read` scope.

##### Example

**Request**:

```None
curl "https://api-school.apple.com/rosterapi/v1/users/1234" \
        -H "Authorization: Bearer ${TOKEN}"
```

**Response**:

```json
{
  "id": "1234",
  "email": "user@example.edu",
  "givenName": "Finny",
  "middleName”: "Kim",
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
```

## Endpoint

`GET https://api-school.apple.com/rosterapi/v1/users/{userId}`

## Parameters

- `userId` (string) *(required)*: The identifier from the user. Use the `id` field from the [`User`](user.md) object.

## See Also

- [object User](user.md)
  A user in an Apple School Manager organization.
- [object RoleLocation](rolelocation.md)
  A mapping between a role assumed by a user in an Apple School Manager organization, and the corresponding location.
- [List users](returns-a-list-of-users-in-an-apple-school-manager-organization.md)
  List users in an Apple School Manager organization.
- [List users in a class](returns-a-users-for-an-apple-school-manager-class.md)
  List users in a class of an Apple School Manager organization.
- [object Users](users.md)
  A list of users, with a token for pagination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/rosterapi/returns-a-specific-user-in-an-apple-school-manager-organization)*