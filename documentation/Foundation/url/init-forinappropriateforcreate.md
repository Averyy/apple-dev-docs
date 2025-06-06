# init(for:in:appropriateFor:create:)

**Framework**: Foundation  
**Kind**: init

Creates a file URL for a common directory in a domain.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(for directory: FileManager.SearchPathDirectory, in domain: FileManager.SearchPathDomainMask, appropriateFor url: URL? = nil, create shouldCreate: Bool = false) throws
```

## Parameters

- `directory`: The search path for the commonly used directory, such as   or  .
- `domain`: The file system domain to search, which the values in   define. Specify only one domain for this parameter. You may not specify   with this initializer.
- `url`: The initializer ignores this parameter unless the directory parameter contains the value   and the domain parameter contains the value  .
- `shouldCreate`: A Boolean value that indicates whether the initializer creates the directory if it doesn’t already exist.

## See Also

- [FileManager.SearchPathDirectory](filemanager/searchpathdirectory.md)
  The location of significant directories.
- [FileManager.SearchPathDomainMask](filemanager/searchpathdomainmask.md)
  Domain constants specifying base locations to use when you search for significant directories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/init(for:in:appropriatefor:create:))*