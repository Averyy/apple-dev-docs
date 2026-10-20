# removeParameterObserver(_:)

**Framework**: Audio Toolbox  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) removeParameterObserver:(AUParameterObserverToken) token;
```

#### Discussion

This call will remove the callback corresponding to the given token. This operation blocks until any callbacks currently in progress have completed.

## Parameters

- `token`: The token corresponding to the given observer.

## See Also

### Observers
- [func token(byAddingParameterObserver: AUParameterObserver) -> AUParameterObserverToken](./token%28byaddingparameterobserver%29.md)
  Adds an observer for a single parameter or all parameters in a group.
- [func token(byAddingParameterRecordingObserver: AUParameterRecordingObserver) -> AUParameterObserverToken](./token%28byaddingparameterrecordingobserver%29.md)
  Adds a recording observer for a single parameter or all parameters in a group.
- [func token(byAddingParameterAutomationObserver: AUParameterAutomationObserver) -> AUParameterObserverToken](./token%28byaddingparameterautomationobserver%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparameternode/removeparameterobserver(_:))*