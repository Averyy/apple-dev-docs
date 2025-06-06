# NSPositionalSpecifier

**Framework**: Foundation  
**Kind**: class

A specifier for an insertion point in a container relative to another object in the container.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSPositionalSpecifier
```

#### Overview

Instances of `NSPositionalSpecifier` specify an insertion point in a container relative to another object in the container, for example, `before first word` or `after paragraph 4`. The container is specified by an instance of `NSScriptObjectSpecifier`. `NSPositionalSpecifier` objects commonly encapsulate object specifiers used as arguments to the `make` (`create`) and `move` commands and indicate where the created or moved object is to be inserted relative to the object represented by an object specifier.

Invoking an accessor method to obtain information about an instance of `NSPositionalSpecifier`  causes the object to be evaluated if it hasn’t been already.

You don’t normally subclass `NSPositionalSpecifier`.

## Topics

### Initializing a positional specifier
- [init(position: NSPositionalSpecifier.InsertionPosition, objectSpecifier: NSScriptObjectSpecifier)](nspositionalspecifier/init(position:objectspecifier:).md)
  Initializes a positional specifier with a given position relative to another given specifier.
### Accessing information about a positional specifier
- [var insertionContainer: Any?](nspositionalspecifier/insertioncontainer.md)
  Returns the container in which the new or copied object or objects should be placed.
- [var insertionIndex: Int](nspositionalspecifier/insertionindex.md)
  Returns an insertion index that indicates where the new or copied object or objects should be placed.
- [var insertionKey: String?](nspositionalspecifier/insertionkey.md)
  Returns the key that identifies the relationship into which the new or copied object or objects should be inserted.
- [var insertionReplaces: Bool](nspositionalspecifier/insertionreplaces.md)
  Returns a Boolean value that indicates whether evaluation has been successful and the object to be inserted should actually replace the keyed, indexed object in the insertion container.
- [var objectSpecifier: NSScriptObjectSpecifier](nspositionalspecifier/objectspecifier.md)
  Returns the object specifier specified at initialization time.
- [var position: NSPositionalSpecifier.InsertionPosition](nspositionalspecifier/position.md)
  Returns the insertion position specified at initialization time.
- [func setInsertionClassDescription(NSScriptClassDescription)](nspositionalspecifier/setinsertionclassdescription(_:).md)
  Sets the class description for the object or objects to be inserted.
### Evaluating a positional specifier
- [func evaluate()](nspositionalspecifier/evaluate.md)
  Causes the receiver to evaluate its position.
### Constants
- [NSPositionalSpecifier.InsertionPosition](nspositionalspecifier/insertionposition.md)
  The following constants are defined by `NSPositionalSpecifier` to specify an insertion position.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSScriptObjectSpecifier](nsscriptobjectspecifier.md)
  An abstract class used to represent natural language expressions.
- [class NSPropertySpecifier](nspropertyspecifier.md)
  A specifier for a simple attribute value, a one-to-one relationship, or all elements of a to-many relationship.
- [class NSRandomSpecifier](nsrandomspecifier.md)
  A specifier for an arbitrary object in a collection or, if not a one-to-many relationship, the sole object.
- [class NSRangeSpecifier](nsrangespecifier.md)
  A specifier for a range of objects in a container.
- [class NSUniqueIDSpecifier](nsuniqueidspecifier.md)
  A specifier for an object in a collection (or container) by unique ID.
- [class NSWhoseSpecifier](nswhosespecifier.md)
  A specifier that indicates every object in a collection matching a condition.
- [class NSNameSpecifier](nsnamespecifier.md)
  A specifier for an object in a collection (or container) by name.
- [class NSMiddleSpecifier](nsmiddlespecifier.md)
  A specifier indicating the middle object in a collection or, if not a one-to-many relationship, the sole object.
- [class NSIndexSpecifier](nsindexspecifier.md)
  A specifier representing an object in a collection (or container) with an index number.
- [class NSRelativeSpecifier](nsrelativespecifier.md)
  A specifier that indicates an object in a collection by its position relative to another object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspositionalspecifier)*