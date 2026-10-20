# Delete a product

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete an Xcode Cloud product and all of its associated workflows, builds, and artifacts.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

To delete an Xcode Cloud product, call this endpoint using the HTTP `DELETE` method like this:

```swift
https://api.appstoreconnect.apple.com/v1/ciProducts/9ad354b0-f380-40d3-b94f-dd5225b8b3d5
```

App Store Connect confirms the deletion by responding with the `HTTP/1.1 204 No Content` HTTP status code.

> ❗ **Important**:  Deleting an Xcode Cloud product permanently deletes all workflows, including their build history and artifacts. Only delete an Xcode Cloud product when you’re confident that you don’t need its workflows, build history, or artifacts anymore. Instead of deleting a product, deactivate its workflows to preserve the product and its build history and artifacts. For more information about deactivating a workflow, see [Developing a workflow strategy for Xcode Cloud](../Xcode/developing-a-workflow-strategy-for-xcode-cloud.md).

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/ciProducts/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the Products resource.

## Responses

- `204` No Content: The request completed successfully and the specific Products resource was deleted.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-ciproducts-_id_)*