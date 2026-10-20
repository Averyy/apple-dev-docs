# mixers

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

Nodes in the event tree that control the volume of their child nodes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var mixers: [String : PHASEMixer] { get }
```

```objc
@property (copy, readonly) NSDictionary<NSString *,PHASEMixer *> * mixers;
```

## See Also

### Configuring Mixers and Metaparameters
- [var metaParameters: [String : PHASEMetaParameter]](./metaparameters.md)
  The object’s meta parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundevent/mixers)*