# subscript(dynamicMember:)

**Framework**: Foundation  
**Kind**: subscript

Gets or sets custom integer properties.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
final subscript<P>(dynamicMember key: KeyPath<ProgressManager.Properties, P.Type>) -> Int where P : ProgressManager.Property, P.Summary == Int, P.Value == Int { get }
```

#### Overview

This subscript provides read-write access to custom progress properties where both the value and summary types are `Int`. If the property has not been set, the getter returns the property’s default value.

## Parameters

- `key`: A key path to the custom integer property type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressreporter/subscript(dynamicmember:)-9pcsi)*