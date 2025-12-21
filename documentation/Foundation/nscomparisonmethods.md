# NSComparisonMethods

**Framework**: Foundation

A collection of default comparison methods useful for performing specifier tests.

#### Overview

If you have scriptable objects that need to perform comparisons for scripting purposes, you may need to implement some of the methods declared in NSScriptingComparisonMethods. The default implementation provided for many of these methods by `NSObject` is appropriate for objects that implement a single comparison method whose selector, signature, and description match the following:

```objc
- (NSComparisonResult)compare:(id)object;
```

This method should return `NSOrderedAscending` if the receiver is less than `object`, `NSOrderedDescending` if the receiver is greater than `object`, and `NSOrderedSame` if the receiver and `object` are equal. For example, `NSString` does not implement most of the methods declared in this informal protocol, but `NSString` objects still handle messages conforming to this protocol properly because `NSString` implements a `compare:` method that meets the necessary requirements. Cocoa also includes appropriate `compare:` method implementations for the `NSDate`, `NSDecimalNumber`, and `NSValue` classes.

## Topics

### Performing comparisons
- [func doesContain(Any) -> Bool](../ObjectiveC/NSObject-swift.class/doesContain(_:).md)
  Returns a Boolean value that indicates whether the receiver contains a given object.
- [func isCaseInsensitiveLike(String) -> Bool](../ObjectiveC/NSObject-swift.class/isCaseInsensitiveLike(_:).md)
  Returns a Boolean value that indicates whether receiver is considered to be “like” a given string when the case of characters in the receiver is ignored.
- [func isEqual(to: Any?) -> Bool](../ObjectiveC/NSObject-swift.class/isEqual(to:).md)
  Returns a Boolean value that indicates whether the receiver is equal to another given object.
- [func isGreaterThan(Any?) -> Bool](../ObjectiveC/NSObject-swift.class/isGreaterThan(_:).md)
  Returns a Boolean value that indicates whether the receiver is greater than another given object.
- [func isGreaterThanOrEqual(to: Any?) -> Bool](../ObjectiveC/NSObject-swift.class/isGreaterThanOrEqual(to:).md)
  Returns a Boolean value that indicates whether the receiver is greater than or equal to another given object.
- [func isLessThan(Any?) -> Bool](../ObjectiveC/NSObject-swift.class/isLessThan(_:).md)
  Returns a Boolean value that indicates whether the receiver is less than another given object.
- [func isLessThanOrEqual(to: Any?) -> Bool](../ObjectiveC/NSObject-swift.class/isLessThanOrEqual(to:).md)
  Returns a Boolean value that indicates whether the receiver is less than or equal to another given object.
- [func isLike(String) -> Bool](../ObjectiveC/NSObject-swift.class/isLike(_:).md)
  Returns a Boolean value that indicates whether the receiver is “like” another given object.
- [func isNotEqual(to: Any?) -> Bool](../ObjectiveC/NSObject-swift.class/isNotEqual(to:).md)
  Returns a Boolean value that indicates whether the receiver is not equal to another given object.

## See Also

- [Cocoa Scripting Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
- [NSScriptingComparisonMethods](../ObjectiveC/nsscriptingcomparisonmethods.md)
  A collection of methods useful for comparing script objects.
- [NSScriptKeyValueCoding](../ObjectiveC/nsscriptkeyvaluecoding.md)
  A collection of methods that provide additional capabilities for working with key-value coding.
- [NSScriptObjectSpecifiers](nsscriptobjectspecifiers.md)
  A collection of methods providing additional object specifier functionality.
- [class NSScriptCoercionHandler](nsscriptcoercionhandler.md)
  A mechanism for converting one kind of scripting data to another.
- [class NSScriptExecutionContext](nsscriptexecutioncontext.md)
  The context in which the current script command is executed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscomparisonmethods)*