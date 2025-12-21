# JSValueIsBigInt(_:_:)

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
func JSValueIsBigInt(_ ctx: JSContextRef, _ value: JSValueRef) -> Bool
```

#### Return Value

True if value’s type is the BigInt type, otherwise false.

#### Discussion

Tests whether a JavaScript value’s type is the BigInt type.

## Parameters

- `ctx`: The execution context to use.
- `value`: The JSValue to test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvalueisbigint(_:_:))*