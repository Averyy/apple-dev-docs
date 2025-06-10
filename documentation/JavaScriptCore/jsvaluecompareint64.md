# JSValueCompareInt64(_:_:_:_:)

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
func JSValueCompareInt64(_ ctx: JSContextRef, _ left: JSValueRef, _ right: Int64, _ exception: UnsafeMutablePointer<JSValueRef?>?) -> JSRelationCondition
```

#### Return Value

A value of JSRelationCondition, a kJSRelationConditionUndefined is returned if an exception is thrown.

#### Discussion

`left` is converted to an integer according to the rules specified by the JavaScript language then compared with `right`.

## Parameters

- `ctx`: The execution context to use.
- `left`: The JSValue as the left operand.
- `right`: The int64_t as the right operand.
- `exception`: A pointer to a JSValueRef in which to store an exception, if any. To reliable detect exception, initialize this to null before the call. Pass NULL if you do not care to store an exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvaluecompareint64(_:_:_:_:))*