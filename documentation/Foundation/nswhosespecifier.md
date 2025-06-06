# NSWhoseSpecifier

**Framework**: Foundation  
**Kind**: class

A specifier that indicates every object in a collection matching a condition.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSWhoseSpecifier
```

#### Overview

`NSWhoseSpecifier` specifies every object in a collection (or every element in a container) that matches the condition defined by a single Boolean expression or multiple Boolean expressions connected by logical operators. `NSWhoseSpecifier` is unique among object specifiers in that its top-level container is typically not the application object but an evaluated object specifier involved in the tested-for condition. An `NSWhoseSpecifier` object encapsulates a “test” object for defining this condition. A test object is instantiated from a subclass of the abstract [`NSScriptWhoseTest`](nsscriptwhosetest.md) class, whose one declared method is [`isTrue()`](nsscriptwhosetest/istrue().md). See “Boolean Expressions and Logical Operations” in [`NSScriptObjectSpecifier`](nsscriptobjectspecifier.md) and the descriptions in NSComparisonMethods and NSScriptingComparisonMethods for more information.

The set of elements specified by an `NSWhoseSpecifier` object can be a subset of those that pass the `NSWhoseSpecifier` object’s test. This subset is specified by the various sub-element properties of the `NSWhoseSpecifier` object . Consider as an example the specifier `paragraphs where color of third word is blue`. This would be represented by an `NSWhoseSpecifier` object  that uses a test specifier and another object specifier to identify a subset of the objects with the specified property. That is, the specifier’s property is `paragraphs`; the test specifier is an index specifier with property `words` and `index 3`; and the qualifier is a key value qualifier for key `color` and value `[NSColor blueColor]`. The test object specifier (`word at index 3`) is evaluated for each object (paragraph) using that object as the container; the resulting objects (if any) are tested with the qualifier (`color blue`).

`NSWhoseSpecifier` is part of Cocoa’s built-in script handling. You don’t normally subclass it.

## Topics

### Initializing a whose specifier
- [init(containerClassDescription: NSScriptClassDescription, containerSpecifier: NSScriptObjectSpecifier?, key: String, test: NSScriptWhoseTest)](nswhosespecifier/init(containerclassdescription:containerspecifier:key:test:).md)
  Returns an `NSWhoseSpecifier` object initialized with the given attributes.
### Accessing information about a whose specifier
- [var endSubelementIdentifier: NSWhoseSpecifier.SubelementIdentifier](nswhosespecifier/endsubelementidentifier.md)
  Sets the end sub-element identifier for the specifier to the value of a given sub-element.
- [var endSubelementIndex: Int](nswhosespecifier/endsubelementindex.md)
  Sets the index position of the last sub-element within the range of objects being tested that pass the specifier’s test.
- [var startSubelementIdentifier: NSWhoseSpecifier.SubelementIdentifier](nswhosespecifier/startsubelementidentifier.md)
  Returns the start sub-element identifier for the receiver.
- [var startSubelementIndex: Int](nswhosespecifier/startsubelementindex.md)
  Returns the index position of the first sub-element within the range of objects being tested that pass the receiver’s test.
- [var test: NSScriptWhoseTest](nswhosespecifier/test.md)
  Returns the test object encapsulated by the receiver.
### Constants
- [NSWhoseSpecifier.SubelementIdentifier](nswhosespecifier/subelementidentifier.md)
  `NSWhoseSpecifier` uses these constants to specify sub-elements within the collection of objects being tested that pass the specifier’s test.
### Initializers
- [init?(coder: NSCoder)](nswhosespecifier/init(coder:).md)

## Relationships

### Inherits From
- [NSScriptObjectSpecifier](nsscriptobjectspecifier.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSScriptObjectSpecifier](nsscriptobjectspecifier.md)
  An abstract class used to represent natural language expressions.
- [class NSPropertySpecifier](nspropertyspecifier.md)
  A specifier for a simple attribute value, a one-to-one relationship, or all elements of a to-many relationship.
- [class NSPositionalSpecifier](nspositionalspecifier.md)
  A specifier for an insertion point in a container relative to another object in the container.
- [class NSRandomSpecifier](nsrandomspecifier.md)
  A specifier for an arbitrary object in a collection or, if not a one-to-many relationship, the sole object.
- [class NSRangeSpecifier](nsrangespecifier.md)
  A specifier for a range of objects in a container.
- [class NSUniqueIDSpecifier](nsuniqueidspecifier.md)
  A specifier for an object in a collection (or container) by unique ID.
- [class NSNameSpecifier](nsnamespecifier.md)
  A specifier for an object in a collection (or container) by name.
- [class NSMiddleSpecifier](nsmiddlespecifier.md)
  A specifier indicating the middle object in a collection or, if not a one-to-many relationship, the sole object.
- [class NSIndexSpecifier](nsindexspecifier.md)
  A specifier representing an object in a collection (or container) with an index number.
- [class NSRelativeSpecifier](nsrelativespecifier.md)
  A specifier that indicates an object in a collection by its position relative to another object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nswhosespecifier)*