# subscript(dynamicMember:)

**Framework**: MusicKit  
**Kind**: subscript

A subscript that allows your app to access any property of the requested section type directly on this library section object.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
subscript<T>(dynamicMember keyPath: KeyPath<SectionType, T>) -> T { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiclibrarysection/subscript(dynamicmember:))*