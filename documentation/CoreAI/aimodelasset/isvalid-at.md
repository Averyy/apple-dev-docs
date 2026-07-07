# isValid(at:)

**Framework**: Core AI  
**Kind**: method

Returns a Boolean value that indicates whether the URL contains a valid model asset.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static func isValid(at url: URL) -> Bool
```

#### Return Value

`true` if the URL points to a valid model asset; otherwise, `false`.

#### Discussion

This checks that:

- the URL is a file URL
- the extension is one of the known model asset extensions
- the model contains either a source program or a derived artifact

## Parameters

- `url`: The file URL to validate.

## See Also

- [init(contentsOf: URL) throws](aimodelasset/init(contentsof:).md)
  Creates a model asset from the contents of the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelasset/isvalid(at:))*