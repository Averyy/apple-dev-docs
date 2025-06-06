# allParameterValues

**Framework**: Audio Toolbox  
**Kind**: property

Special read-only property for KVO.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var allParameterValues: Bool { get }
```

#### Discussion

KVO notifications are issued on this property in response to certain events where potentially all parameter values are invalidated—for example, the selection of a preset.

## See Also

- [var fullState: [String : Any]?](auaudiounit/fullstate.md)
  A persistable snapshot of the audio unit’s properties and parameters, suitable for saving as a user preset.
- [var parameterTree: AUParameterTree?](auaudiounit/parametertree.md)
  An audio unit’s parameters, organized in a tree hierarchy.
- [func parametersForOverview(withCount: Int) -> [NSNumber]](auaudiounit/parametersforoverview(withcount:).md)
  Returns the audio unit’s most important parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/allparametervalues)*