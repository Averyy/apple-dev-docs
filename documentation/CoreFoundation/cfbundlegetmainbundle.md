# CFBundleGetMainBundle()

**Framework**: Core Foundation  
**Kind**: func

Returns an application’s main bundle.

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
func CFBundleGetMainBundle() -> CFBundle!
```

#### Return Value

A CFBundle object representing the application’s main bundle, or `NULL` if it is not possible to create a bundle. Ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

#### Discussion

CFBundle creates a main bundle whenever it possibly can, even for unbundled apps. There are a few situations in which it is not possible, so you should check the return value against `NULL`, but this happens only in exceptional circumstances.

For an explanation of the main bundle, see [`Locating and Opening Bundles`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/AccessingaBundlesContents/AccessingaBundlesContents.html#//apple_ref/doc/uid/10000123i-CH104-SW6) in [`Bundle Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/Introduction/Introduction.html#//apple_ref/doc/uid/10000123i).

## See Also

- [func CFBundleCreate(CFAllocator!, CFURL!) -> CFBundle!](cfbundlecreate(_:_:).md)
  Creates a CFBundle object.
- [func CFBundleCreateBundlesFromDirectory(CFAllocator!, CFURL!, CFString!) -> CFArray!](cfbundlecreatebundlesfromdirectory(_:_:_:).md)
  Searches a directory and constructs an array of CFBundle objects from all valid bundles in the specified directory.
- [func CFBundleGetAllBundles() -> CFArray!](cfbundlegetallbundles().md)
  Returns an array containing all of the bundles currently open in the application.
- [func CFBundleGetBundleWithIdentifier(CFString!) -> CFBundle!](cfbundlegetbundlewithidentifier(_:).md)
  Locate a bundle given its program-defined identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundlegetmainbundle())*