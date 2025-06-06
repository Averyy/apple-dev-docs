# token(byAddingParameterAutomationObserver:)

**Framework**: Audio Toolbox  
**Kind**: method

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func token(byAddingParameterAutomationObserver observer: @escaping AUParameterAutomationObserver) -> AUParameterObserverToken
```

## See Also

- [func token(byAddingParameterObserver: AUParameterObserver) -> AUParameterObserverToken](auparameternode/token(byaddingparameterobserver:).md)
  Adds an observer for a single parameter or all parameters in a group.
- [func token(byAddingParameterRecordingObserver: AUParameterRecordingObserver) -> AUParameterObserverToken](auparameternode/token(byaddingparameterrecordingobserver:).md)
  Adds a recording observer for a single parameter or all parameters in a group.
- [func removeParameterObserver(AUParameterObserverToken)](auparameternode/removeparameterobserver(_:).md)
  Remove a specific parameter observer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparameternode/token(byaddingparameterautomationobserver:))*