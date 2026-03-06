# List classes

**Framework**: Roster API  
**Kind**: httpRequest

List classes in an Apple School Manager organization.

**Availability**:
- Roster API 1.0.0+

## Mentions

- [Obtaining information about people and classes](obtaining-information-about-people-and-classes.md)

#### Discussion

##### Example

**Request**:

```None
curl "https://api-school.apple.com/rosterapi/v1/classes?limit=1" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}"

```

**Response**:

```json
{
  "classes": [
    {
      "id": "1234",
      "name": "Algebra",
      "number": "101",
      "room": "PL-213",
      "locationId": "LO:1234",
      "instructorIds": [
        "1234",
        "2345"
      ],
      "studentIds": [
        "54321",
        "54322",
        "54323"
      ],
      "dateCreated": "2021-07-26T11:11:51Z",
      "dateLastModified": "2021-07-26T11:11:51Z"
    }
  ],
  "moreToFollow": true,
  "nextPageToken": "3da541559918a808c2402bba5012f6c60b27661c"
}
```

## Endpoint

`GET https://api-school.apple.com/rosterapi/v1/classes`

## Parameters

- `limit` (string): The maximum number of class records to return. The default is 100.
- `pageToken` (string): A token for paging through a large number of results. If the number of records in the organization is greater than the `limit` parameter, pass the token returned in [`Classes`](classes.md).

## See Also

- [Read a class](returns-a-specific-class-in-an-apple-school-manager-organization..md)
  Read a class from an Apple School Manager organization.
- [object Class](class.md)
  A class in an Apple School Manager organization.
- [object Classes](classes.md)
  A list of classes, with a token for pagination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/rosterapi/returns-a-list-of-classes-for-an-apple-school-manager-organization)*