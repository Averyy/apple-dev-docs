# deleteLastPathComponent()

**Framework**: Foundation  
**Kind**: method

Returns a URL constructed by removing the last path component of self.

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
mutating func deleteLastPathComponent()
```

#### Discussion

This function may either remove a path component or append `/..`.

If the URL has an empty path (e.g., `http://www.example.com`), then this function will do nothing.

## See Also

- [func deletingLastPathComponent() -> URL](url/deletinglastpathcomponent.md)
  Returns a URL constructed by removing the last path component of self.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/deletelastpathcomponent())*