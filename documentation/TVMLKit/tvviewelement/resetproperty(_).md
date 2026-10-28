# resetProperty(_:)

**Framework**: TVMLKit  
**Kind**: method  
**Role**: Instance Method

Resets the property to its default value.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
func resetProperty(_ resettableProperty: TVElementResettableProperty)
```

```objc
- (void) resetProperty:(TVElementResettableProperty) resettableProperty;
```

## Discussion

This method can be used to reset a resettable property to its default value after changes to the property have been read.

## Parameters

- `resettableProperty`: A property that can be reset to its default value. For possible values, see [`TVElementResettableProperty`](../tvelementresettableproperty.md).

## See Also

### Resetting a Property’s Value
- [enum TVElementResettableProperty](../tvelementresettableproperty.md)
  The types of properties that can be reset to their default values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvviewelement/resetproperty(_:))*