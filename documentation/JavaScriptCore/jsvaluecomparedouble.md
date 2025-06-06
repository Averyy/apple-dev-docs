# JSValueCompareDouble(_:_:_:_:)

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
func JSValueCompareDouble(_ ctx: JSContextRef, _ left: JSValueRef, _ right: Double, _ exception: UnsafeMutablePointer<JSValueRef?>?) -> JSRelationCondition
```

#### Discussion

```None
@function
@abstract         Compares a JSValue with a double.
@param ctx        The execution context to use.
@param left       The JSValue as the left operand.
@param right      The double as the right operand.
@param exception  A pointer to a JSValueRef in which to store an exception, if any. To reliable detect exception, initialize this to null before the call. Pass NULL if you do not care to store an exception.
@result           A value of JSRelationCondition, a kJSRelationConditionUndefined is returned if an exception is thrown.
@discussion       `left` is converted to a double according to the rules specified by the JavaScript language then compared with `right`.
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvaluecomparedouble(_:_:_:_:))*