# init(_:)

**Framework**: SwiftUI  
**Kind**: init

Creates a property that can save and restore an Optional boolean.

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
init(_ key: String) where Value == Bool?
```

#### Discussion

Defaults to nil if there is no restored value

## Parameters

- `key`: A key used to save and restore the value.

## See Also

- [init(wrappedValue:_:)](scenestorage/init(wrappedvalue:_:).md)
  Creates a property that can save and restore an integer, transforming it to a `RawRepresentable` data type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scenestorage/init(_:))*