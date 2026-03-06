# List Users

**Framework**: Enterprise Program API  
**Kind**: httpRequest

Get a list of the users on your team.

##### Example Request and Response

**Request**:

```None
https://qa.api.adep.ase.apple.com/v1/users?limit=2
```

**Response**:

```json
{
"data": [
{
"type": "users",
"id": "a514773b-b4ed-4564-9d97-6215bda0662b",
"attributes": {
"username": "username",
"firstName": "Firstname",
"lastName": "Lastname",
"roles": [
  "DEVELOPER"
]
},
"links": {
"self": "https://qa.api.adep.ase.apple.com/v1/users/a514773b-b4ed-4564-9d97-6215bda0662b"
}
},
{
"type": "users",
"id": "c26a77a6-b906-4191-90b8-4f181fa2c7d3",
"attributes": {
"username": "username",
"firstName": "Firstname",
"lastName": "Lastname",
"roles": [
  "DEVELOPER"
]
},
"links": {
"self": "https://qa.api.adep.ase.apple.com/v1/users/c26a77a6-b906-4191-90b8-4f181fa2c7d3"
}
}
],
"links": {
"self": "https://qa.api.adep.ase.apple.com/v1/users?limit=2",
"next": "https://qa.api.adep.ase.apple.com/v1/users?cursor=Ag.FcUD4A&limit=2"
},
"meta": {
"paging": {
"total": 150,
"limit": 2
}
}
}
```

## Endpoint

`GET https://api.enterprise.developer.apple.com/v1/users`

## Parameters

- `fields[users]` ([string]): Fields to return for included related types.
- `limit` (integer): Number of resources to return.
- `sort` ([string]): Attributes by which to sort.
- `filter[roles]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[username]` ([string]): Attributes, relationships, and IDs by which to filter.

## See Also

- [Read User Information](read-user-information.md)
  Get information about a user on your team, such as name, roles, and app visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/list-users)*