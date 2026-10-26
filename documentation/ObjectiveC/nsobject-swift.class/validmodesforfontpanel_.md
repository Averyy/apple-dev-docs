# validModesForFontPanel:

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Returns the mode mask corresponding to the expected font panel mode.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

## Declaration

```objc
- (NSFontPanelModeMask) validModesForFontPanel:(NSFontPanel *) fontPanel;
```

#### Discussion

The mode masks are defined in [Mode Masks](../../AppKit/mode-masks.md).

The Font Panel has the ability to hide elements that are not applicable for a given context by having the target respond to [`validModesForFontPanel:`](./validmodesforfontpanel_.md). If the target desires a font panel mode other than the standard mode mask, it must respond to this method.

This message is sent up the responder chain to the first responder implementing the method. Ideally that object should be the first responder found that also implements [`changeFont:`](./changefont_.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/validmodesforfontpanel:)*