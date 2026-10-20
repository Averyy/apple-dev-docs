# implementorValueObserver

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

The callback for parameter value changes.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var implementorValueObserver: AUImplementorValueObserver { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, copy) AUImplementorValueObserver implementorValueObserver;
```

*macOS*

```objc
@property (atomic, copy) AUImplementorValueObserver implementorValueObserver;
```

#### Discussion

This block receives all externally-generated changes to parameter values. It should store the new value in its audio signal processing state (assuming that state is separate from the parameter object).

## See Also

### Audio Unit Implementations
- [var implementorValueProvider: AUImplementorValueProvider](./implementorvalueprovider.md)
  The callback for refreshing known stale values in a parameter tree.
- [var implementorStringFromValueCallback: AUImplementorStringFromValueCallback](./implementorstringfromvaluecallback.md)
  The callback for providing a string representation of a parameter value.
- [var implementorValueFromStringCallback: AUImplementorValueFromStringCallback](./implementorvaluefromstringcallback.md)
  The callback for converting a string to a parameter value.
- [var implementorDisplayNameWithLengthCallback: AUImplementorDisplayNameWithLengthCallback](./implementordisplaynamewithlengthcallback.md)
  The callback for obtaining an abbreviated version of a parameter node display name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparameternode/implementorvalueobserver)*