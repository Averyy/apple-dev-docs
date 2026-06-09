# subscript(dynamicMember:)

**Framework**: Foundation  
**Kind**: subscript

Gets or sets custom duration properties.

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
final subscript<P>(dynamicMember key: KeyPath<ProgressManager.Properties, P.Type>) -> Duration where P : ProgressManager.Property, P.Summary == Duration, P.Value == Duration { get }
```

#### Overview

This subscript provides read-write access to custom progress properties where the value type is `Duration` and the summary type is `Duration`. If the property has not been set, the getter returns the property’s default value.

## Parameters

- `key`: A key path to the custom duration property type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressreporter/subscript(dynamicmember:)-cjlx)*