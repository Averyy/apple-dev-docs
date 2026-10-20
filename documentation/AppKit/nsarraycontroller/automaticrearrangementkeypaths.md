# automaticRearrangementKeyPaths

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of key paths that trigger automatic content sorting or filtering

**Availability**:
- macOS 10.5+

## Declaration

```swift
var automaticRearrangementKeyPaths: [String]? { get }
```

```objc
@property (copy, readonly, nullable) NSArray<NSString *> * automaticRearrangementKeyPaths;
```

#### Discussion

Subclasses can override this property to customize the default behavior of the sort descriptors and filtering predicates, for example, if additional arrangement criteria are used in a custom implementation of [`arrangedObjects`](./arrangedobjects.md).

## See Also

### Automatic Content Rearranging
- [var automaticallyRearrangesObjects: Bool](./automaticallyrearrangesobjects.md)
  A Boolean that indicates if the receiver automatically rearranges its content to correspond to the current sort descriptors and filter predicates
- [func didChangeArrangementCriteria()](./didchangearrangementcriteria%28%29.md)
  Invoked when any criteria for arranging objects change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/automaticrearrangementkeypaths)*