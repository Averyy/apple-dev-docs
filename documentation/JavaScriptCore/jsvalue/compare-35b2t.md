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
func compare(_ other: Double) -> JSRelationCondition
```

#### Return Value

A value of JSRelationCondition, a kJSRelationConditionUndefined is returned if an exception is thrown.

#### Discussion

The JSValue is converted to a double according to the rules specified by the JavaScript language then compared with other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/compare(_:)-35b2t)*