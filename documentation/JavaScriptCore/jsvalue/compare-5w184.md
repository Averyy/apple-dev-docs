# compare(_:)

**Framework**: JavaScriptCore  
**Kind**: method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 9.0+
- visionOS 2.0+

## Declaration

```swift
func compare(_ other: JSValue) -> JSRelationCondition
```

#### Return Value

A value of JSRelationCondition, a kJSRelationConditionUndefined is returned if an exception is thrown.

#### Discussion

The result is computed by comparing the results of JavaScript’s ==, <, and > operators. If either self or other is (or would coerce to) NaN in JavaScript, then the result is kJSRelationConditionUndefined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/compare(_:)-5w184)*