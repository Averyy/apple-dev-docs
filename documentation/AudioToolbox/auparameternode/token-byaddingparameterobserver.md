# token(byAddingParameterObserver:)

**Framework**: Audio Toolbox  
**Kind**: method

Adds an observer for a single parameter or all parameters in a group.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func token(byAddingParameterObserver observer: @escaping AUParameterObserver) -> AUParameterObserverToken
```

#### Return Value

A token which can be passed to the [`removeParameterObserver(_:)`](auparameternode/removeparameterobserver(_:).md) or [`setValue(_:originator:)`](auparameter/setvalue(_:originator:).md) methods.

#### Discussion

An audio unit view can use an observer to be notified of changes to a single parameter or all parameters in a group. These callbacks are throttled so as to limit the rate of redundant notifications in the case of frequent changes to a single parameter.

This block is called in an arbitrary thread context and it is responsible for thread-safety. It must not make any calls to add or remove other observers, including itself, as this will deadlock.

An audio unit should interact with the parameter node via the [`implementorValueObserver`](auparameternode/implementorvalueobserver.md) and [`implementorValueProvider`](auparameternode/implementorvalueprovider.md) properties.

## Parameters

- `observer`: A block called after the value of a parameter has changed.

## See Also

- [func token(byAddingParameterRecordingObserver: AUParameterRecordingObserver) -> AUParameterObserverToken](auparameternode/token(byaddingparameterrecordingobserver:).md)
  Adds a recording observer for a single parameter or all parameters in a group.
- [func token(byAddingParameterAutomationObserver: AUParameterAutomationObserver) -> AUParameterObserverToken](auparameternode/token(byaddingparameterautomationobserver:).md)
- [func removeParameterObserver(AUParameterObserverToken)](auparameternode/removeparameterobserver(_:).md)
  Remove a specific parameter observer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparameternode/token(byaddingparameterobserver:))*