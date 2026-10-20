# deletingPathExtension()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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
func deletingPathExtension() -> URL
```

#### Discussion

If the URL has an empty path (e.g., `http://www.example.com`), then this function will return the URL unchanged.

## See Also

### Removing a path extension
- [func deletePathExtension()](./deletepathextension%28%29.md)
  Returns a URL constructed by removing any path extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/deletingpathextension())*