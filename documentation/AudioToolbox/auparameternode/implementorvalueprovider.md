# implementorValueProvider

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

The callback for refreshing known stale values in a parameter tree.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var implementorValueProvider: AUImplementorValueProvider { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, copy) AUImplementorValueProvider implementorValueProvider;
```

*macOS*

```objc
@property (atomic, copy) AUImplementorValueProvider implementorValueProvider;
```

#### Discussion

The audio unit should return the current value for this parameter; the parameter node object then stores this value.

## See Also

### Audio Unit Implementations
- [var implementorValueObserver: AUImplementorValueObserver](./implementorvalueobserver.md)
  The callback for parameter value changes.
- [var implementorStringFromValueCallback: AUImplementorStringFromValueCallback](./implementorstringfromvaluecallback.md)
  The callback for providing a string representation of a parameter value.
- [var implementorValueFromStringCallback: AUImplementorValueFromStringCallback](./implementorvaluefromstringcallback.md)
  The callback for converting a string to a parameter value.
- [var implementorDisplayNameWithLengthCallback: AUImplementorDisplayNameWithLengthCallback](./implementordisplaynamewithlengthcallback.md)
  The callback for obtaining an abbreviated version of a parameter node display name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparameternode/implementorvalueprovider)*