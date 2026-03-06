# setTo(_:)

**Framework**: Scripting Bridge  
**Kind**: method

Sets the receiver to a specified value.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
func setTo(_ value: Any?)
```

#### Discussion

You should not call this method directly.

## Parameters

- `value`: The data the receiver should be set to. It can be an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString), [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber), [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray), `SBObject`, or any other type of object supported by the Scripting Bridge framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbobject/setto(_:))*