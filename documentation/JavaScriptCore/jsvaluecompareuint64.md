# JSValueCompareUInt64(_:_:_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 9.0+
- visionOS 2.0+

## Declaration

```swift
func JSValueCompareUInt64(_ ctx: JSContextRef, _ left: JSValueRef, _ right: UInt64, _ exception: UnsafeMutablePointer<JSValueRef?>?) -> JSRelationCondition
```

#### Discussion

```None
@function
@abstract         Compares a JSValue with an unsigned 64-bit integer.
@param ctx        The execution context to use.
@param left       The JSValue as the left operand.
@param right      The uint64_t as the right operand.
@param exception  A pointer to a JSValueRef in which to store an exception, if any. To reliable detect exception, initialize this to null before the call. Pass NULL if you do not care to store an exception.
@result           A value of JSRelationCondition, a kJSRelationConditionUndefined is returned if an exception is thrown.
@discussion       `left` is converted to an integer according to the rules specified by the JavaScript language then compared with `right`.
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvaluecompareuint64(_:_:_:_:))*