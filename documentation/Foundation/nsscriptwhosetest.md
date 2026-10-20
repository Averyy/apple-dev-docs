# NSScriptWhoseTest

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

An abstract class that provides the basis for testing specifiers one at a time or in groups.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSScriptWhoseTest
```

```objc
@interface NSScriptWhoseTest : NSObject
```

#### Overview

`NSScriptWhoseTest` is an abstract class whose sole method is [`isTrue()`](./nsscriptwhosetest/istrue%28%29.md). Two concrete subclasses of `NSScriptWhoseTest` generate objects representing Boolean expressions comparing one object with another and objects representing multiple Boolean expressions connected by logical operators (`OR`, `AND`, `NOT`). These classes are, respectively, [`NSSpecifierTest`](./nsspecifiertest.md) and [`NSLogicalTest`](./nslogicaltest.md). In evaluating itself, an [`NSWhoseSpecifier`](./nswhosespecifier.md) invokes the [`isTrue()`](./nsscriptwhosetest/istrue%28%29.md) method of its “test” object.

You shouldn’t need to subclass `NSScriptWhoseTest`, and you should rarely need to subclass one of its subclasses.

## Topics

### Evaluating a test
- [func isTrue() -> Bool](./nsscriptwhosetest/istrue%28%29.md)
  Returns a Boolean value that indicates whether the test represented by the receiver evaluates to true.
### Initializers
- [init()](./nsscriptwhosetest/init%28%29.md)
- [init?(coder: NSCoder)](./nsscriptwhosetest/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [NSLogicalTest](./nslogicaltest.md)
- [NSSpecifierTest](./nsspecifiertest.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Object Matching Tests
- [class NSSpecifierTest](./nsspecifiertest.md)
  A comparison between an object specifier and a test object.
- [class NSLogicalTest](./nslogicaltest.md)
  The logical combination of one or more specifier tests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptwhosetest)*