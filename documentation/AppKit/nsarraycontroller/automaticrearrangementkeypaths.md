# automaticRearrangementKeyPaths

**Framework**: AppKit  
**Kind**: property

An array of key paths that trigger automatic content sorting or filtering

**Availability**:
- macOS 10.5+

## Declaration

```swift
var automaticRearrangementKeyPaths: [String]? { get }
```

#### Discussion

Subclasses can override this property to customize the default behavior of the sort descriptors and filtering predicates, for example, if additional arrangement criteria are used in a custom implementation of [`arrangedObjects`](nsarraycontroller/arrangedobjects.md).

## See Also

- [var automaticallyRearrangesObjects: Bool](nsarraycontroller/automaticallyrearrangesobjects.md)
  A Boolean that indicates if the receiver automatically rearranges its content to correspond to the current sort descriptors and filter predicates
- [func didChangeArrangementCriteria()](nsarraycontroller/didchangearrangementcriteria.md)
  Invoked when any criteria for arranging objects change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/automaticrearrangementkeypaths)*