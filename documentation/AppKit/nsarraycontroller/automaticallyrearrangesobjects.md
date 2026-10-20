# automaticallyRearrangesObjects

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates if the receiver automatically rearranges its content to correspond to the current sort descriptors and filter predicates

**Availability**:
- macOS 10.5+

## Declaration

```swift
var automaticallyRearrangesObjects: Bool { get set }
```

```objc
@property BOOL automaticallyRearrangesObjects;
```

#### Discussion

The default is [`false`](../../Swift/false.md).

## See Also

### Automatic Content Rearranging
- [var automaticRearrangementKeyPaths: [String]?](./automaticrearrangementkeypaths.md)
  An array of key paths that trigger automatic content sorting or filtering
- [func didChangeArrangementCriteria()](./didchangearrangementcriteria%28%29.md)
  Invoked when any criteria for arranging objects change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/automaticallyrearrangesobjects)*