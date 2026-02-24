# subscript(dynamicMember:)

**Framework**: Foundation  
**Kind**: subscript

Provides dynamic member lookup for translation attributes.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
subscript<T>(dynamicMember keyPath: KeyPath<AttributeScopes.TranslationAttributes, T>) -> T where T : AttributedStringKey { get }
```

#### Return Value

The attribute key type that can be used to get or set attribute values.

#### Overview

This subscript enables the convenient dot-syntax access to translation attributes on [`AttributedString`](attributedstring.md):

```swift
var text = AttributedString("Product Name")
text.skipsTranslation = true
```

## Parameters

- `keyPath`: A key path to a property in the `TranslationAttributes` scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedynamiclookup/subscript(dynamicmember:)-4n6dp)*