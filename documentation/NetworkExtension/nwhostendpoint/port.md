# port

**Framework**: Network Extension  
**Kind**: property

The endpoint’s port, represented as a string.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var port: String { get }
```

#### Discussion

Since the port is represented as a string, it is always represented in host byte order. If converting between byte fields and strings, make sure to use host byte ordering.

## See Also

- [var hostname: String](nwhostendpoint/hostname.md)
  The endpoint’s hostname.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwhostendpoint/port)*