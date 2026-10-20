# fromValue

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

Defines the value the receiver uses to start interpolation.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var fromValue: Any? { get set }
```

```objc
@property (strong, nullable) id fromValue;
```

#### Discussion

See [Setting Interpolation Values](../cabasicanimation.md#Setting-Interpolation-Values) for details on how `fromValue` interacts with the other interpolation values.

## See Also

### Related Documentation
- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)
### Interpolation values
- [var toValue: Any?](./tovalue.md)
  Defines the value the receiver uses to end interpolation.
- [var byValue: Any?](./byvalue.md)
  Defines the value the receiver uses to perform relative interpolation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cabasicanimation/fromvalue)*