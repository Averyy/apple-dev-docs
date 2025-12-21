# NSScriptWhoseTest

**Framework**: Foundation  
**Kind**: class

An abstract class that provides the basis for testing specifiers one at a time or in groups.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSScriptWhoseTest
```

#### Overview

`NSScriptWhoseTest` is an abstract class whose sole method is [`isTrue()`](nsscriptwhosetest/istrue().md). Two concrete subclasses of `NSScriptWhoseTest` generate objects representing Boolean expressions comparing one object with another and objects representing multiple Boolean expressions connected by logical operators (`OR`, `AND`, `NOT`). These classes are, respectively, [`NSSpecifierTest`](nsspecifiertest.md) and [`NSLogicalTest`](nslogicaltest.md). In evaluating itself, an [`NSWhoseSpecifier`](nswhosespecifier.md) invokes the [`isTrue()`](nsscriptwhosetest/istrue().md) method of its “test” object.

You shouldn’t need to subclass `NSScriptWhoseTest`, and you should rarely need to subclass one of its subclasses.

## Topics

### Evaluating a test
- [func isTrue() -> Bool](nsscriptwhosetest/istrue.md)
  Returns a Boolean value that indicates whether the test represented by the receiver evaluates to true.
### Initializers
- [init()](nsscriptwhosetest/init.md)
- [init?(coder: NSCoder)](nsscriptwhosetest/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSLogicalTest](nslogicaltest.md)
- [NSSpecifierTest](nsspecifiertest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSSpecifierTest](nsspecifiertest.md)
  A comparison between an object specifier and a test object.
- [class NSLogicalTest](nslogicaltest.md)
  The logical combination of one or more specifier tests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptwhosetest)*