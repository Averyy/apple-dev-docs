# removeOtherVersionsOfItem(at:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Removes all versions of a file, except the current one, from the version store.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func removeOtherVersionsOfItem(at url: URL) throws
```

```objc
+ (BOOL) removeOtherVersionsOfItemAtURL:(NSURL *) url error:(NSError **) outError;
```

## Discussion

This method removes all versions except the current one from the version store, freeing up the associated storage space.

You should always remove file versions as part of a coordinated write operation to a file. In other words, always call this method from a block passed to a file coordinator object to initiate a write operation. Doing so ensures that no other processes are operating on the file while you remove the version information.

If successful, subsequent requests for the versions of the file reflect that only the current version is available. You can use this method to free up disk space by removing versions that are no longer needed.

> **Handling Errors in Swift**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: The file whose older versions you want to delete. If the file at this URL does not exist, a new file is created at the location.

## See Also

### Replacing and Deleting Versions
- [func replaceItem(at: URL, options: NSFileVersion.ReplacingOptions) throws -> URL](./replaceitem%28at,options%29.md)
  Replace the contents of the specified file with the contents of the current version’s file.
- [func remove() throws](./remove%28%29.md)
  Remove this version object and its associated file from the version store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfileversion/removeotherversionsofitem(at:))*