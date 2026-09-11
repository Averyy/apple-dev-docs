# subscript(dynamicMember:)

**Framework**: Foundation  
**Kind**: subscript

Gets or sets custom URL properties.

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
final subscript<P>(dynamicMember key: KeyPath<ProgressManager.Properties, P.Type>) -> URL? where P : ProgressManager.Property, P.Summary == [URL?], P.Value == URL? { get }
```

#### Overview

This subscript provides read-write access to custom progress properties where the value type is `URL?` and the summary type is `[URL?]`. If the property has not been set, the getter returns the property’s default value.

## Parameters

- `key`: A key path to the custom URL property type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressreporter/subscript(dynamicmember:)-84opo)*