# Read User Information

**Framework**: Enterprise Program API  
**Kind**: httpRequest

Get information about a user on your team, such as name, roles, and app visibility.

##### Example Request and Response

**Request**:

```None
https://qa.api.adep.ase.apple.com/v1/users/345bb7dc-a653-43ff-acee-a4817cd28479
```

**Response**:

```json
{
"data": {
"type": "users",
"id": "345bb7dc-a653-43ff-acee-a4817cd28479",
"attributes": {
"username": "ifuko+6env3@apple.com",
"firstName": "Ildiko",
"lastName": "Ln6Env3",
"roles": [
"ADMIN"
]
},
"links": {
"self": "https://qa.api.adep.ase.apple.com/v1/users/345bb7dc-a653-43ff-acee-a4817cd28479"
}
},
"links": {
"self": "https://qa.api.adep.ase.apple.com/v1/users/345bb7dc-a653-43ff-acee-a4817cd28479"
}
}
```

## Endpoint

`GET https://api.enterprise.developer.apple.com/v1/users/{id}`

## Parameters

- `fields[users]` ([string]): Fields to return for included related types.

## See Also

- [List Users](list-users.md)
  Get a list of the users on your team.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/read-user-information)*