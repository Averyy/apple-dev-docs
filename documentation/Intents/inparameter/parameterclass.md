# parameterClass

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The type of object represented by this parameter.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var parameterClass: AnyClass { get }
```

```objc
@property (nonatomic, readonly) Class parameterClass;
```

## Discussion

When fetching the parameter’s value, you can use the class information in this property to obtain the type information for that value.

## See Also

### Getting the Parameter Details
- [var parameterKeyPath: String](./parameterkeypath.md)
  The key path to a property of an interaction object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inparameter/parameterclass)*