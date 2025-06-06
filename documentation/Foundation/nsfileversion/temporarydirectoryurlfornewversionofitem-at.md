# temporaryDirectoryURLForNewVersionOfItem(at:)

**Framework**: Foundation  
**Kind**: method

Creates and returns a temporary directory to use for saving the contents of the file.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class func temporaryDirectoryURLForNewVersionOfItem(at url: URL) -> URL
```

#### Return Value

A URL identifying the temporary directory in which to create a the new file. You must delete the directory specified by this URL after you have created the file and moved it to its proper location.

#### Discussion

You can use this method in situations where you want to create a file in a temporary location. For example, you might use this method when saving the contents of a file to disk for the first time. When you finish creating the temporary file, move it to a more appropriate location, such as the user’s `Documents` directory. You must delete the directory returned by this method when you are done with it.

## Parameters

- `url`: The URL of the file whose contents you want to save.

## See Also

- [class func currentVersionOfItem(at: URL) -> NSFileVersion?](nsfileversion/currentversionofitem(at:).md)
  Returns the most recent version object for the file at the specified URL.
- [class func otherVersionsOfItem(at: URL) -> [NSFileVersion]?](nsfileversion/otherversionsofitem(at:).md)
  Returns all versions of the specified file except the current version.
- [class func version(itemAt: URL, forPersistentIdentifier: Any) -> NSFileVersion?](nsfileversion/version(itemat:forpersistentidentifier:).md)
  Returns the version of the file that has the specified persistent ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfileversion/temporarydirectoryurlfornewversionofitem(at:))*