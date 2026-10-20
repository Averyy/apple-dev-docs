# currentVersionOfItem(at:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (NSFileVersion *) currentVersionOfItemAtURL:(NSURL *) url;
```

#### Return Value

The version object representing the current version of the file or `nil` if there is no such file.

## Parameters

- `url`: The URL of the file whose version object you want.

## See Also

### Getting the Version of a File
- [class func otherVersionsOfItem(at: URL) -> [NSFileVersion]?](./otherversionsofitem%28at%29.md)
  Returns all versions of the specified file except the current version.
- [class func version(itemAt: URL, forPersistentIdentifier: Any) -> NSFileVersion?](./version%28itemat,forpersistentidentifier%29.md)
  Returns the version of the file that has the specified persistent ID.
- [class func temporaryDirectoryURLForNewVersionOfItem(at: URL) -> URL](./temporarydirectoryurlfornewversionofitem%28at%29.md)
  Creates and returns a temporary directory to use for saving the contents of the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfileversion/currentversionofitem(at:))*