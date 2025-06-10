# AttributedStringProtocol

**Framework**: Foundation  
**Kind**: protocol

A protocol that provides common functionality to attributed strings and attributed substrings.

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
protocol AttributedStringProtocol : AttributedStringAttributeMutation, CustomStringConvertible, Hashable, Sendable
```

#### Overview

Don’t declare new conformances to [`AttributedStringProtocol`](attributedstringprotocol.md). Only the [`AttributedString`](attributedstring.md) and [`AttributedSubstring`](attributedsubstring.md) types in the standard library are valid conforming types.

## Topics

### Applying Attributes
- [func settingAttributes(AttributeContainer) -> AttributedString](attributedstringprotocol/settingattributes(_:).md)
  Returns an attributed string by setting the attributed string’s attributes to those in a specified attribute container.
- [func mergingAttributes(AttributeContainer, mergePolicy: AttributedString.AttributeMergePolicy) -> AttributedString](attributedstringprotocol/mergingattributes(_:mergepolicy:).md)
  Returns an attributed string by merging the attributed string’s attributes with those in a specified attribute container.
- [AttributedString.AttributeMergePolicy](attributedstring/attributemergepolicy.md)
  An enumeration of behaviors to apply when merging attributes.
- [func replacingAttributes(AttributeContainer, with: AttributeContainer) -> AttributedString](attributedstringprotocol/replacingattributes(_:with:).md)
  Returns an attributed string by replacing occurrences of attributes in one attribute container with those in another attribute container.
### Searching for a Substring
- [func range<T>(of: T, options: String.CompareOptions, locale: Locale?) -> Range<AttributedString.Index>?](attributedstringprotocol/range(of:options:locale:).md)
  Returns the range of a substring in the attributed string, if it exists.
### Accessing a Range
- [subscript<R>(R) -> AttributedSubstring](attributedstringprotocol/subscript(_:)-109me.md)
  Returns a substring of the attributed string using a range to indicate the substring bounds.
### Accessing Indices
- [var startIndex: AttributedString.Index](attributedstringprotocol/startindex.md)
  The position of the first character in a nonempty attributed string.
- [var endIndex: AttributedString.Index](attributedstringprotocol/endindex.md)
  A string’s past-the-end position — the position one greater than the last valid subscript argument.
- [func index(AttributedString.Index, offsetByCharacters: Int) -> AttributedString.Index](attributedstringprotocol/index(_:offsetbycharacters:).md)
  Returns the position of the character offset a given distance, measured in characters, from a given string index.
- [func index(AttributedString.Index, offsetByRuns: Int) -> AttributedString.Index](attributedstringprotocol/index(_:offsetbyruns:).md)
  Returns the position of the run offset a given number of runs from a given string index.
- [func index(AttributedString.Index, offsetByUnicodeScalars: Int) -> AttributedString.Index](attributedstringprotocol/index(_:offsetbyunicodescalars:).md)
  Returns the position of the Unicode scalar offset a given distance, measured in Unicode scalars, from a given string index.
- [func index(afterCharacter: AttributedString.Index) -> AttributedString.Index](attributedstringprotocol/index(aftercharacter:).md)
  Returns the position of the character immediately after another charcter indicated by an index.
- [func index(afterRun: AttributedString.Index) -> AttributedString.Index](attributedstringprotocol/index(afterrun:).md)
  Returns the position of the run immediately after a run indicated by an index.
- [func index(afterUnicodeScalar: AttributedString.Index) -> AttributedString.Index](attributedstringprotocol/index(afterunicodescalar:).md)
  Returns the position of the Unicode scalar immediately after a Unicode scalar indicated by an index.
- [func index(beforeCharacter: AttributedString.Index) -> AttributedString.Index](attributedstringprotocol/index(beforecharacter:).md)
  Returns the position of the character immediately before another charcter indicated by an index.
- [func index(beforeRun: AttributedString.Index) -> AttributedString.Index](attributedstringprotocol/index(beforerun:).md)
  Returns the position of the run immediately before a run indicated by an index.
- [func index(beforeUnicodeScalar: AttributedString.Index) -> AttributedString.Index](attributedstringprotocol/index(beforeunicodescalar:).md)
  Returns the position of the Unicode scalar immediately before a Unicode scalar indicated by an index.
- [AttributedString.Index](attributedstring/index.md)
  A type that represents the position of a character or code unit within an attributed string.
### Accessing Views into the Attributed String
- [var characters: AttributedString.CharacterView](attributedstringprotocol/characters.md)
  The characters of the attributed string, as a view into the underlying string.
- [var unicodeScalars: AttributedString.UnicodeScalarView](attributedstringprotocol/unicodescalars.md)
  The Unicode scalars of the attributed string, as a view into the underlying string.
- [var runs: AttributedString.Runs](attributedstringprotocol/runs.md)
  The attributed runs of the attributed string, as a view into the underlying string.
### Accessing Whole-String Attributes
- [subscript<K>(K.Type) -> K.Value?](attributedstringprotocol/subscript(_:)-4thnp.md)
  Returns an attribute value that corresponds to an attributed string key.
- [subscript<K>(dynamicMember _: KeyPath<AttributeDynamicLookup, K>) -> K.Value?](attributedstringprotocol/subscript(dynamicmember:)-2wake.md)
  Returns an attribute value that a key path indicates.
- [enum AttributeDynamicLookup](attributedynamiclookup.md)
  A type to support dynamic member lookup of attributes and containers.
- [subscript<S>(dynamicMember _: KeyPath<AttributeScopes, S.Type>) -> ScopedAttributeContainer<S>](attributedstringprotocol/subscript(dynamicmember:)-55pcu.md)
  Returns a scoped attribute container that a key path indicates.
- [struct ScopedAttributeContainer](scopedattributecontainer.md)
  An attribute container that allows dynamic member lookup of its contents within the specified attribute scope.
### Comparing Attributed Strings or Substrings
- [static func == <RHS>(Self, RHS) -> Bool](attributedstringprotocol/==(_:_:).md)
### Instance Properties
- [var utf16: AttributedString.UTF16View](attributedstringprotocol/utf16.md)
- [var utf8: AttributedString.UTF8View](attributedstringprotocol/utf8.md)
### Default Implementations
- [CustomStringConvertible Implementations](attributedstringprotocol/customstringconvertible-implementations.md)
- [Hashable Implementations](attributedstringprotocol/hashable-implementations.md)

## Relationships

### Inherits From
- [AttributedStringAttributeMutation](attributedstringattributemutation.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [AttributedString](attributedstring.md)
- [AttributedSubstring](attributedsubstring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstringprotocol)*