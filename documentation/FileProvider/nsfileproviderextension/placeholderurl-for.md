# placeholderURL(for:)

**Framework**: File Provider  
**Kind**: method

Returns a placeholder URL for a given document URL.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- visionOS 1.0+

## Declaration

```swift
class func placeholderURL(for url: URL) -> URL
```

#### Return Value

A placeholder URL for the given document.

#### Discussion

This method maps file URLs into their corresponding placeholder URLs. You typically call this method to generate the placeholder URL before calling [`writePlaceholder(at:withMetadata:)`](nsfileproviderextension/writeplaceholder(at:withmetadata:).md).

You must not override this method.

## Parameters

- `url`: The document URL to be converted.

## See Also

- [class func writePlaceholder(at: URL, withMetadata: [URLResourceKey : Any]) throws](nsfileproviderextension/writeplaceholder(at:withmetadata:).md)
  Writes a document placeholder with the provided metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/placeholderurl(for:))*