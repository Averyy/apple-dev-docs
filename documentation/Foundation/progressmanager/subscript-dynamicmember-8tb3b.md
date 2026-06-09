# subscript(dynamicMember:)

**Framework**: Foundation  
**Kind**: subscript

Gets or sets custom unsigned integer properties.

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
final subscript<P>(dynamicMember key: KeyPath<ProgressManager.Properties, P.Type>) -> UInt64 where P : ProgressManager.Property, P.Summary == [UInt64], P.Value == UInt64 { get set }
```

#### Overview

This subscript provides read-write access to custom progress properties where the value type is `UInt64` and the summary type is `[UInt64]`. If the property has not been set, the getter returns the property’s default value.

## Parameters

- `key`: A key path to the custom unsigned integer property type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressmanager/subscript(dynamicmember:)-8tb3b)*