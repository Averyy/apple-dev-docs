# Delete a Workflow

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete an Xcode Cloud workflow and all of its associated data.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

To delete an Xcode Cloud workflow, call this endpoint using the HTTP `DELETE` method like this:

```swift
https://api.appstoreconnect.apple.com/v1/ciWorkflows/9ad354b0-f380-40d3-b94f-dd5225b8b3d5
```

App Store Connect confirms the deletion by responding with the `HTTP/1.1 204 No Content` HTTP status code.

> ❗ **Important**:  Deleting an Xcode Cloud workflow permanently deletes its build history and artifacts. Only delete an Xcode Cloud workflow when you’re confident that you no longer need it and its build history or artifacts. Instead of deleting a workflow, deactivate it to preserve its build history and artifacts. To deactivate a workflow, use the [`Update an Xcode Cloud Workflow`](patch-v1-ciworkflows-_id_.md) endpoint to set the workflow’s `isEnabled` attribute to `false` or deactivate it in the Xcode or App Store Connect. For more information about deactivating a workflow using Xcode or App Store Connect, see [`Developing a workflow strategy for Xcode Cloud`](https://developer.apple.com/documentation/Xcode/Developing-a-Workflow-Strategy-for-Xcode-Cloud).

## See Also

- [Create a Workflow](post-v1-ciworkflows.md)
  Create a new Xcode Cloud workflow for an Xcode Cloud product.
- [Update an Xcode Cloud Workflow](patch-v1-ciworkflows-_id_.md)
  Make changes to an Xcode Cloud workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-ciworkflows-_id_)*