# CFBundleCreate(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a CFBundle object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFBundleCreate(_ allocator: CFAllocator!, _ bundleURL: CFURL!) -> CFBundle!
```

```c
extern CFBundleRefCFBundleCreate(CFAllocatorRef allocator, CFURLRef bundleURL);
```

## Return Value

A CFBundle object created from the bundle at `bundleURL`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

Returns `NULL` if there was a memory allocation problem. May return an existing CFBundle object with the reference count incremented. May return `NULL` if the bundle doesn’t exist at `bundleURL` (see Discussion).

## Discussion

Once a bundle has been created, it is cached; the bundle cache is flushed only periodically. `CFBundleCreate` does not check that a cached bundle still exists in the filesystem. If a bundle is deleted from the filesystem, it is therefore possible for `CFBundleCreate` to return a cached bundle that has actually been deleted.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass `NULL` or [`kCFAllocatorDefault`](./kcfallocatordefault.md) to use the current default allocator.
- `bundleURL`: The location of the bundle for which to create a CFBundle object.

## See Also

### Creating and Accessing Bundles
- [func CFBundleCreateBundlesFromDirectory(CFAllocator!, CFURL!, CFString!) -> CFArray!](./cfbundlecreatebundlesfromdirectory%28_,_,_%29.md)
  Searches a directory and constructs an array of CFBundle objects from all valid bundles in the specified directory.
- [func CFBundleGetAllBundles() -> CFArray!](./cfbundlegetallbundles%28%29.md)
  Returns an array containing all of the bundles currently open in the application.
- [func CFBundleGetBundleWithIdentifier(CFString!) -> CFBundle!](./cfbundlegetbundlewithidentifier%28_%29.md)
  Locate a bundle given its program-defined identifier.
- [func CFBundleGetMainBundle() -> CFBundle!](./cfbundlegetmainbundle%28%29.md)
  Returns an application’s main bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundlecreate(_:_:))*