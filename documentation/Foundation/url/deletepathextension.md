# deletePathExtension()

**Framework**: Foundation  
**Kind**: method

Returns a URL constructed by removing any path extension.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
mutating func deletePathExtension()
```

#### Discussion

If the URL has an empty path (e.g., `http://www.example.com`), then this function will do nothing.

## See Also

- [func deletingPathExtension() -> URL](url/deletingpathextension.md)
  Returns a URL constructed by removing any path extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/deletepathextension())*