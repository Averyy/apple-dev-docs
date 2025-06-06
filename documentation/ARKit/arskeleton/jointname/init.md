# init(_:)

**Framework**: ARKit  
**Kind**: init

Returns a joint name that corresponds to a key point defined in a human body pose.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
init?(_ recognizedPointKey: VNRecognizedPointKey)
```

#### Discussion

This function matches human body key points defined by the Vision framework with joint names defined by ARKit. This function may return `nil` if the key point doesn’t map to a joint name. For more information about key points, see [`Detecting Human Body Poses in Images`](https://developer.apple.com/documentation/Vision/detecting-human-body-poses-in-images).

## Parameters

- `recognizedPointKey`: The argument key point.

## See Also

- [init(rawValue: String)](arskeleton/jointname/init(rawvalue:).md)
  Creates a new joint name.
- [struct VNRecognizedPointKey](../Vision/VNRecognizedPointKey.md)
  The data type for all recognized point keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeleton/jointname/init(_:))*