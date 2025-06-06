# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a localization value instance.

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
init(_ value: String)
```

#### Discussion

Creating a [`String.LocalizationValue`](string/localizationvalue.md) with this initializer creates a localized value with no interpolated values.

## Parameters

- `value`: A string that provides the localization key to look up. This parameter also serves as the default value if the system can’t find a localized string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/localizationvalue/init(_:))*