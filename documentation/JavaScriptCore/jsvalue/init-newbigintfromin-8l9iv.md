# init(newBigIntFrom:in:)

**Framework**: JavaScriptCore  
**Kind**: init

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 9.0+
- visionOS 2.0+

## Declaration

```swift
init?(newBigIntFrom int64: Int64, in context: JSContext)
```

#### Return Value

The JSValue representing a JavaScript value with type BigInt.

## Parameters

- `int64`: The signed 64-bit integer of the BigInt JavaScript value being created.
- `context`: The JSContext to which the resulting JSValue belongs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalue/init(newbigintfrom:in:)-8l9iv)*