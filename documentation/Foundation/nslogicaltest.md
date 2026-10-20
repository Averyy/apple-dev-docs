# NSLogicalTest

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

The logical combination of one or more specifier tests.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSLogicalTest
```

```objc
@interface NSLogicalTest : NSScriptWhoseTest
```

#### Overview

Instances of this class perform logical operations of `AND`, `OR`, and `NOT` on Boolean expressions represented by [`NSSpecifierTest`](./nsspecifiertest.md) objects. These operators are equivalent to “`&&`”, “`||`”, and “`!`” in the C language.

For `AND` and `OR` operations, an `NSLogicalTest` object is typically initialized with an array containing two or more [`NSSpecifierTest`](./nsspecifiertest.md) objects. [`isTrue()`](./nsscriptwhosetest/istrue%28%29.md)—inherited from [`NSScriptWhoseTest`](./nsscriptwhosetest.md)—evaluates the array in a manner appropriate to the logical operation. For `NOT` operations, an `NSLogicalTest` object is initialized with only one `NSSpecifierTest` object; it simply reverses the Boolean outcome of the [`isTrue()`](./nsscriptwhosetest/istrue%28%29.md) method.

You don’t normally subclass `NSLogicalTest`.

## Topics

### Initializing a logical test
- [init(andTestWith: [NSSpecifierTest])](./nslogicaltest/init%28andtestwith%29.md)
  Returns an `NSLogicalTest` object initialized to perform an `AND` operation with the `NSSpecifierTest` objects in a given array.
- [init(notTestWith: NSScriptWhoseTest)](./nslogicaltest/init%28nottestwith%29.md)
  Returns an `NSLogicalTest` object initialized to perform a `NOT` operation on the given `NSScriptWhoseTest` object.
- [init(orTestWith: [NSSpecifierTest])](./nslogicaltest/init%28ortestwith%29.md)
  Returns an `NSLogicalTest` object initialized to perform an `OR` operation with the `NSSpecifierTest` objects in a given array.
### Initializers
- [init(andTestWithTests: [NSSpecifierTest])](./nslogicaltest/init%28andtestwithtests%29.md)
- [init(notTestWithTest: NSScriptWhoseTest)](./nslogicaltest/init%28nottestwithtest%29.md)
- [init(orTestWithTests: [NSSpecifierTest])](./nslogicaltest/init%28ortestwithtests%29.md)

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
- [class NSSpecifierTest](./nsspecifiertest.md)
  A comparison between an object specifier and a test object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslogicaltest)*