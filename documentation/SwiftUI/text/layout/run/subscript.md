# subscript(_:)

**Framework**: SwiftUI  
**Kind**: subscript

The custom attribute of type `T` associated with the run of glyphs, or nil. If no run contains the custom attribute we also check its attachment’s runs.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
subscript<T>(key: T.Type) -> T? where T : TextAttribute { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/layout/run/subscript(_:))*