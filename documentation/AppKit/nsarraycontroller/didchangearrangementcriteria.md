# didChangeArrangementCriteria()

**Framework**: AppKit  
**Kind**: method

Invoked when any criteria for arranging objects change.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func didChangeArrangementCriteria()
```

#### Discussion

This method is invoked by the controller itself when any criteria for arranging objects change (sort descriptors or filter predicates) to reset the key paths for automatic rearranging.

##### Special Considerations

If you implement a subclass of `NSArrayController` and override [`rearrangeObjects()`](nsarraycontroller/rearrangeobjects().md) to use additional arrangement criteria, you should invoke this method if those criteria change.

## See Also

- [func rearrangeObjects()](nsarraycontroller/rearrangeobjects.md)
  Triggers filtering of the receiver’s content.
- [var automaticallyRearrangesObjects: Bool](nsarraycontroller/automaticallyrearrangesobjects.md)
  A Boolean that indicates if the receiver automatically rearranges its content to correspond to the current sort descriptors and filter predicates
- [var automaticRearrangementKeyPaths: [String]?](nsarraycontroller/automaticrearrangementkeypaths.md)
  An array of key paths that trigger automatic content sorting or filtering


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/didchangearrangementcriteria())*