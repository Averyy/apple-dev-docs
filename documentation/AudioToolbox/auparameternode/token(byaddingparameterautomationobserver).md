# token(byAddingParameterAutomationObserver:)

**Framework**: Audio Toolbox  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (AUParameterObserverToken) tokenByAddingParameterAutomationObserver:(AUParameterAutomationObserver) observer;
```

## See Also

### Observers
- [func token(byAddingParameterObserver: AUParameterObserver) -> AUParameterObserverToken](./token%28byaddingparameterobserver%29.md)
  Adds an observer for a single parameter or all parameters in a group.
- [func token(byAddingParameterRecordingObserver: AUParameterRecordingObserver) -> AUParameterObserverToken](./token%28byaddingparameterrecordingobserver%29.md)
  Adds a recording observer for a single parameter or all parameters in a group.
- [func removeParameterObserver(AUParameterObserverToken)](./removeparameterobserver%28_%29.md)
  Remove a specific parameter observer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparameternode/token(byaddingparameterautomationobserver:))*