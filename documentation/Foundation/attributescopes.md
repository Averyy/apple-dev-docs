# AttributeScopes

**Framework**: Foundation  
**Kind**: enum

Collections of attributes that system frameworks define.

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
@frozen
enum AttributeScopes
```

#### Overview

Attribute scopes define groups of attributes appropriate for use with attributed strings in a certain domain. Attribute definitions contain a name, value type, and encode/decode methods to support serialization.

For example, the [`AttributeScopes.FoundationAttributes`](attributescopes/foundationattributes.md) scope provides an attribute type for a link to a URL, [`AttributeScopes.FoundationAttributes.LinkAttribute`](attributescopes/foundationattributes/linkattribute.md), along with a property to access this type, [`link`](attributescopes/foundationattributes/link.md). Because [`AttributeScopes.FoundationAttributes`](attributescopes/foundationattributes.md) implements [`AttributeDynamicLookup`](attributedynamiclookup.md), you can access the link attribute by name, as this example shows:

```swift
var attrStr = AttributedString("Example site")
attrStr.link = URL(string: "http://example.com")
```

## Topics

### Foundation-Defined Attributes
- [var foundation: AttributeScopes.FoundationAttributes.Type](attributescopes/foundation.md)
  A property for accessing the attribute scopes that Foundation defines.
- [AttributeScopes.FoundationAttributes](attributescopes/foundationattributes.md)
  Attribute scopes that Foundation defines.
### SwiftUI-Defined Attributes
- [var swiftUI: AttributeScopes.SwiftUIAttributes.Type](attributescopes/swiftui.md)
  A property for accessing the attribute scopes that SwiftUI defines.
- [AttributeScopes.SwiftUIAttributes](attributescopes/swiftuiattributes.md)
  Attribute scopes that SwiftUI defines.
### UIKit-Defined Attributes
- [var uiKit: AttributeScopes.UIKitAttributes.Type](attributescopes/uikit.md)
  A property for accessing the attribute scopes that UIKit defines.
- [AttributeScopes.UIKitAttributes](attributescopes/uikitattributes.md)
  Attribute scopes that UIKit defines.
### AppKit-Defined Attributes
- [var appKit: AttributeScopes.AppKitAttributes.Type](attributescopes/appkit.md)
  A property for accessing the attribute scopes that AppKit defines.
- [AttributeScopes.AppKitAttributes](attributescopes/appkitattributes.md)
  Attribute scopes that AppKit defines.
### Structures
- [AttributeScopes.AccessibilityAttributes](attributescopes/accessibilityattributes.md)
- [AttributeScopes.CoreTextAttributes](attributescopes/coretextattributes.md)
  A namespace for attributes defined by CoreText.
- [AttributeScopes.SpeechAttributes](attributescopes/speechattributes.md)
### Instance Properties
- [var accessibility: AttributeScopes.AccessibilityAttributes.Type](attributescopes/accessibility.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)

## See Also

- [enum AttributeDynamicLookup](attributedynamiclookup.md)
  A type to support dynamic member lookup of attributes and containers.
- [struct ScopedAttributeContainer](scopedattributecontainer.md)
  An attribute container that allows dynamic member lookup of its contents within the specified attribute scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes)*