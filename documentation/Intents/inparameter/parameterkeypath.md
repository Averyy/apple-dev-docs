# parameterKeyPath

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The key path to a property of an interaction object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var parameterKeyPath: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * parameterKeyPath;
```

## Discussion

This string defines the location of a property in an [`INInteraction`](../ininteraction.md) object. For example, in the pickup location of a ride request intent, the key path would be represented by the string `pickupLocation`.

## See Also

### Getting the Parameter Details
- [var parameterClass: AnyClass](./parameterclass.md)
  The type of object represented by this parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inparameter/parameterkeypath)*