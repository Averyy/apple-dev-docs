# firstFoundOnly

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

An option to return only the first object found.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

> **Deprecated**: Use the [`searchMode`](./searchmode.md) option with value [`SCNHitTestSearchMode.any`](../scnhittestsearchmode/any.md) instead.

## Declaration

```swift
static let firstFoundOnly: SCNHitTestOption
```

```c
extern SCNHitTestOption const SCNHitTestFirstFoundOnlyKey;
```

## Discussion

The value for this key is a [`NSNumber`](../../Foundation/nsnumber.md) object containing a Boolean value. The default value is [`false`](../../Swift/false.md), specifying that hit-testing should return all objects found. If you specify [`true`](../../Swift/true.md), the array of hit-test results contains only the first object found (which is not necessarily the nearest).

## See Also

### Deprecated
- [static let sortResults: SCNHitTestOption](./sortresults.md)
  An option to sort the results of a hit-test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnhittestoption/firstfoundonly)*