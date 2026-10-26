# code

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The code that indicates whether you successfully handled the intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var code: INCancelWorkoutIntentResponseCode { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) INCancelWorkoutIntentResponseCode code;
```

*macOS*

```objc
@property (atomic, readonly) INCancelWorkoutIntentResponseCode code;
```

#### Discussion

This property’s value is set automatically at initialization time and can’t be changed later.

## See Also

### Getting the Response Code
- [enum INCancelWorkoutIntentResponseCode](../incancelworkoutintentresponsecode.md)
  Constants that indicate the response state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incancelworkoutintentresponse/code)*