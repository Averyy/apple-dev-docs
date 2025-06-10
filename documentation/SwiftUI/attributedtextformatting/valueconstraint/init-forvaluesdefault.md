# init(for:values:default:)

**Framework**: SwiftUI  
**Kind**: init

Create a definition that constrains an attribute’s value to a defined set of allowed values.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
init(for attribute: AttributeKey.Type, values allowedValues: Set<AttributeKey.Value?>, default defaultValue: AttributeKey.Value?)
```

## Parameters

- `allowedValues`: A set of values that are permitted.
- `defaultValue`: A single permitted value that is used to   replace any values that are not in the set of  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextformatting/valueconstraint/init(for:values:default:))*