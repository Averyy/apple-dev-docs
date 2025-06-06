# implementorValueProvider

**Framework**: Audio Toolbox  
**Kind**: property

The callback for refreshing known stale values in a parameter tree.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var implementorValueProvider: AUImplementorValueProvider { get set }
```

#### Discussion

The audio unit should return the current value for this parameter; the parameter node object then stores this value.

## See Also

- [var implementorValueObserver: AUImplementorValueObserver](auparameternode/implementorvalueobserver.md)
  The callback for parameter value changes.
- [var implementorStringFromValueCallback: AUImplementorStringFromValueCallback](auparameternode/implementorstringfromvaluecallback.md)
  The callback for providing a string representation of a parameter value.
- [var implementorValueFromStringCallback: AUImplementorValueFromStringCallback](auparameternode/implementorvaluefromstringcallback.md)
  The callback for converting a string to a parameter value.
- [var implementorDisplayNameWithLengthCallback: AUImplementorDisplayNameWithLengthCallback](auparameternode/implementordisplaynamewithlengthcallback.md)
  The callback for obtaining an abbreviated version of a parameter node display name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparameternode/implementorvalueprovider)*