# toUInt64()

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
func toUInt64() -> UInt64
```

#### Discussion

Convert a JSValue to a uint64_t.

The JSValue is converted to an integer according to the rules specified by the JavaScript language. If the value is a BigInt, then the value is truncated to a uint64_t.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/touint64())*