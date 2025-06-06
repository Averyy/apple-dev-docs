# Create or Replace Contexts

**Framework**: ClassKit Catalog API  
**Kind**: httpRequest

Store information about the assignable content that your educational app provides.

**Availability**:
- ClassKit 1.0+

#### Discussion

Define parent contexts of any of the contexts defined in this call, either in a previous call to the same endpoint, or as part of the same call.

You can specify up to 200 contexts for any one call to this endpoint. The call overwrites any contexts that already exist with the same identifier path and locale.

##### Example

## Request Body

The context or contexts to add.

## See Also

- [Preparing Context Data](preparing-context-data.md)
  Adjust how you manage context data when working with the web API.
- [Get a Context](get-a-context.md)
  Fetch information that you previously stored about your app’s assignable activities.
- [Delete a Context](delete-a-context.md)
  Remove information that you previously stored about your app’s assignable activities.
- [object Context](context.md)
  An area of your app that represents an assignable task, like a quiz or a chapter.
- [object ContextsRequest](contextsrequest.md)
  A request that you make when modifying context information.
- [object ContextsResponse](contextsresponse.md)
  The response you receive after modifying context information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkitcatalogapi/create-or-replace-contexts)*