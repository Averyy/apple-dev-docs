# init(_:)

**Framework**: ARKit  
**Kind**: init  
**Role**: Initializer

Returns a joint name that corresponds to a key point defined in a human body pose.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
init?(_ recognizedPointKey: VNRecognizedPointKey)
```

```c
extern ARSkeletonJointNameARSkeletonJointNameForRecognizedPointKey(VNRecognizedPointKey recognizedPointKey);
```

#### Discussion

This function matches human body key points defined by the Vision framework with joint names defined by ARKit. This function may return `nil` if the key point doesn’t map to a joint name. For more information about key points, see [Detecting Human Body Poses in Images](../../../Vision/detecting-human-body-poses-in-images.md).

## Parameters

- `recognizedPointKey`: The argument key point.

## See Also

### Creating a Joint Name
- [init(rawValue: String)](./init%28rawvalue%29.md)
  Creates a new joint name.
- [struct VNRecognizedPointKey](../../../Vision/vnrecognizedpointkey.md)
  The data type for all recognized point keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeleton/jointname/init(_:))*