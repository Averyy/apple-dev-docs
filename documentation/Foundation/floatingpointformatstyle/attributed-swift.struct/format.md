# format(_:)

**Framework**: Foundation  
**Kind**: method

Formats a floating-point value, using this style.

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
func format(_ value: Value) -> AttributedString
```

#### Return Value

An attributed string representation of `value`, formatted according to the style’s configuration. The returned string contains attributes from the [`AttributeScopes.FoundationAttributes.NumberFormatAttributes`](attributescopes/foundationattributes/numberformatattributes.md) attribute scope to indicate runs formatted by this format style.

## Parameters

- `value`: The floating-point value to format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/floatingpointformatstyle/attributed-swift.struct/format(_:))*