# getPromisedItemResourceValue(_:forKey:)

**Framework**: Foundation  
**Kind**: method

Returns the value of the resource property for the specified key.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func getPromisedItemResourceValue(_ value: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey key: URLResourceKey) throws
```

#### Discussion

This method behaves identically to [`getResourceValue(_:forKey:)`](nsurl/getresourcevalue(_:forkey:).md), but works on promised items. A promised item is not guaranteed to have its contents in the file system until you use a file coordinator to perform a coordinated read on its URL, which causes the contents to be downloaded or otherwise generated. Promised item URLs are returned by various APIs, including:

- A metadata query using either the [`NSMetadataQueryUbiquitousDataScope`](nsmetadataqueryubiquitousdatascope.md) or [`NSMetadataQueryUbiquitousDocumentsScope`](nsmetadataqueryubiquitousdocumentsscope.md) scopes
- The contents of the directory returned by the file manager’s `URLForUbiquitousContainerIdentifier:`
- The URL inside the accessor block of a coordinated read or write operation that used the [`immediatelyAvailableMetadataOnly`](nsfilecoordinator/readingoptions/immediatelyavailablemetadataonly.md), [`forDeleting`](nsfilecoordinator/writingoptions/fordeleting.md), [`forMoving`](nsfilecoordinator/writingoptions/formoving.md), or [`contentIndependentMetadataOnly`](nsfilecoordinator/writingoptions/contentindependentmetadataonly.md) options

You must use this method instead of `getResourceValue:forKey:error:` for any URLs returned by these methods.

This method works for any resource value that is not tied to the item’s contents. Some keys, like [`contentAccessDateKey`](urlresourcekey/contentaccessdatekey.md) or [`generationIdentifierKey`](urlresourcekey/generationidentifierkey.md), do not return valid values. If you use one of these keys, the method returns [`true`](https://developer.apple.com/documentation/swift/true), but the value returns `nil`.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `value`: The location where the value for the resource property identified by   should be stored.
- `key`: The name of one of the URL’s resource properties.

## See Also

- [func getResourceValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey: URLResourceKey) throws](nsurl/getresourcevalue(_:forkey:).md)
  Returns the value of the resource property for the specified key.
- [func checkPromisedItemIsReachableAndReturnError(NSErrorPointer) -> Bool](nsurl/checkpromiseditemisreachableandreturnerror(_:).md)
  Returns whether the promised item can be reached.
- [func promisedItemResourceValues(forKeys: [URLResourceKey]) throws -> [URLResourceKey : Any]](nsurl/promiseditemresourcevalues(forkeys:).md)
  Returns the resource values for the properties identified by specified array of keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/getpromiseditemresourcevalue(_:forkey:))*