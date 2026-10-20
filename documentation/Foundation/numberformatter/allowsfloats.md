# allowsFloats

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Determines whether the receiver allows as input floating-point values (that is, values that include the period character [`.`]).

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
var allowsFloats: Bool { get set }
```

```objc
@property BOOL allowsFloats;
```

#### Discussion

By default, floating point values are allowed.

## See Also

### Managing Input and Output Attributes
- [var minimum: NSNumber?](./minimum.md)
  The lowest number allowed as input by the receiver.
- [var maximum: NSNumber?](./maximum.md)
  The highest number allowed as input by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/allowsfloats)*