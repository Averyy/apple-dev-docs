# resume()

**Framework**: Matter  
**Kind**: method

Resume the controller.  This has no effect if the controller is not suspended.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
func resume()
```

#### Discussion

A resume following any number of suspend calls will resume the controller; there does not need to be a resume call to match every suspend call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontroller/resume())*