# scope

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The audio unit scope for the parameter.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var scope: UInt32 { get set }
```

```objc
@property (readwrite) UInt32 scope;
```

## See Also

### Configuring a parameter event
- [var parameterID: UInt32](./parameterid.md)
  The identifier of the parameter.
- [var element: UInt32](./element.md)
  The element index in the scope.
- [var value: Float](./value.md)
  The value of the parameter to set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avparameterevent/scope)*