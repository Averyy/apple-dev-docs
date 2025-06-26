# AttributedString

**Framework**: Foundation  
**Kind**: struct

A value type for a string with associated attributes for portions of its text.

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
struct AttributedString
```

#### Overview

Attributed strings are character strings that have attributes for individual characters or ranges of characters. Attributes provide traits like visual styles for display, accessibility for guided access, and hyperlink data for linking between data sources. Attribute keys provide the name and value type of each attribute. System frameworks like Foundation and SwiftUI define common keys, and you can define your own in custom extensions.

##### String Attributes

You can apply an attribute to an entire string, or to a range within the string. The string represents each range with consistent attributes as a .

[`AttributedString`](attributedstring.md) uses subscripts and dynamic member lookup to simplify working with attributes from your call points. In its most verbose form, you set an attribute by creating an [`AttributeContainer`](attributecontainer.md) and merging it into an existing attributed string, like this:

```swift
var attributedString = AttributedString("This is a string with empty attributes.")
var container = AttributeContainer()
container[AttributeScopes.AppKitAttributes.ForegroundColorAttribute.self] = .red
attributedString.mergeAttributes(container, mergePolicy: .keepNew)
```

Using the attributed string’s [`subscript(_:)`](attributedstringprotocol/subscript(_:)-4thnp.md) method, you can omit the explicit use of an [`AttributeContainer`](attributecontainer.md) and just set the attribute by its type:

```swift
attributedString[AttributeScopes.AppKitAttributes.ForegroundColorAttribute.self] = .yellow
```

Because an [`AttributedString`](attributedstring.md) supports dynamic member lookup — as described under [`Attributes`](https://developer.apple.comhttps://docs.swift.org/swift-book/ReferenceManual/Attributes.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) — you can access its subscripts with dot syntax instead. When combined with properties like [`foregroundColor`](attributescopes/appkitattributes/foregroundcolor.md) that return the attribute key type, this final form offers a natural way to set an attribute that applies to an entire string:

```swift
attributedString.foregroundColor = .green
```

This example works because AppKit defines an [`AttributeScope`](attributescope.md), [`AttributeScopes.AppKitAttributes`](attributescopes/appkitattributes.md), in which the property [`foregroundColor`](attributescopes/appkitattributes/foregroundcolor.md) returns the type `AttributeScopes.AppKitAttributes.ForegroundColorAttribute`. Because AppKit’s attribute scope implements [`AttributeDynamicLookup`](attributedynamiclookup.md), the dot syntax resolves to an equivalent subscript expression, allowing `attributedString.foregroundColor` to replace `attributedString[AttributeScopes.AppKitAttributes.ForegroundColorAttribute.self]`.

You can also set an attribute to apply only to part of an attributed string, by applying the attribute to a range, as seen here:

```swift
var attributedString = AttributedString("The first month of your subscription is free.")
guard let range = attributedString.range(of: "free") else {return}
attributedString[range].foregroundColor = .green
```

You can access portions of the string with unique combinations of attributes by iterating over the string’s `runs` property.

You can define your own custom attributes by creating types that conform to [`AttributedStringKey`](attributedstringkey.md), and collecting them in an [`AttributeScope`](attributescope.md). Custom keys should also extend [`AttributeDynamicLookup`](attributedynamiclookup.md), so callers can use dot-syntax to access the attribute.

##### Creating Attributed Strings with Markdown

You can create an attributed string by passing a standard [`String`](https://developer.apple.com/documentation/Swift/String) or [`Data`](data.md) instance that contains Markdown to initializers like [`init(markdown:options:baseURL:)`](attributedstring/init(markdown:options:baseurl:)-52n3u.md). The attributed string creates attributes by parsing the markup in the string.

```swift
do {
    let thankYouString = try AttributedString(
        markdown:"**Thank you!** Please visit our [website](https://example.com)")
} catch {
    print("Couldn't parse the string. \(error.localizedDescription)")
}
```

Localized strings that you load from strings files with initializers like [`init(localized:options:table:bundle:locale:comment:)`](attributedstring/init(localized:options:table:bundle:locale:comment:)-8dlnl.md) can also contain Markdown to add styling. In addition, these localized attributed string initializers can apply the [`replacementIndex`](attributescopes/foundationattributes/replacementindex.md) attribute, which allows you to determine the range of replacement strings, whose order may vary between languages.

By declaring new attributes that conform to [`MarkdownDecodableAttributedStringKey`](markdowndecodableattributedstringkey.md), you can add attributes that you invoke by using Apple’s Markdown extension syntax: `^[text](name:value, name:value, …)`. See the sample code project doc:building-a-localized-food-ordering-app for an example of creating custom attributes and using them with Markdown.

Localized attributed strings can also use the extension syntax to indicate parts of the string where the system can apply automatic grammar agreement. See the initializers that take a `localized:` parameter for examples of this extension syntax, as used with automatic grammar agreement.

##### Attribute Scopes

The [`AttributedString`](attributedstring.md) API defines keys for common uses, such as text styling, semantically marking up formattable types like dates and numbers, and hyperlinking. You can find these in the [`AttributeScopes`](attributescopes.md) enumeration, which contains attributes for AppKit, Foundation, SwiftUI, and UIKit.

You can define your own attributes by implementing [`AttributedStringKey`](attributedstringkey.md), and reference them by name by collecting them in an [`AttributeScope`](attributescope.md).

## Topics

### Creating an Attributed String
- [init()](attributedstring/init.md)
  Creates an empty attributed string.
- [init(AttributedSubstring)](attributedstring/init(_:)-8tnoq.md)
  Creates an attributed string from an attributed substring.
- [init(String, attributes: AttributeContainer)](attributedstring/init(_:attributes:)-2a45h.md)
  Creates an attributed string from a string and an attribute container.
- [init(Substring, attributes: AttributeContainer)](attributedstring/init(_:attributes:)-8jqhp.md)
  Creates an attributed string from a substring and an attribute container.
- [init<S>(S, attributes: AttributeContainer)](attributedstring/init(_:attributes:)-8l0iq.md)
  Creates an attributed string from a character sequence and an attribute container.
- [struct AttributeContainer](attributecontainer.md)
  A container for attribute keys and values.
### Creating a Localized Attributed String
- [init(localized: String.LocalizationValue, options: AttributedString.FormattingOptions, table: String?, bundle: Bundle?, locale: Locale?, comment: StaticString?)](attributedstring/init(localized:options:table:bundle:locale:comment:)-8dlnl.md)
  Creates an attributed string by looking up a localized string from the app’s bundle.
- [init<S>(localized: String.LocalizationValue, options: AttributedString.FormattingOptions, table: String?, bundle: Bundle?, locale: Locale?, comment: StaticString?, including: S.Type)](attributedstring/init(localized:options:table:bundle:locale:comment:including:)-8uknv.md)
  Creates an attributed string by looking up a localized string from the app’s bundle, including an attribute scope.
- [init<S>(localized: String.LocalizationValue, options: AttributedString.FormattingOptions, table: String?, bundle: Bundle?, locale: Locale?, comment: StaticString?, including: KeyPath<AttributeScopes, S.Type>)](attributedstring/init(localized:options:table:bundle:locale:comment:including:)-5jzpg.md)
  Creates an attributed string by looking up a localized string from the app’s bundle, including an attribute scope that a key path identifies.
- [String.LocalizationValue](../Swift/String/LocalizationValue.md)
  A reference to a localizable string, with optional string interpolation.
- [AttributedString.FormattingOptions](attributedstring/formattingoptions.md)
  Options that affect the handling of attributes.
- [init(localized: LocalizedStringResource)](attributedstring/init(localized:).md)
  Creates a localized attributed string from a localized string resource.
- [init<S>(localized: LocalizedStringResource, including: S.Type)](attributedstring/init(localized:including:)-2xebo.md)
  Creates a localized attributed string from a localized string resource, including an attribute scope.
- [init<S>(localized: LocalizedStringResource, including: KeyPath<AttributeScopes, S.Type>)](attributedstring/init(localized:including:)-15xc5.md)
  Creates a localized attributed string from a localized string resource, including an attribute scope that a key path identifies.
- [struct LocalizedStringResource](localizedstringresource.md)
  A reference to a localizable string, accessible from another process.
### Creating a Localized Attributed String with a Default Value
- [init(localized: StaticString, defaultValue: String.LocalizationValue, options: AttributedString.FormattingOptions, table: String?, bundle: Bundle?, locale: Locale?, comment: StaticString?)](attributedstring/init(localized:defaultvalue:options:table:bundle:locale:comment:)-4n8e2.md)
  Creates an attributed string by looking up a localized string from the app’s bundle, using a default value if necessary.
- [init<S>(localized: StaticString, defaultValue: String.LocalizationValue, options: AttributedString.FormattingOptions, table: String?, bundle: Bundle?, locale: Locale?, comment: StaticString?, including: S.Type)](attributedstring/init(localized:defaultvalue:options:table:bundle:locale:comment:including:)-2elmp.md)
  Creates an attributed string by looking up a localized string from the app’s bundle, including an attribute scope, using a default value if necessary.
- [init<S>(localized: StaticString, defaultValue: String.LocalizationValue, options: AttributedString.FormattingOptions, table: String?, bundle: Bundle?, locale: Locale?, comment: StaticString?, including: KeyPath<AttributeScopes, S.Type>)](attributedstring/init(localized:defaultvalue:options:table:bundle:locale:comment:including:)-9gjtg.md)
  Creates an attributed string by looking up a localized string from the app’s bundle, including an attribute scope that a key path identifies, using a default value if necessary.
### Creating an Attributed String from Markdown
- [Instantiating Attributed Strings with Markdown Syntax](instantiating-attributed-strings-with-markdown-syntax.md)
  Use a Markdown-syntax string to iniitalize an attributed string with standard or custom attributes.
### Creating an Attributed String from a Reference Type
- [init<S>(NSAttributedString, including: S.Type) throws](attributedstring/init(_:including:)-9no47.md)
  Creates a value-type attributed string from a reference type, including an attribute scope.
- [init<S>(NSAttributedString, including: KeyPath<AttributeScopes, S.Type>) throws](attributedstring/init(_:including:)-puv0.md)
  Creates a value-type attributed string from a reference type, including an attribute scope that a key path identifies.
- [init(NSAttributedString)](attributedstring/init(_:)-1fru0.md)
  Creates a value-type attributed string from a reference type.
### Creating a Duplicate Attributed String
- [init<S, T>(T, including: S.Type)](attributedstring/init(_:including:)-6u3ho.md)
  Creates an attributed string from another attributed string, including an attribute scope.
- [init<S, T>(T, including: KeyPath<AttributeScopes, S.Type>)](attributedstring/init(_:including:)-9ejyj.md)
  Creates an attributed string from another attributed string, including an attribute scope that a key path identifies.
### Applying and Modifying Attributes
- [AttributedString.AttributeMergePolicy](attributedstring/attributemergepolicy.md)
  An enumeration of behaviors to apply when merging attributes.
- [protocol AttributedStringAttributeMutation](attributedstringattributemutation.md)
  A protocol that defines in-place mutations for attributes in an attributed string.
### Using Defined Attributes
- [enum AttributeScopes](attributescopes.md)
  Collections of attributes that system frameworks define.
- [enum AttributeDynamicLookup](attributedynamiclookup.md)
  A type to support dynamic member lookup of attributes and containers.
- [struct ScopedAttributeContainer](scopedattributecontainer.md)
  An attribute container that allows dynamic member lookup of its contents within the specified attribute scope.
### Accessing Indices
- [Accessing Indicies Within an Attributed String](accessing-indicies-within-an-attributed-string.md)
  Access a position within an attributed string, offset from the beginning, or before or after another known position.
### Accessing Views into the Attributed String
- [AttributedString.CharacterView](attributedstring/characterview.md)
  A view into the underlying storage of the attributed string, as Unicode characters.
- [AttributedString.UnicodeScalarView](attributedstring/unicodescalarview.md)
  A view into the underlying storage of the attributed string, as Unicode scalars.
- [AttributedString.Runs](attributedstring/runs.md)
  An iterable view into segments of the attributed string, each of which indicates where a run of identical attributes begins or ends.
### Modifying an Attributed String
- [func insert(some AttributedStringProtocol, at: AttributedString.Index)](attributedstring/insert(_:at:).md)
  Inserts the specified string at a specific index in the attributed string.
- [AttributedString.Index](attributedstring/index.md)
  A type that represents the position of a character or code unit within an attributed string.
- [func removeSubrange(some RangeExpression<AttributedString.Index>)](attributedstring/removesubrange(_:).md)
  Removes a range of characters from the attributed string.
- [func replaceSubrange(some RangeExpression<AttributedString.Index>, with: some AttributedStringProtocol)](attributedstring/replacesubrange(_:with:).md)
  Replaces the contents in a range of the attributed string.
### Transforming Attributes
- [func transformingAttributes<K>(K.Type, (inout AttributedString.SingleAttributeTransformer<K>) -> Void) -> AttributedString](attributedstring/transformingattributes(_:_:)-9prm2.md)
  Returns an attributed string by calling a closure that transforms one attribute of a source attributed string.
- [func transformingAttributes<K>(KeyPath<AttributeDynamicLookup, K>, (inout AttributedString.SingleAttributeTransformer<K>) -> Void) -> AttributedString](attributedstring/transformingattributes(_:_:)-64qnl.md)
  Returns an attributed string by calling a closure that transforms one attribute, which a key path identifies, of a source attributed string.
- [func transformingAttributes<K1, K2>(K1.Type, K2.Type, (inout AttributedString.SingleAttributeTransformer<K1>, inout AttributedString.SingleAttributeTransformer<K2>) -> Void) -> AttributedString](attributedstring/transformingattributes(_:_:_:)-7kw1o.md)
  Returns an attributed string by calling a closure that transforms two attributes of a source attributed string.
- [func transformingAttributes<K1, K2>(KeyPath<AttributeDynamicLookup, K1>, KeyPath<AttributeDynamicLookup, K2>, (inout AttributedString.SingleAttributeTransformer<K1>, inout AttributedString.SingleAttributeTransformer<K2>) -> Void) -> AttributedString](attributedstring/transformingattributes(_:_:_:)-8gt2n.md)
  Returns an attributed string created by calling a closure that transforms two attributes, which key paths identify, of a source attributed string.
- [func transformingAttributes<K1, K2, K3>(K1.Type, K2.Type, K3.Type, (inout AttributedString.SingleAttributeTransformer<K1>, inout AttributedString.SingleAttributeTransformer<K2>, inout AttributedString.SingleAttributeTransformer<K3>) -> Void) -> AttributedString](attributedstring/transformingattributes(_:_:_:_:)-4owv7.md)
  Returns an attributed string by calling a closure that transforms three attributes of a source attributed string.
- [func transformingAttributes<K1, K2, K3>(KeyPath<AttributeDynamicLookup, K1>, KeyPath<AttributeDynamicLookup, K2>, KeyPath<AttributeDynamicLookup, K3>, (inout AttributedString.SingleAttributeTransformer<K1>, inout AttributedString.SingleAttributeTransformer<K2>, inout AttributedString.SingleAttributeTransformer<K3>) -> Void) -> AttributedString](attributedstring/transformingattributes(_:_:_:_:)-5xmlf.md)
  Returns an attributed string by calling a closure that transforms three attributes, which key paths identify, of a source attributed string.
- [func transformingAttributes<K1, K2, K3, K4>(K1.Type, K2.Type, K3.Type, K4.Type, (inout AttributedString.SingleAttributeTransformer<K1>, inout AttributedString.SingleAttributeTransformer<K2>, inout AttributedString.SingleAttributeTransformer<K3>, inout AttributedString.SingleAttributeTransformer<K4>) -> Void) -> AttributedString](attributedstring/transformingattributes(_:_:_:_:_:)-9uodg.md)
  Returns an attributed string by calling a closure that transforms four attributes of a source attributed string.
- [func transformingAttributes<K1, K2, K3, K4>(KeyPath<AttributeDynamicLookup, K1>, KeyPath<AttributeDynamicLookup, K2>, KeyPath<AttributeDynamicLookup, K3>, KeyPath<AttributeDynamicLookup, K4>, (inout AttributedString.SingleAttributeTransformer<K1>, inout AttributedString.SingleAttributeTransformer<K2>, inout AttributedString.SingleAttributeTransformer<K3>, inout AttributedString.SingleAttributeTransformer<K4>) -> Void) -> AttributedString](attributedstring/transformingattributes(_:_:_:_:_:)-all0.md)
  Returns an attributed string created by calling a closure that transforms four attributes, which key paths identify, of a source attributed string.
- [func transformingAttributes<K1, K2, K3, K4, K5>(K1.Type, K2.Type, K3.Type, K4.Type, K5.Type, (inout AttributedString.SingleAttributeTransformer<K1>, inout AttributedString.SingleAttributeTransformer<K2>, inout AttributedString.SingleAttributeTransformer<K3>, inout AttributedString.SingleAttributeTransformer<K4>, inout AttributedString.SingleAttributeTransformer<K5>) -> Void) -> AttributedString](attributedstring/transformingattributes(_:_:_:_:_:_:)-3i7ac.md)
  Returns an attributed string created by calling a closure that transforms five attributes of a source attributed string.
- [func transformingAttributes<K1, K2, K3, K4, K5>(KeyPath<AttributeDynamicLookup, K1>, KeyPath<AttributeDynamicLookup, K2>, KeyPath<AttributeDynamicLookup, K3>, KeyPath<AttributeDynamicLookup, K4>, KeyPath<AttributeDynamicLookup, K5>, (inout AttributedString.SingleAttributeTransformer<K1>, inout AttributedString.SingleAttributeTransformer<K2>, inout AttributedString.SingleAttributeTransformer<K3>, inout AttributedString.SingleAttributeTransformer<K4>, inout AttributedString.SingleAttributeTransformer<K5>) -> Void) -> AttributedString](attributedstring/transformingattributes(_:_:_:_:_:_:)-9hppo.md)
  Returns an attributed string created by calling a closure that transforms five attributes, which key paths identify, of a source attributed string.
- [AttributedString.SingleAttributeTransformer](attributedstring/singleattributetransformer.md)
  A type that transforms an attribute by altering its range or value, or by replacing it entirely.
### Accessing Whole-String Attributes
- [enum AttributeDynamicLookup](attributedynamiclookup.md)
  A type to support dynamic member lookup of attributes and containers.
- [struct ScopedAttributeContainer](scopedattributecontainer.md)
  An attribute container that allows dynamic member lookup of its contents within the specified attribute scope.
### Combining Attributed Strings
- [func append(some AttributedStringProtocol)](attributedstring/append(_:).md)
  Appends a string to the attributed string.
- [static func + (AttributedString, AttributedString) -> AttributedString](attributedstring/+(_:_:)-8sbsq.md)
  Concatenates two attributed strings.
- [static func + (AttributedString, some AttributedStringProtocol) -> AttributedString](attributedstring/+(_:_:)-drfc.md)
  Concatenates two attributed strings or substrings.
- [static func += (inout AttributedString, AttributedString)](attributedstring/+=(_:_:)-4dk88.md)
  Appends an attributed string to another attributed string.
- [static func += (inout AttributedString, some AttributedStringProtocol)](attributedstring/+=(_:_:)-6yimu.md)
  Appends an attributed string or substring to another attributed string.
### Performing Automatic Grammar Agreement
- [func inflected() -> AttributedString](attributedstring/inflected.md)
  Applies automatic grammar agreement inflection rules to the attributed string and returns the result.
### Performing String Interpolation
- [AttributedString.InterpolationOptions](attributedstring/interpolationoptions.md)
  Options that affect the behavior of string interpolation on the attributed string.
### Encoding and Decoding
- [struct AttributeScopeCodableConfiguration](attributescopecodableconfiguration.md)
  A configuration type for encoding and decoding attributed strings.
- [Encoding and Decoding Attributed String Keys](encoding-and-decoding-attributed-string-keys.md)
  Protocols adopted by attribute keys to encode or decode data.
### Structures
- [AttributedString.AdaptiveImageGlyph](attributedstring/adaptiveimageglyph.md)
- [AttributedString.AttributeInvalidationCondition](attributedstring/attributeinvalidationcondition.md)
- [AttributedString.LineHeight](attributedstring/lineheight.md)
  The line height definition of a paragraph.
- [AttributedString.LocalizationOptions](attributedstring/localizationoptions.md)
  Configuration options for the localization of text.
- [AttributedString.MarkdownSourcePosition](attributedstring/markdownsourceposition.md)
  The position of attributed string text in its original Markdown source string.
- [AttributedString.UTF16View](attributedstring/utf16view.md)
  A view of an attributed string’s contents as a collection of UTF-16 code units.
- [AttributedString.UTF8View](attributedstring/utf8view.md)
  A view of an attributed string’s contents as a collection of UTF-8 code units.
### Initializers
- [init(DiscontiguousAttributedSubstring)](attributedstring/init(_:)-83wi.md)
  Creates an attributed string from a discontiguous attributed substring.
- [init(localized: StaticString, defaultValue: String.LocalizationValue, options: AttributedString.LocalizationOptions, table: String?, bundle: Bundle?, locale: Locale?, comment: StaticString?)](attributedstring/init(localized:defaultvalue:options:table:bundle:locale:comment:)-2nmk8.md)
- [init<S>(localized: StaticString, defaultValue: String.LocalizationValue, options: AttributedString.LocalizationOptions, table: String?, bundle: Bundle?, locale: Locale?, comment: StaticString?, including: S.Type)](attributedstring/init(localized:defaultvalue:options:table:bundle:locale:comment:including:)-6qaoe.md)
- [init<S>(localized: StaticString, defaultValue: String.LocalizationValue, options: AttributedString.LocalizationOptions, table: String?, bundle: Bundle?, locale: Locale?, comment: StaticString?, including: KeyPath<AttributeScopes, S.Type>)](attributedstring/init(localized:defaultvalue:options:table:bundle:locale:comment:including:)-iisj.md)
- [init(localized: LocalizedStringResource, options: AttributedString.LocalizationOptions)](attributedstring/init(localized:options:).md)
- [init<S>(localized: LocalizedStringResource, options: AttributedString.LocalizationOptions, including: S.Type)](attributedstring/init(localized:options:including:)-3dycp.md)
- [init<S>(localized: LocalizedStringResource, options: AttributedString.LocalizationOptions, including: KeyPath<AttributeScopes, S.Type>)](attributedstring/init(localized:options:including:)-4cbfv.md)
- [init(localized: String.LocalizationValue, options: AttributedString.LocalizationOptions, table: String?, bundle: Bundle?, locale: Locale?, comment: StaticString?)](attributedstring/init(localized:options:table:bundle:locale:comment:)-1w4s.md)
- [init<S>(localized: String.LocalizationValue, options: AttributedString.LocalizationOptions, table: String?, bundle: Bundle?, locale: Locale?, comment: StaticString?, including: KeyPath<AttributeScopes, S.Type>)](attributedstring/init(localized:options:table:bundle:locale:comment:including:)-3zy6h.md)
- [init<S>(localized: String.LocalizationValue, options: AttributedString.LocalizationOptions, table: String?, bundle: Bundle?, locale: Locale?, comment: StaticString?, including: S.Type)](attributedstring/init(localized:options:table:bundle:locale:comment:including:)-8ao6x.md)
- [init(transferable: AttributedTextFormatting.Transferable, in: EnvironmentValues) throws](attributedstring/init(transferable:in:).md)
  Extract an attributed string from SwiftUI’s transferable representation in a certain environment.
### Instance Methods
- [func inflected(locale: Locale, userTermOfAddress: TermOfAddress?, inflectionConcepts: [InflectionConcept]) -> AttributedString](attributedstring/inflected(locale:usertermofaddress:inflectionconcepts:).md)
- [func rangeOfAudioTimeRangeAttributes(intersecting: CMTimeRange) -> Range<AttributedString.Index>?](attributedstring/rangeofaudiotimerangeattributes(intersecting:).md)
  Returns the range of indices of the receiver that are part of given time range.
- [func removeSubranges(RangeSet<AttributedString.Index>)](attributedstring/removesubranges(_:).md)
  Removes the elements at the given indices.
- [func replaceSelection(inout AttributedTextSelection, with: some AttributedStringProtocol)](attributedstring/replaceselection(_:with:).md)
  Replace the selection with new attributed content.
- [func replaceSelection(inout AttributedTextSelection, withCharacters: some Collection<Character>)](attributedstring/replaceselection(_:withcharacters:).md)
  Replace the selection with new content, attributed with the typing attributes.
- [func transform<E>(updating: inout Range<AttributedString.Index>, body: (inout AttributedString) throws(E) -> Void) throws(E)](attributedstring/transform(updating:body:)-1b6eb.md)
  Tracks the location of the provided range throughout the mutation closure, updating the provided range to one that represents the same effective locations after the mutation.
- [func transform<E>(updating: inout [Range<AttributedString.Index>], body: (inout AttributedString) throws(E) -> Void) throws(E)](attributedstring/transform(updating:body:)-3j625.md)
  Tracks the location of the provided ranges throughout the mutation closure, updating them to new ranges that represent the same effective locations after the mutation.
- [func transform<E>(updating: Range<AttributedString.Index>, body: (inout AttributedString) throws(E) -> Void) throws(E) -> Range<AttributedString.Index>?](attributedstring/transform(updating:body:)-79te9.md)
  Tracks the location of the provided range throughout the mutation closure, returning a new, updated range that represents the same effective locations after the mutation.
- [func transform<E>(updating: [Range<AttributedString.Index>], body: (inout AttributedString) throws(E) -> Void) throws(E) -> [Range<AttributedString.Index>]?](attributedstring/transform(updating:body:)-89r96.md)
  Tracks the location of the provided ranges throughout the mutation closure, returning a new, updated range that represents the same effective locations after the mutation
- [func transform<E>(updating: inout AttributedTextSelection, body: (inout AttributedString) throws(E) -> Void) throws(E)](attributedstring/transform(updating:body:)-9wpg2.md)
  Tracks the location of the selection throughout the mutation closure, updating the selection so it represents the same effective locations after the mutation.
- [func transformAttributes<E>(in: inout AttributedTextSelection, body: (inout AttributeContainer) throws(E) -> Void) throws(E)](attributedstring/transformattributes(in:body:).md)
  Apply a change to the attributes in the entire selection.
### Subscripts
- [subscript(AttributedTextSelection) -> DiscontiguousAttributedSubstring](attributedstring/subscript(_:)-2yypq.md)
  Obtain the discontiguous substring of a selection.
- [subscript(RangeSet<AttributedString.Index>) -> DiscontiguousAttributedSubstring](attributedstring/subscript(_:)-ftoi.md)
  Returns a discontiguous substring of this discontiguous attributed string using a set of ranges to indicate the discontiguous substring bounds.
### Type Aliases
- [AttributedString.Specification](attributedstring/specification.md)
- [AttributedString.UnwrappedType](attributedstring/unwrappedtype.md)
- [AttributedString.ValueType](attributedstring/valuetype.md)
### Type Properties
- [static var defaultResolverSpecification: some ResolverSpecification](attributedstring/defaultresolverspecification.md)
### Enumerations
- [AttributedString.AttributeRunBoundaries](attributedstring/attributerunboundaries.md)
- [AttributedString.TextAlignment](attributedstring/textalignment.md)
  The explicit alignment of text within its container.
- [AttributedString.WritingDirection](attributedstring/writingdirection.md)
  The writing direction of a piece of text.
### Default Implementations
- [AttributedStringProtocol Implementations](attributedstring/attributedstringprotocol-implementations.md)
- [Transferable Implementations](attributedstring/transferable-implementations.md)

## Relationships

### Conforms To
- [AttributedStringAttributeMutation](attributedstringattributemutation.md)
- [AttributedStringProtocol](attributedstringprotocol.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [DecodableWithConfiguration](decodablewithconfiguration.md)
- [Encodable](../Swift/Encodable.md)
- [EncodableWithConfiguration](encodablewithconfiguration.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Transferable](../CoreTransferable/Transferable.md)

## See Also

- [struct AttributedSubstring](attributedsubstring.md)
  A portion of an attributed string.
- [Attributed String Supporting Types](attributed-string-supporting-types.md)
  Types that the attributed string, attributed substring, and helper types extend or conform to, for sharing common functionality.
- [class NSAttributedString](nsattributedstring.md)
  A string of text that manages data, layout, and stylistic information for ranges of characters to support rendering.
- [class NSMutableAttributedString](nsmutableattributedstring.md)
  A mutable string with associated attributes (such as visual style, hyperlinks, or accessibility data) for portions of its text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring)*