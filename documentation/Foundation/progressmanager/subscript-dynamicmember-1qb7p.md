# subscript(dynamicMember:)

**Framework**: Foundation  
**Kind**: subscript

Gets or sets custom integer properties.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
final subscript<P>(dynamicMember key: KeyPath<ProgressManager.Properties, P.Type>) -> Int where P : ProgressManager.Property, P.Summary == Int, P.Value == Int { get set }
```

#### Overview

This subscript provides read-write access to custom progress properties where both the value and summary types are `Int`. If the property has not been set, the getter returns the property’s default value.

## Parameters

- `key`: A key path to the custom integer property type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressmanager/subscript(dynamicmember:)-1qb7p)*