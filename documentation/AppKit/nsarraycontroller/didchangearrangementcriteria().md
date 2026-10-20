# didChangeArrangementCriteria()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked when any criteria for arranging objects change.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func didChangeArrangementCriteria()
```

```objc
- (void) didChangeArrangementCriteria;
```

#### Discussion

This method is invoked by the controller itself when any criteria for arranging objects change (sort descriptors or filter predicates) to reset the key paths for automatic rearranging.

##### Special Considerations

If you implement a subclass of `NSArrayController` and override [`rearrangeObjects()`](./rearrangeobjects%28%29.md) to use additional arrangement criteria, you should invoke this method if those criteria change.

## See Also

### Related Documentation
- [func rearrangeObjects()](./rearrangeobjects%28%29.md)
  Triggers filtering of the receiver’s content.
### Automatic Content Rearranging
- [var automaticallyRearrangesObjects: Bool](./automaticallyrearrangesobjects.md)
  A Boolean that indicates if the receiver automatically rearranges its content to correspond to the current sort descriptors and filter predicates
- [var automaticRearrangementKeyPaths: [String]?](./automaticrearrangementkeypaths.md)
  An array of key paths that trigger automatic content sorting or filtering


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/didchangearrangementcriteria())*