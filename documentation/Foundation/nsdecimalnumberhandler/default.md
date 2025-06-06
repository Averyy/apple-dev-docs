# default

**Framework**: Foundation  
**Kind**: property

Returns the default instance of `NSDecimalNumberHandler`.

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
class var `default`: NSDecimalNumberHandler { get }
```

#### Return Value

The default instance of `NSDecimalNumberHandler`.

#### Discussion

This default decimal number handler rounds to the closest possible return value. It assumes your need for precision does not exceed 38 significant digits, and it raises an exception when its `NSDecimalNumber` object tries to divide by `0` or when its `NSDecimalNumber` object produces a number too big or too small to be represented.

## See Also

- [Number and Value Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/NumbersandValues.html#//apple_ref/doc/uid/10000038i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumberhandler/default)*