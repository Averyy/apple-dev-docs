# outputKeys()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns an array that contains the keys that identify the output ports of the root patch of the composition.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func outputKeys() -> [Any]!
```

```objc
- (NSArray *) outputKeys;
```

## Return Value

An array of keys associated with input ports.

## See Also

### Getting Input and Output Keys
- [func inputKeys() -> [Any]!](./inputkeys%28%29.md)
  Returns an array that contains the keys that identify the input ports of the root patch of the composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionrenderer/outputkeys())*