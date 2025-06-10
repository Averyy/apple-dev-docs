# toInt64()

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
func toInt64() -> Int64
```

#### Discussion

The JSValue is converted to an integer according to the rules specified by the JavaScript language. If the value is a BigInt, then the value is truncated to an int64_t.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/toint64())*