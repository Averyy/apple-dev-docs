# isEqual(to:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the specified parameter object represents the same property as the current parameter object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func isEqual(to parameter: INParameter) -> Bool
```

```objc
- (BOOL) isEqualToParameter:(INParameter *) parameter;
```

## Return Value

[`true`](../../Swift/true.md) if the two parameter objects represent the same property of the interaction object, or [`false`](../../Swift/false.md) if they do not.

## Parameters

- `parameter`: The parameter object to compare to this one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inparameter/isequal(to:))*