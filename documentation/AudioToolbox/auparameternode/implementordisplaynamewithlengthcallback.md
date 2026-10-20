# implementorDisplayNameWithLengthCallback

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

The callback for obtaining an abbreviated version of a parameter node display name.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var implementorDisplayNameWithLengthCallback: AUImplementorDisplayNameWithLengthCallback { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, copy) AUImplementorDisplayNameWithLengthCallback implementorDisplayNameWithLengthCallback;
```

*macOS*

```objc
@property (atomic, copy) AUImplementorDisplayNameWithLengthCallback implementorDisplayNameWithLengthCallback;
```

## See Also

### Audio Unit Implementations
- [var implementorValueObserver: AUImplementorValueObserver](./implementorvalueobserver.md)
  The callback for parameter value changes.
- [var implementorValueProvider: AUImplementorValueProvider](./implementorvalueprovider.md)
  The callback for refreshing known stale values in a parameter tree.
- [var implementorStringFromValueCallback: AUImplementorStringFromValueCallback](./implementorstringfromvaluecallback.md)
  The callback for providing a string representation of a parameter value.
- [var implementorValueFromStringCallback: AUImplementorValueFromStringCallback](./implementorvaluefromstringcallback.md)
  The callback for converting a string to a parameter value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparameternode/implementordisplaynamewithlengthcallback)*