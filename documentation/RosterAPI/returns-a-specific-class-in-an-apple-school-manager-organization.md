# Read a class

**Framework**: Roster API  
**Kind**: httpRequest

Read a class from an Apple School Manager organization.

**Availability**:
- Roster API 1.0.0+

#### Discussion

##### Example

**Request**:

```None
curl "https://api-school.apple.com/rosterapi/v1/classes/1234" \
    -H "Authorization: Bearer ${TOKEN}"
```

**Response**:

```json
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
  "dateLastModified”: "2021-07-26T11:11:51Z"
}
```

## Endpoint

`GET https://api-school.apple.com/rosterapi/v1/classes/{classId}`

## Parameters

- `classId` (string) *(required)*: The identifier from the class. Use the `id` field from the [`Class`](class.md) object.

## See Also

- [object Class](class.md)
  A class in an Apple School Manager organization.
- [List classes](returns-a-list-of-classes-for-an-apple-school-manager-organization.md)
  List classes in an Apple School Manager organization.
- [object Classes](classes.md)
  A list of classes, with a token for pagination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/rosterapi/returns-a-specific-class-in-an-apple-school-manager-organization.)*