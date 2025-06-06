# version(itemAt:forPersistentIdentifier:)

**Framework**: Foundation  
**Kind**: method

Returns the version of the file that has the specified persistent ID.

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
class func version(itemAt url: URL, forPersistentIdentifier persistentIdentifier: Any) -> NSFileVersion?
```

#### Return Value

The file version object with the specified ID or `nil` if no such version object exists.

## Parameters

- `url`: The URL of the file whose version you want.
- `persistentIdentifier`: The persistent ID of the   object you want.

## See Also

- [var persistentIdentifier: any NSCoding](nsfileversion/persistentidentifier.md)
  The identifier for this version of the file.
- [class func currentVersionOfItem(at: URL) -> NSFileVersion?](nsfileversion/currentversionofitem(at:).md)
  Returns the most recent version object for the file at the specified URL.
- [class func otherVersionsOfItem(at: URL) -> [NSFileVersion]?](nsfileversion/otherversionsofitem(at:).md)
  Returns all versions of the specified file except the current version.
- [class func temporaryDirectoryURLForNewVersionOfItem(at: URL) -> URL](nsfileversion/temporarydirectoryurlfornewversionofitem(at:).md)
  Creates and returns a temporary directory to use for saving the contents of the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfileversion/version(itemat:forpersistentidentifier:))*