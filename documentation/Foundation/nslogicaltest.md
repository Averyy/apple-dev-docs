# NSLogicalTest

**Framework**: Foundation  
**Kind**: class

The logical combination of one or more specifier tests.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSLogicalTest
```

#### Overview

Instances of this class perform logical operations of `AND`, `OR`, and `NOT` on Boolean expressions represented by [`NSSpecifierTest`](nsspecifiertest.md) objects. These operators are equivalent to “`&&`”, “`||`”, and “`!`” in the C language.

For `AND` and `OR` operations, an `NSLogicalTest` object is typically initialized with an array containing two or more [`NSSpecifierTest`](nsspecifiertest.md) objects. [`isTrue()`](nsscriptwhosetest/istrue().md)—inherited from [`NSScriptWhoseTest`](nsscriptwhosetest.md)—evaluates the array in a manner appropriate to the logical operation. For `NOT` operations, an `NSLogicalTest` object is initialized with only one `NSSpecifierTest` object; it simply reverses the Boolean outcome of the [`isTrue()`](nsscriptwhosetest/istrue().md) method.

You don’t normally subclass `NSLogicalTest`.

## Topics

### Initializing a logical test
- [init(andTestWith: [NSSpecifierTest])](nslogicaltest/init(andtestwith:).md)
  Returns an `NSLogicalTest` object initialized to perform an `AND` operation with the `NSSpecifierTest` objects in a given array.
- [init(notTestWith: NSScriptWhoseTest)](nslogicaltest/init(nottestwith:).md)
  Returns an `NSLogicalTest` object initialized to perform a `NOT` operation on the given `NSScriptWhoseTest` object.
- [init(orTestWith: [NSSpecifierTest])](nslogicaltest/init(ortestwith:).md)
  Returns an `NSLogicalTest` object initialized to perform an `OR` operation with the `NSSpecifierTest` objects in a given array.

## Relationships

### Inherits From
- [NSScriptWhoseTest](nsscriptwhosetest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSScriptWhoseTest](nsscriptwhosetest.md)
  An abstract class that provides the basis for testing specifiers one at a time or in groups.
- [class NSSpecifierTest](nsspecifiertest.md)
  A comparison between an object specifier and a test object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslogicaltest)*