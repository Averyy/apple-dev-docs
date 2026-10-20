# lastEventTimestamp

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The time of the most recent change to an element’s value.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var lastEventTimestamp: TimeInterval { get }
```

```objc
@property (atomic, readonly) NSTimeInterval lastEventTimestamp;
```

## See Also

### Getting change information
- [var valueDidChangeHandler: ((GCPhysicalInputProfile, GCControllerElement) -> Void)?](./valuedidchangehandler.md)
  The block that the profile calls when an element’s value changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcphysicalinputprofile/lasteventtimestamp)*