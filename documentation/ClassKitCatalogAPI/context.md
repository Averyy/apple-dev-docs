# Context

**Framework**: ClassKit Catalog API  
**Kind**: dictionary

An area of your app that represents an assignable task, like a quiz or a chapter.

**Availability**:
- ClassKit 1.0+

## Declaration

```swift
object Context
```

## Mentions

- [Preparing Context Data](preparing-context-data.md)

#### Discussion

The contexts that you specify in your app as [`CLSContext`](https://developer.apple.com/documentation/classkit/clscontext) instances correspond to the [`Context.Data`](context/data-data.dictionary.md) object. The [`Context.Metadata`](context/metadata-data.dictionary.md) object contains additional information about a context that’s implicit when working with ClassKit in your app.

## Topics

### Objects
- [object Context.Data](context/data-data.dictionary.md)
  The data that makes up a context.
- [object Context.Metadata](context/metadata-data.dictionary.md)
  Information that helps the system categorize a context.

## Properties

- `data` (Context.Data) *(required)*: The data that makes up the context. This is largely the same information that you provide to the ClassKit framework when you create a [`CLSContext`](https://developer.apple.com/documentation/classkit/clscontext) instance.
- `metadata` (Context.Metadata) *(required)*: Information about the context, like the locale to which the context applies.

## See Also

- [Preparing Context Data](preparing-context-data.md)
  Adjust how you manage context data when working with the web API.
- [Create or Replace Contexts](create-or-replace-contexts.md)
  Store information about the assignable content that your educational app provides.
- [Get a Context](get-a-context.md)
  Fetch information that you previously stored about your app’s assignable activities.
- [Delete a Context](delete-a-context.md)
  Remove information that you previously stored about your app’s assignable activities.
- [object ContextsRequest](contextsrequest.md)
  A request that you make when modifying context information.
- [object ContextsResponse](contextsresponse.md)
  The response you receive after modifying context information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkitcatalogapi/context)*