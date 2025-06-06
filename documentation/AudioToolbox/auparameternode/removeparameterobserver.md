# removeParameterObserver(_:)

**Framework**: Audio Toolbox  
**Kind**: method

Remove a specific parameter observer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func removeParameterObserver(_ token: AUParameterObserverToken)
```

#### Discussion

This call will remove the callback corresponding to the given token. This operation blocks until any callbacks currently in progress have completed.

## Parameters

- `token`: The token corresponding to the given observer.

## See Also

- [func token(byAddingParameterObserver: AUParameterObserver) -> AUParameterObserverToken](auparameternode/token(byaddingparameterobserver:).md)
  Adds an observer for a single parameter or all parameters in a group.
- [func token(byAddingParameterRecordingObserver: AUParameterRecordingObserver) -> AUParameterObserverToken](auparameternode/token(byaddingparameterrecordingobserver:).md)
  Adds a recording observer for a single parameter or all parameters in a group.
- [func token(byAddingParameterAutomationObserver: AUParameterAutomationObserver) -> AUParameterObserverToken](auparameternode/token(byaddingparameterautomationobserver:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparameternode/removeparameterobserver(_:))*