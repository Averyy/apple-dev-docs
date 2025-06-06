# init(_:)

**Framework**: System  
**Kind**: init

Create a file path component from a string.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init?(_ string: String)
```

#### Discussion

Returns `nil` if `string` is empty, a root, or has more than one component in it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/component/init(_:))*