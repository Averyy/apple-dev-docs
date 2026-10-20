# UserUpdateRequest.Data

**Framework**: Enterprise Program API  
**Kind**: dictionary  
**Role**: Object

The data element of the request body.

## Declaration

```
object UserUpdateRequest.Data
```

## Topics

### Objects
- [object UserUpdateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  Attributes for which you change values as part of the update request.

## Properties

- `attributes` (UserUpdateRequest.Data.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `users`


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/userupdaterequest/data-data.dictionary)*