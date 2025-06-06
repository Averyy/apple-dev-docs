# init(_:store:)

**Framework**: SwiftUI  
**Kind**: init

Creates a property that can read and write an Optional boolean user default.

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
init(_ key: String, store: UserDefaults? = nil) where Value == Bool?
```

#### Discussion

Defaults to nil if there is no restored value.

## Parameters

- `key`: The key to read and write the value to in the user defaults   store.
- `store`: The user defaults store to read and write to. A value   of   will use the user default store from the environment.

## See Also

- [init(wrappedValue:_:store:)](appstorage/init(wrappedvalue:_:store:).md)
  Creates a property that can save and restore tab sidebar customizations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/appstorage/init(_:store:))*