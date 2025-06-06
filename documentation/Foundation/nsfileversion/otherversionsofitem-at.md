# otherVersionsOfItem(at:)

**Framework**: Foundation  
**Kind**: method

Returns all versions of the specified file except the current version.

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
class func otherVersionsOfItem(at url: URL) -> [NSFileVersion]?
```

#### Return Value

An array of file version objects or `nil` if there is no such file. The array does not contain the version object returned by the [`currentVersionOfItem(at:)`](nsfileversion/currentversionofitem(at:).md) method.

#### Discussion

For locally based files, this property typically contains versions of the file that you saved explicitly or that were saved at appropriate times while the file was being edited. For documents residing in the cloud, this property typically returns zero or more file versions representing conflicting versions of a file that need to be resolved with the current version.

## Parameters

- `url`: The URL of the file whose versions you want.

## See Also

- [class func currentVersionOfItem(at: URL) -> NSFileVersion?](nsfileversion/currentversionofitem(at:).md)
  Returns the most recent version object for the file at the specified URL.
- [class func version(itemAt: URL, forPersistentIdentifier: Any) -> NSFileVersion?](nsfileversion/version(itemat:forpersistentidentifier:).md)
  Returns the version of the file that has the specified persistent ID.
- [class func temporaryDirectoryURLForNewVersionOfItem(at: URL) -> URL](nsfileversion/temporarydirectoryurlfornewversionofitem(at:).md)
  Creates and returns a temporary directory to use for saving the contents of the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfileversion/otherversionsofitem(at:))*