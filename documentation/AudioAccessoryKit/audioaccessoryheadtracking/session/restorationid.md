# restorationID

**Framework**: AudioAccessoryKit  
**Kind**: property

A stable identifier the system uses to bring this extension out of suspension when sensor traffic arrives for this accessory.

**Availability**:
- iOS 27.0+ (Beta)

## Declaration

```swift
final let restorationID: String?
```

#### Discussion

`nil` if the host could not provide a restoration identifier for the underlying accessory transport.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/audioaccessoryheadtracking/session/restorationid)*