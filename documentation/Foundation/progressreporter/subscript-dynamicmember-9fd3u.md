# subscript(dynamicMember:)

**Framework**: Foundation  
**Kind**: subscript

Gets or sets custom double properties.

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
final subscript<P>(dynamicMember key: KeyPath<ProgressManager.Properties, P.Type>) -> P.Value where P : ProgressManager.Property, P.Summary == Double, P.Value == Double { get }
```

#### Overview

This subscript provides read-write access to custom progress properties where both the value and summary types are `Double`. If the property has not been set, the getter returns the property’s default value.

## Parameters

- `key`: A key path to the custom double property type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressreporter/subscript(dynamicmember:)-9fd3u)*