# placeholderURL(for:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Type Method

Returns a placeholder URL for a given document URL.

**Availability**:
- iOS 8.0+ - Deprecated in 11.0
- iPadOS 8.0+ - Deprecated in 11.0
- Mac Catalyst 8.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`NSFileProviderManager`](../nsfileprovidermanager.md) class’s [`placeholderURL(for:)`](../nsfileprovidermanager/placeholderurl%28for%29.md) method instead.

## Declaration

```swift
class func placeholderURL(for url: URL) -> URL
```

```objc
+ (NSURL *) placeholderURLForURL:(NSURL *) url;
```

#### Return Value

A placeholder URL for the given document.

#### Discussion

This method maps file URLs into their corresponding placeholder URLs. You typically call this method to generate the placeholder URL before calling [`writePlaceholder(at:withMetadata:)`](./writeplaceholder%28at,withmetadata%29.md).

You must not override this method.

## Parameters

- `url`: The document URL to be converted.

## See Also

### Managing placeholders
- [class func writePlaceholder(at: URL, withMetadata: [URLResourceKey : Any]) throws](./writeplaceholder%28at,withmetadata%29.md)
  Writes a document placeholder with the provided metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/placeholderurl(for:))*