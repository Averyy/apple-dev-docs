# Allocating and Releasing Objects

**Framework**: GSS  
**Role**: Article

Manage memory and object lifetimes.

#### Overview

The GSS-API defines certain objects as C data structures containing elements using dynamically allocated memory. These include names, buffers, contexts, and credentials, as well as the collection objects that hold buffer sets and Object Identifier (OID) sets. The API provides functions for both allocating and freeing the memory associated with these objects.

Many GSS-API functions create structures on your behalf and return them to you with pointer parameters. You then become responsible for managing the associated memory. When you’re done with such objects, you use one of the release or destroy functions to return its memory to the system.

##### Allocate and Release an Empty Buffer

Prepare an empty buffer set with a call to the [`gss_create_empty_buffer_set(_:_:)`](./gss_create_empty_buffer_set%28_,_%29.md) function, and release it with [`gss_release_buffer_set(_:_:)`](./gss_release_buffer_set%28_,_%29.md) when done.

```swift
import GSS

let minor_status = UnsafeMutablePointer<OM_uint32>.allocate(capacity: 1)
let gss_buffer_set = UnsafeMutablePointer<gss_buffer_set_t>.allocate(capacity: 1)
if gss_create_empty_buffer_set(minor_status, gss_buffer_set) == GSS_S_COMPLETE {
    // buffer has been created.
    // use it and release it when done.
    gss_release_buffer_set(minor_status, gss_buffer_set)
}
```

##### Acquire and Release Credential Memory

When releasing the memory associated with a credential returned to you by the [`gss_acquire_cred(_:_:_:_:_:_:_:_:)`](./gss_acquire_cred%28_,_,_,_,_,_,_,_%29.md) function,  use the [`gss_release_cred(_:_:)`](./gss_release_cred%28_,_%29.md) function. This only releases the memory back to the heap, however, potentially leaving traces of the data behind. To actively purge the credential and only then release the memory, use the [`gss_destroy_cred(_:_:)`](./gss_destroy_cred%28_,_%29.md) function instead. This function is more secure for objects that might contain sensitive information.

##### Handle OID Objects as Static Memory

An exception to the memory management rule is the OID object [`gss_OID`](./gss_oid.md) (not the same as a set of OID objects, [`gss_OID_set`](./gss_oid_set.md)). While an implementation of GSS-API could theoretically allocate memory for OID objects dynamically, Apple’s implementation always returns statically allocated OID objects to you. You use these as-is, and never need to explicitly create or release them. As a result, in practice you never need to call the functions [`gss_duplicate_oid(_:_:_:)`](./gss_duplicate_oid%28_,_,_%29.md) or [`gss_release_oid(_:_:)`](./gss_release_oid%28_,_%29.md).

## See Also

### Memory and Context
- [Function Status](./function-status.md)
  Evaluate return values that most GSS-API functions use to indicate the outcome of an operation.
- [Buffer Management](./buffer-management.md)
  Allocate and deallocate buffers with structures that hold a variety of data.
- [Context Services](./context-services.md)
  Use context services to manage secure operations between endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/allocating-and-releasing-objects)*