# automaticallyRearrangesObjects

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates if the receiver automatically rearranges its content to correspond to the current sort descriptors and filter predicates

**Availability**:
- macOS 10.5+

## Declaration

```swift
var automaticallyRearrangesObjects: Bool { get set }
```

#### Discussion

The default is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var automaticRearrangementKeyPaths: [String]?](nsarraycontroller/automaticrearrangementkeypaths.md)
  An array of key paths that trigger automatic content sorting or filtering
- [func didChangeArrangementCriteria()](nsarraycontroller/didchangearrangementcriteria.md)
  Invoked when any criteria for arranging objects change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/automaticallyrearrangesobjects)*