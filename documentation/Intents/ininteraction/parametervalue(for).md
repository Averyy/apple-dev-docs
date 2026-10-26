# parameterValue(for:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Returns the value of the specified parameter of this interaction object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func parameterValue(for parameter: INParameter) -> Any?
```

```objc
- (id) parameterValueForParameter:(INParameter *) parameter;
```

#### Return Value

The value associated with the property at the specified key path.

#### Discussion

Use this method to fetch the value of a property that was specified using an [`INParameter`](../inparameter.md) object. A parameter object contains a key path that identifies the location of the property inside this interaction object.

## Parameters

- `parameter`: The [`INParameter`](../inparameter.md) object that specifies the key path to a property of this interaction object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ininteraction/parametervalue(for:))*