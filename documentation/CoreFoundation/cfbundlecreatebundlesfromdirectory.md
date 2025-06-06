# CFBundleCreateBundlesFromDirectory(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Searches a directory and constructs an array of CFBundle objects from all valid bundles in the specified directory.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFBundleCreateBundlesFromDirectory(_ allocator: CFAllocator!, _ directoryURL: CFURL!, _ bundleType: CFString!) -> CFArray!
```

#### Return Value

A CFArray object containing CFBundle objects created from the contents of the specified directory. Returns an empty array if no bundles exist at `directoryURL`, and `NULL` if there was a memory allocation problem. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

The array returned by this function will not contain stale CFBundle references.

##### Special Considerations

The [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029) applies both to the array returned and to the bundles in the array. In order to properly dispose of the returned value, you must release the array  any bundles returned in the array.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass   or   to use the current default allocator.
- `directoryURL`: The location of the directory to search for valid bundles.
- `bundleType`: The abstract type of the bundles to locate and create. The type is expressed as a filename extension, such as  . Pass   to create CFBundle objects for bundles of any type.

## See Also

- [func CFBundleCreate(CFAllocator!, CFURL!) -> CFBundle!](cfbundlecreate(_:_:).md)
  Creates a CFBundle object.
- [func CFBundleGetAllBundles() -> CFArray!](cfbundlegetallbundles().md)
  Returns an array containing all of the bundles currently open in the application.
- [func CFBundleGetBundleWithIdentifier(CFString!) -> CFBundle!](cfbundlegetbundlewithidentifier(_:).md)
  Locate a bundle given its program-defined identifier.
- [func CFBundleGetMainBundle() -> CFBundle!](cfbundlegetmainbundle().md)
  Returns an application’s main bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundlecreatebundlesfromdirectory(_:_:_:))*