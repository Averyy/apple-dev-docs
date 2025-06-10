# firstFoundOnly

**Framework**: SceneKit  
**Kind**: property

An option to return only the first object found.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static let firstFoundOnly: SCNHitTestOption
```

#### Discussion

The value for this key is a [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing a Boolean value. The default value is [`false`](https://developer.apple.com/documentation/swift/false), specifying that hit-testing should return all objects found. If you specify [`true`](https://developer.apple.com/documentation/swift/true), the array of hit-test results contains only the first object found (which is not necessarily the nearest).

## See Also

- [static let sortResults: SCNHitTestOption](scnhittestoption/sortresults.md)
  An option to sort the results of a hit-test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnhittestoption/firstfoundonly)*