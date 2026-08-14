# AttributedSubstring

**Framework**: Foundation  
**Kind**: struct

A portion of an attributed string.

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
@dynamicMemberLookup
struct AttributedSubstring
```

#### Overview

[`AttributedSubstring`](attributedsubstring.md) provides no-copy access to the contents of the string within the relevant range. The distinction between an [`AttributedString`](attributedstring.md) and an [`AttributedSubstring`](attributedsubstring.md) lets you distinguish between whether you’re in possession of an entire string or just a slice of it.

Because [`AttributedSubstring`](attributedsubstring.md) and [`AttributedString`](attributedstring.md) both conform to [`AttributedStringProtocol`](attributedstringprotocol.md), working with ranges of [`AttributedString`](attributedstring.md) is natural. Modifying attributes by range works the same as it does on the base string.

If you use an [`AttributedSubstring`](attributedsubstring.md) to mutate its base [`AttributedString`](attributedstring.md), you must perform your mutation inline, as the following example shows:

```swift
// Correct use of copying.
attrStr[range].link = url

// Incorrect use of AttributedString copy. Copies the referenced range of the base
// AttributedString and mutates that.
var substr = attrStr[range]
substr.link = url
```

## Topics

### Creating Attributed Substrings
- [init()](attributedsubstring/init.md)
  Creates an empty attributed substring.
### Applying and Modifying Attributes
- [func setAttributes(AttributeContainer)](attributedsubstring/setattributes(_:).md)
  Sets the attributed substring’s attributes to those in a specified attribute container.
- [func mergeAttributes(AttributeContainer, mergePolicy: AttributedString.AttributeMergePolicy)](attributedsubstring/mergeattributes(_:mergepolicy:).md)
  Merges the attributed string’s attributes with those in a specified attribute container.
- [AttributedString.AttributeMergePolicy](attributedstring/attributemergepolicy.md)
  An enumeration of behaviors to apply when merging attributes.
- [func replaceAttributes(AttributeContainer, with: AttributeContainer)](attributedsubstring/replaceattributes(_:with:).md)
  Replaces the attributed substring’s attributes with those in a specified attribute container.
### Accessing a Range
- [subscript(some RangeExpression<AttributedString.Index>) -> AttributedSubstring](attributedsubstring/subscript(_:)-96fey.md)
  Returns a substring of the attributed substring that a range indicates.
### Accessing Indices
- [Accessing Indicies Within an Attributed Substring](accessing-indicies-within-an-attributed-substring.md)
### Accessing Views into the Attributed Substring
- [var characters: AttributedString.CharacterView](attributedsubstring/characters.md)
  The characters of the attributed string, as a view into the underlying string.
- [AttributedString.CharacterView](attributedstring/characterview.md)
  A view into the underlying storage of the attributed string, as Unicode characters.
- [var unicodeScalars: AttributedString.UnicodeScalarView](attributedsubstring/unicodescalars.md)
  The Unicode scalars of the attributed string, as a view into the underlying string.
- [AttributedString.UnicodeScalarView](attributedstring/unicodescalarview.md)
  A view into the underlying storage of the attributed string, as Unicode scalars.
- [var runs: AttributedString.Runs](attributedsubstring/runs.md)
  The attributed runs of the attributed string, as a view into the underlying string.
- [AttributedString.Runs](attributedstring/runs-swift.struct.md)
  An iterable view into segments of the attributed string, each of which indicates where a run of identical attributes begins or ends.
### Accessing the Underlying Attributed String
- [var base: AttributedString](attributedsubstring/base.md)
  Returns the underlying attributed string that the attributed substring derives from.
### Accessing Whole-Substring Attributes
- [subscript<K>(K.Type) -> K.Value?](attributedsubstring/subscript(_:)-2hp64.md)
  Returns an attribute value that corresponds to an attributed string key.
- [subscript<K>(dynamicMember _: KeyPath<AttributeDynamicLookup, K>) -> K.Value?](attributedsubstring/subscript(dynamicmember:)-3o8o1.md)
  Returns an attribute value that a key path indicates.
- [enum AttributeDynamicLookup](attributedynamiclookup.md)
  A type to support dynamic member lookup of attributes and containers.
- [subscript<S>(dynamicMember _: KeyPath<AttributeScopes, S.Type>) -> ScopedAttributeContainer<S>](attributedsubstring/subscript(dynamicmember:)-548k0.md)
  Returns a scoped attribute container that a key path indicates.
- [struct ScopedAttributeContainer](scopedattributecontainer.md)
  An attribute container that allows dynamic member lookup of its contents within the specified attribute scope.
### Default Implementations
- [AttributedStringAttributeMutation Implementations](attributedsubstring/attributedstringattributemutation-implementations.md)
- [AttributedStringProtocol Implementations](attributedsubstring/attributedstringprotocol-implementations.md)

## Relationships

### Conforms To
- [AttributedStringAttributeMutation](attributedstringattributemutation.md)
- [AttributedStringProtocol](attributedstringprotocol.md)
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct AttributedString](attributedstring.md)
  A value type for a string with associated attributes for portions of its text.
- [Attributed String Supporting Types](attributed-string-supporting-types.md)
  Types that the attributed string, attributed substring, and helper types extend or conform to, for sharing common functionality.
- [class NSAttributedString](nsattributedstring.md)
  A string of text that manages data, layout, and stylistic information for ranges of characters to support rendering.
- [class NSMutableAttributedString](nsmutableattributedstring.md)
  A mutable string with associated attributes (such as visual style, hyperlinks, or accessibility data) for portions of its text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedsubstring)*