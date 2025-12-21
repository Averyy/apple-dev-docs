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
func compare(_ other: UInt64) -> JSRelationCondition
```

#### Return Value

A value of JSRelationCondition, a kJSRelationConditionUndefined is returned if an exception is thrown.

#### Discussion

Compare a JSValue with a uint64_t.

The JSValue is converted to an integer according to the rules specified by the JavaScript language then compared with other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/compare(_:)-64n3k)*