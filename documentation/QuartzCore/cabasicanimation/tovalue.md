# toValue

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

Defines the value the receiver uses to end interpolation.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var toValue: Any? { get set }
```

```objc
@property (strong, nullable) id toValue;
```

## Discussion

See [Setting Interpolation Values](../cabasicanimation.md#Setting-Interpolation-Values) for details on how `toValue` interacts with the other interpolation values.

## See Also

### Interpolation values
- [var fromValue: Any?](./fromvalue.md)
  Defines the value the receiver uses to start interpolation.
- [var byValue: Any?](./byvalue.md)
  Defines the value the receiver uses to perform relative interpolation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cabasicanimation/tovalue)*