# init(data:)

**Framework**: SwiftUI  
**Kind**: init

Creates a new Metal shader library from `data`, which must be the contents of precompiled Metal library. Functions compiled from the returned library will only be cached as long as the returned library exists.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(data: Data)
```

## See Also

- [init(url: URL)](shaderlibrary/init(url:).md)
  Creates a new Metal shader library from the contents of `url`, which must be the location  of precompiled Metal library. Functions compiled from the returned library will only be cached as long as the returned library exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shaderlibrary/init(data:))*