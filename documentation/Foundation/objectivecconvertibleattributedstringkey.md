# ObjectiveCConvertibleAttributedStringKey

**Framework**: Foundation  
**Kind**: protocol

A protocol that defines Objective-C interoperability with an attribute key’s value type.

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
protocol ObjectiveCConvertibleAttributedStringKey : AttributedStringKey
```

#### Overview

Conform to this protocol to allow your attributed string key to customize its Objective-C conversion behavior. This allows you to define an Objective-C value type and provide methods to convert to and from this type.

Attributed string keys that don’t conform to this protocol cast the value to [`AnyObject`](https://developer.apple.com/documentation/Swift/AnyObject) before converting to Objective-C. When converting from Objective-C, the value casts to the key’s [`Value`](attributedstringkey/value.md) type. In cases where Swift types bridge automatically to Objective-C types, like [`String`](https://developer.apple.com/documentation/Swift/String) to [`NSString`](nsstring.md), this default behavior is adequate. But for unbridged value types, you need to conform to this protocol and provide the conversion methods.

## Topics

### Accessing the Objective-C Type
- [associatedtype ObjectiveCValue : NSObject](objectivecconvertibleattributedstringkey/objectivecvalue.md)
  The Objective-C type that corresponds to this key’s value type.
### Converting between Swift and Objective-C Types
- [static func objectiveCValue(for: Self.Value) throws -> Self.ObjectiveCValue](objectivecconvertibleattributedstringkey/objectivecvalue(for:).md)
  Returns an Objective-C typed value for a given value of this key’s type.
- [static func value(for: Self.ObjectiveCValue) throws -> Self.Value](objectivecconvertibleattributedstringkey/value(for:).md)
  Returns a value of this key’s type for a given Objective-C value.

## Relationships

### Inherits From
- [AttributedStringKey](attributedstringkey.md)
### Conforming Types
- [AttributeScopes.AccessibilityAttributes.AdjustedPitchAttribute](attributescopes/accessibilityattributes/adjustedpitchattribute.md)
- [AttributeScopes.AccessibilityAttributes.AnnouncementPriorityAttribute](attributescopes/accessibilityattributes/announcementpriorityattribute.md)
- [AttributeScopes.AccessibilityAttributes.HeadingLevelAttribute](attributescopes/accessibilityattributes/headinglevelattribute.md)
- [AttributeScopes.AccessibilityAttributes.TextualContextAttribute](attributescopes/accessibilityattributes/textualcontextattribute.md)
- [AttributeScopes.AppKitAttributes.AdaptiveImageGlyphAttribute](attributescopes/appkitattributes/adaptiveimageglyphattribute.md)
- [AttributeScopes.AppKitAttributes.StrikethroughStyleAttribute](attributescopes/appkitattributes/strikethroughstyleattribute.md)
- [AttributeScopes.AppKitAttributes.UnderlineStyleAttribute](attributescopes/appkitattributes/underlinestyleattribute.md)
- [AttributeScopes.FoundationAttributes.InflectionAlternativeAttribute](attributescopes/foundationattributes/inflectionalternativeattribute.md)
- [AttributeScopes.FoundationAttributes.InlinePresentationIntentAttribute](attributescopes/foundationattributes/inlinepresentationintentattribute.md)
- [AttributeScopes.FoundationAttributes.LinkAttribute](attributescopes/foundationattributes/linkattribute.md)
- [AttributeScopes.FoundationAttributes.ListItemDelimiterAttribute](attributescopes/foundationattributes/listitemdelimiterattribute.md)
- [AttributeScopes.FoundationAttributes.PersonNameComponentAttribute](attributescopes/foundationattributes/personnamecomponentattribute.md)
- [AttributeScopes.UIKitAttributes.AdaptiveImageGlyphAttribute](attributescopes/uikitattributes/adaptiveimageglyphattribute.md)
- [AttributeScopes.UIKitAttributes.StrikethroughStyleAttribute](attributescopes/uikitattributes/strikethroughstyleattribute.md)
- [AttributeScopes.UIKitAttributes.UnderlineStyleAttribute](attributescopes/uikitattributes/underlinestyleattribute.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/objectivecconvertibleattributedstringkey)*