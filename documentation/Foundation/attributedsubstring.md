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
- [AttributedString.AttributeMergePolicy](attributedstring/attributemergepolicy.md)
  An enumeration of behaviors to apply when merging attributes.
### Accessing Indices
- [Accessing Indicies Within an Attributed Substring](accessing-indicies-within-an-attributed-substring.md)
### Accessing Views into the Attributed Substring
- [AttributedString.CharacterView](attributedstring/characterview.md)
  A view into the underlying storage of the attributed string, as Unicode characters.
- [AttributedString.UnicodeScalarView](attributedstring/unicodescalarview.md)
  A view into the underlying storage of the attributed string, as Unicode scalars.
- [AttributedString.Runs](attributedstring/runs.md)
  An iterable view into segments of the attributed string, each of which indicates where a run of identical attributes begins or ends.
### Accessing the Underlying Attributed String
- [var base: AttributedString](attributedsubstring/base.md)
  Returns the underlying attributed string that the attributed substring derives from.
### Accessing Whole-Substring Attributes
- [enum AttributeDynamicLookup](attributedynamiclookup.md)
  A type to support dynamic member lookup of attributes and containers.
- [struct ScopedAttributeContainer](scopedattributecontainer.md)
  An attribute container that allows dynamic member lookup of its contents within the specified attribute scope.
### Default Implementations
- [AttributedStringProtocol Implementations](attributedsubstring/attributedstringprotocol-implementations.md)

## Relationships

### Conforms To
- [AttributedStringAttributeMutation](attributedstringattributemutation.md)
- [AttributedStringProtocol](attributedstringprotocol.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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