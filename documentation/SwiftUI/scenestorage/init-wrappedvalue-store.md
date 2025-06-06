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

The tab view customization is typically not added to `SceneStorage`, but instead stored in `AppStorage` so the customizations are consistent across different scenes.

## Parameters

- `wrappedValue`: The default value if the customization   is not available for the given key.
- `key`: A key used to save and restore the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scenestorage/init(wrappedvalue:_:store:))*