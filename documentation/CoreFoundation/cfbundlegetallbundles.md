# CFBundleGetAllBundles()

**Framework**: Core Foundation  
**Kind**: func

Returns an array containing all of the bundles currently open in the application.

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
func CFBundleGetAllBundles() -> CFArray!
```

#### Return Value

A CFArray object containing CFBundle objects for each open bundle in the application. Ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

#### Discussion

This function is potentially expensive and not thread-safe. It’s best used for debugging or other diagnostics purposes rather than as part of the main execution path of production code.

## See Also

- [func CFBundleCreate(CFAllocator!, CFURL!) -> CFBundle!](cfbundlecreate(_:_:).md)
  Creates a CFBundle object.
- [func CFBundleCreateBundlesFromDirectory(CFAllocator!, CFURL!, CFString!) -> CFArray!](cfbundlecreatebundlesfromdirectory(_:_:_:).md)
  Searches a directory and constructs an array of CFBundle objects from all valid bundles in the specified directory.
- [func CFBundleGetBundleWithIdentifier(CFString!) -> CFBundle!](cfbundlegetbundlewithidentifier(_:).md)
  Locate a bundle given its program-defined identifier.
- [func CFBundleGetMainBundle() -> CFBundle!](cfbundlegetmainbundle().md)
  Returns an application’s main bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundlegetallbundles())*