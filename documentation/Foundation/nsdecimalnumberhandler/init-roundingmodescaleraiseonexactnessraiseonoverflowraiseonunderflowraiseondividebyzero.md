# init(roundingMode:scale:raiseOnExactness:raiseOnOverflow:raiseOnUnderflow:raiseOnDivideByZero:)

**Framework**: Foundation  
**Kind**: init

Returns an `NSDecimalNumberHandler` object initialized so it behaves as specified by the method’s arguments.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(roundingMode: NSDecimalNumber.RoundingMode, scale: Int16, raiseOnExactness exact: Bool, raiseOnOverflow overflow: Bool, raiseOnUnderflow underflow: Bool, raiseOnDivideByZero divideByZero: Bool)
```

#### Return Value

An initialized `NSDecimalNumberHandler` object initialized with customized behavior. The returned object might be different than the original receiver.

#### Discussion

See the [`NSDecimalNumberBehaviors`](nsdecimalnumberbehaviors.md) protocol specification for a complete explanation of the possible behaviors.

## Parameters

- `roundingMode`: The rounding mode to use. There are four possible values:  ,  ,  , and  .
- `scale`: The number of digits a rounded value should have after its decimal point.
- `exact`: If  , in the event of an exactness error the handler will raise an exception, otherwise it will ignore the error and return control to the calling method.
- `overflow`: If  , in the event of an overflow error the handler will raise an exception, otherwise it will ignore the error and return control to the calling method
- `underflow`: If  , in the event of an underflow error the handler will raise an exception, otherwise it will ignore the error and return control to the calling method
- `divideByZero`: If  , in the event of a divide by zero error the handler will raise an exception, otherwise it will ignore the error and return control to the calling method


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumberhandler/init(roundingmode:scale:raiseonexactness:raiseonoverflow:raiseonunderflow:raiseondividebyzero:))*