# eraSymbols

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The era symbols for the receiver.

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
var eraSymbols: [String]! { get set }
```

```objc
@property (copy, null_resettable) NSArray<NSString *> * eraSymbols;
```

#### Discussion

An array containing `NSString` objects representing the era symbols for the receiver (for example, {“B.C.E.”, “C.E.”}).

## See Also

### Managing Era Symbols
- [var longEraSymbols: [String]!](./longerasymbols.md)
  The long era symbols for the receiver


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateformatter/erasymbols)*