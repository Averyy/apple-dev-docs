# url(for:in:appropriateFor:create:)

**Framework**: Foundation  
**Kind**: method

Locates and optionally creates the specified common directory in a domain.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func url(for directory: FileManager.SearchPathDirectory, in domain: FileManager.SearchPathDomainMask, appropriateFor url: URL?, create shouldCreate: Bool) throws -> URL
```

#### Return Value

The [`NSURL`](nsurl.md) for the requested directory. When using Objective-C, if an error occurs, this method returns `nil` and assigns an appropriate error object to the `error` parameter.

#### Discussion

You typically use this method to locate one of the standard system directories, such as the `Documents`, `Application Support` or `Caches` directories. After locating (or creating) the desired directory, this method returns the URL for that directory. If more than one appropriate directory exists in the specified domain, this method returns only the first one it finds.

> ❗ **Important**:  Passing a directory and domain pair that makes no sense (for example [`FileManager.SearchPathDirectory.desktopDirectory`](filemanager/searchpathdirectory/desktopdirectory.md) and [`networkDomainMask`](filemanager/searchpathdomainmask/networkdomainmask.md)) raises an exception.

 Passing a directory and domain pair that makes no sense (for example [`FileManager.SearchPathDirectory.desktopDirectory`](filemanager/searchpathdirectory/desktopdirectory.md) and [`networkDomainMask`](filemanager/searchpathdomainmask/networkdomainmask.md)) raises an exception.

You can use this method to create a new temporary directory. To do so, specify [`FileManager.SearchPathDirectory.itemReplacementDirectory`](filemanager/searchpathdirectory/itemreplacementdirectory.md) for the `directory` parameter, [`userDomainMask`](filemanager/searchpathdomainmask/userdomainmask.md) for the `domain` parameter, and a URL for the `url` parameter which determines the volume of the returned URL.

For example, the following code results in a new temporary directory with a path in the form of `/private/var/folders/d0/h37cw8ns3h1bfr_2gnwq2yyc0000gn/T/TemporaryItems/Untitled/`:

> ❗ **Important**:  If you use this method to create a temporary directory, you should not rely on the existence of that temporary directory after the app is exited. It is recommended that you remove any temporary directories that are created after they’re no longer needed.

 If you use this method to create a temporary directory, you should not rely on the existence of that temporary directory after the app is exited. It is recommended that you remove any temporary directories that are created after they’re no longer needed.

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `directory`: The search path directory. The supported values are described in  .
- `domain`: The file system domain to search. The value for this parameter is one of the constants described in  . You should specify only one domain for your search and you may not specify the   constant for this parameter.
- `url`: This parameter is ignored unless the   parameter contains the value   and the   parameter contains the value  .
- `shouldCreate`: When creating a temporary directory, this parameter is ignored and the directory is always created.

## See Also

- [func urls(for: FileManager.SearchPathDirectory, in: FileManager.SearchPathDomainMask) -> [URL]](filemanager/urls(for:in:).md)
  Returns an array of URLs for the specified common directory in the requested domains.
- [func NSSearchPathForDirectoriesInDomains(FileManager.SearchPathDirectory, FileManager.SearchPathDomainMask, Bool) -> [String]](nssearchpathfordirectoriesindomains(_:_:_:).md)
  Creates a list of directory search paths.
- [func NSOpenStepRootDirectory() -> String](nsopensteprootdirectory().md)
  Returns the root directory of the user’s system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/url(for:in:appropriatefor:create:))*