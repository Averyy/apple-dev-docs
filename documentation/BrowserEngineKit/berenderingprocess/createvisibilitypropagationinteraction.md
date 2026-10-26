# createVisibilityPropagationInteraction

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Returns an interaction that associates a view with the rendering process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```objc
- (id<UIInteraction>) createVisibilityPropagationInteraction;
```

#### Return Value

An interaction that you attach to the view for which your rendering process prepares content.

#### Discussion

When you add a visibility propagation interaction to a view, the system considers the extension process visible whenever the view is visible, and schedules the process as if it has visible UI. When the view isn’t visible, the system schedules the process as a background helper. If your rendering extension prepares content for multiple views, create a separate visibility propagation for each view.

## See Also

### Coordinating processes
- [- grantCapability:error:](./grantcapability_error_.md)
  Grants the specified capability to the process.
- [- grantCapability:error:invalidationHandler:](./grantcapability_error_invalidationhandler_.md)
  Grants the specified capability to the process, invoking the handler when the capability becomes invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/berenderingprocess/createvisibilitypropagationinteraction)*