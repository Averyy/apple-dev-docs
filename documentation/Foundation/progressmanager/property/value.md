# Value

**Framework**: Foundation  
**Kind**: associatedtype  
**Required**: Yes

The type used for individual values of this property.

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
associatedtype Value : Equatable, Sendable
```

#### Discussion

This associated type represents the type of property values that can be set on progress managers. Must be `Sendable` and `Equatable`. The currently allowed types are `Int`, `Double`, `String?`, `URL?` or `UInt64`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressmanager/property/value)*