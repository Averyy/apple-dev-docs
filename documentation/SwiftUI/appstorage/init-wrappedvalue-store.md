# init(wrappedValue:_:store:)

**Framework**: SwiftUI  
**Kind**: init

Creates a property that can save and restore tab sidebar customizations.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
init(wrappedValue: Value = TabViewCustomization(), _ key: String, store: UserDefaults? = nil) where Value == TabViewCustomization
```

#### Discussion

You can set this customization on the TabView using [`tabViewCustomization(_:)`](view/tabviewcustomization(_:).md).

## Parameters

- `wrappedValue`: The default value if the customization is not   available for the given key.
- `key`: The key to read and write the value to in the user defaults   store.
- `store`: The user defaults store to read and write to. A value   of   will use the user default store from the environment.

## See Also

- [init(_:store:)](appstorage/init(_:store:).md)
  Creates a property that can read and write an Optional boolean user default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/appstorage/init(wrappedvalue:_:store:))*