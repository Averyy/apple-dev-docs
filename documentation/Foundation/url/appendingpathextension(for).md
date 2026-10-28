# appendingPathExtension(for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a URL by appending the preferred path extension for the type you specify to the URL’s last path component.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func appendingPathExtension(for contentType: UTType) -> URL
```

## Return Value

A URL with the default path extension for the type you specify.

## Discussion

Use this method when you want to mix partial input from a user or other source, and need to produce a complete filename suitable for that input. For example, if you download a file from the internet and know its MIME type, you can use this method to ensure the URL has the correct filename extension where you save the file.

If `partialName` already has a path extension, and that path extension is valid for file system objects of type `contentType`, the function doesn’t add an extension before appending it to the URL. For example, if the inputs are `puppy.jpg` and [`jpeg`](../../UniformTypeIdentifiers/uttype-swift.struct/jpeg.md), respectively, the function returns a URL with an appended path component of `puppy.jpg`. However, if the inputs are `puppy.jpg` and [`plainText`](../../UniformTypeIdentifiers/uttype-swift.struct/plaintext.md), respectively, the function returns a URL with an appended path component of `puppy.jpg.txt`. If you want to replace any existing path extension, use the [`deletePathExtension()`](./deletepathextension%28%29.md) method first.

If the function can’t append the path component, it returns an unchanged URL.

For more information about types, see [Uniform Type Identifiers](../../UniformTypeIdentifiers/UniformTypeIdentifiers.md).

## Parameters

- `contentType`: A uniform type identifier.

## See Also

### Adding a path extension
- [func appendPathExtension(String)](./appendpathextension%28_%29.md)
  Appends the specified path extension to self.
- [func appendingPathExtension(String) -> URL](./appendingpathextension%28_%29.md)
  Returns a URL by appending the specified path extension to self.
- [func appendPathExtension(for: UTType)](./appendpathextension%28for%29.md)
  Appends the preferred path extension for the type you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/appendingpathextension(for:))*