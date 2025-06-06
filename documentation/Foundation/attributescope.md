# AttributeScope

**Framework**: Foundation  
**Kind**: protocol

A type that organizes attributes into a grouping, and supports dynamic member lookup and serialization of attribute keys.

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
protocol AttributeScope : DecodingConfigurationProviding, EncodingConfigurationProviding
```

#### Overview

Attribute owners — typically frameworks — define attributes with [`AttributedStringKey`](attributedstringkey.md) types. To allow access to attributes with dynamic member lookup, owners create one or more structures that conform to [`AttributeScope`](attributescope.md). The scopes provide short names for their attributes that map to the [`AttributedStringKey`](attributedstringkey.md) type. The following example shows how to do this:

```swift
struct TextStyleAttributes : AttributeScope {
    let foregroundColor : ForegroundColorAttribute // ForegroundColorAttribute.Value == Color
    let backgroundColor : BackgroundColorAttribute // BackgroundColorAttribute.Value == Color
    let underlineStyle : UnderlineStyleAttribute // UnderlineStyleAttribute.Value == UnderlineStyle
    // etc.
}
```

This allows callers to use a syntax like `myAttributedString.foregroundColor = .red`.

## Topics

### Supporting Coding Configurations
- [static var encodingConfiguration: AttributeScopeCodableConfiguration](attributescope/encodingconfiguration.md)
  The configuration for encoding the attribute scope.
- [static var decodingConfiguration: AttributeScopeCodableConfiguration](attributescope/decodingconfiguration.md)
  The configuration for decoding the attribute scope.

## Relationships

### Inherits From
- [DecodingConfigurationProviding](decodingconfigurationproviding.md)
- [EncodingConfigurationProviding](encodingconfigurationproviding.md)
### Conforming Types
- [AttributeScopes.AccessibilityAttributes](attributescopes/accessibilityattributes.md)
- [AttributeScopes.AppKitAttributes](attributescopes/appkitattributes.md)
- [AttributeScopes.FoundationAttributes](attributescopes/foundationattributes.md)
- [AttributeScopes.FoundationAttributes.NumberFormatAttributes](attributescopes/foundationattributes/numberformatattributes.md)
- [AttributeScopes.SwiftUIAttributes](attributescopes/swiftuiattributes.md)
- [AttributeScopes.UIKitAttributes](attributescopes/uikitattributes.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescope)*