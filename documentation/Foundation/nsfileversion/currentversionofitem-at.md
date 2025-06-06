# currentVersionOfItem(at:)

**Framework**: Foundation  
**Kind**: method

Returns the most recent version object for the file at the specified URL.

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
class func currentVersionOfItem(at url: URL) -> NSFileVersion?
```

#### Return Value

The version object representing the current version of the file or `nil` if there is no such file.

## Parameters

- `url`: The URL of the file whose version object you want.

## See Also

- [class func otherVersionsOfItem(at: URL) -> [NSFileVersion]?](nsfileversion/otherversionsofitem(at:).md)
  Returns all versions of the specified file except the current version.
- [class func version(itemAt: URL, forPersistentIdentifier: Any) -> NSFileVersion?](nsfileversion/version(itemat:forpersistentidentifier:).md)
  Returns the version of the file that has the specified persistent ID.
- [class func temporaryDirectoryURLForNewVersionOfItem(at: URL) -> URL](nsfileversion/temporarydirectoryurlfornewversionofitem(at:).md)
  Creates and returns a temporary directory to use for saving the contents of the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfileversion/currentversionofitem(at:))*