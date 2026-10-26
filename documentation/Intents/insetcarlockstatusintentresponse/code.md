# code

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The code indicating success or failure when confirming or handling an intent.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var code: INSetCarLockStatusIntentResponseCode { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) INSetCarLockStatusIntentResponseCode code;
```

*macOS*

```objc
@property (atomic, readonly) INSetCarLockStatusIntentResponseCode code;
```

#### Discussion

The value of this property is set automatically at initialization time and can’t be changed later.

## See Also

### Getting the Response Code
- [enum INSetCarLockStatusIntentResponseCode](../insetcarlockstatusintentresponsecode.md)
  Constants indicating the status of the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetcarlockstatusintentresponse/code)*