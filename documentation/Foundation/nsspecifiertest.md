# NSSpecifierTest

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A comparison between an object specifier and a test object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSSpecifierTest
```

```objc
@interface NSSpecifierTest : NSScriptWhoseTest
```

## Overview

Instances of this class represent a Boolean expression; they evaluate an object specifier and compare the resulting object to another object using a given comparison method. For more information on `NSSpecifierTest`, see the method description for its sole public method, its initializer, [`init(objectSpecifier:comparisonOperator:test:)`](./nsspecifiertest/init%28objectspecifier,comparisonoperator,test%29.md).

When an `NSSpecifierTest` object is properly initialized, it holds two objects:

- A “value” or “test” object used as the basis of the comparison; this object can be a regular object or object specifier (such as “blue” in “words whose color is blue”).
- An object specifier evaluating to the container (“words”).

The instance also encapsulates a selector identifying the method performing this comparison. The informal protocol [NSComparisonMethods](./nscomparisonmethods.md) defines a set of comparison methods useful for this purpose, while [NSScriptingComparisonMethods](../ObjectiveC/nsscriptingcomparisonmethods.md) describes additional methods you may need to use for scripting.

The test object is compared, using the selector, against each object in the container. Specifiers in these tests usually have [`containerIsObjectBeingTested`](./nsscriptobjectspecifier/containerisobjectbeingtested.md) invoked on their topmost container.

You should rarely need to subclass `NSSpecifierTest`.

## Topics

### Initializing a specifier test
- [init(objectSpecifier: NSScriptObjectSpecifier?, comparisonOperator: NSSpecifierTest.TestComparisonOperation, test: Any?)](./nsspecifiertest/init%28objectspecifier,comparisonoperator,test%29.md)
  Returns a specifier test initialized to evaluate a test object against an object specified by an object specifier using a given comparison operation.
### Constants
- [NSSpecifierTest.TestComparisonOperation](./nsspecifiertest/testcomparisonoperation.md)
  These are passed to  [`init(objectSpecifier:comparisonOperator:test:)`](./nsspecifiertest/init%28objectspecifier,comparisonoperator,test%29.md) to specify the comparison operator.
### Initializers
- [init?(coder: NSCoder)](./nsspecifiertest/init%28coder%29.md)
- [init(objectSpecifier: NSScriptObjectSpecifier?, comparisonOperator: NSSpecifierTest.TestComparisonOperation, testObject: Any?)](./nsspecifiertest/init%28objectspecifier,comparisonoperator,testobject%29.md)

## Relationships

### Inherits From
- [NSScriptWhoseTest](./nsscriptwhosetest.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Object Matching Tests
- [class NSScriptWhoseTest](./nsscriptwhosetest.md)
  An abstract class that provides the basis for testing specifiers one at a time or in groups.
- [class NSLogicalTest](./nslogicaltest.md)
  The logical combination of one or more specifier tests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsspecifiertest)*