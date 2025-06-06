# Delete a Context

**Framework**: ClassKit Catalog API  
**Kind**: httpRequest

Remove information that you previously stored about your app’s assignable activities.

**Availability**:
- ClassKit 1.0+

#### Discussion

You can’t delete a context that has child contexts. Delete any child contexts before trying to delete their parent.

##### Example

## See Also

- [Preparing Context Data](preparing-context-data.md)
  Adjust how you manage context data when working with the web API.
- [Create or Replace Contexts](create-or-replace-contexts.md)
  Store information about the assignable content that your educational app provides.
- [Get a Context](get-a-context.md)
  Fetch information that you previously stored about your app’s assignable activities.
- [object Context](context.md)
  An area of your app that represents an assignable task, like a quiz or a chapter.
- [object ContextsRequest](contextsrequest.md)
  A request that you make when modifying context information.
- [object ContextsResponse](contextsresponse.md)
  The response you receive after modifying context information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkitcatalogapi/delete-a-context)*