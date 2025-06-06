# NSLoadedClasses

**Framework**: Foundation  
**Kind**: var

A constant used as a key for the `userInfo` dictionary of a [`didLoadNotification`](bundle/didloadnotification.md) notification that corresponds to an array of names of each class that was loaded.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let NSLoadedClasses: String
```

## See Also

- [func classNamed(String) -> AnyClass?](bundle/classnamed(_:).md)
  Returns the `Class` object for the specified name.
- [var principalClass: AnyClass?](bundle/principalclass.md)
  The bundle’s principal class.
- [class let didLoadNotification: NSNotification.Name](bundle/didloadnotification.md)
  A notification that lets observers know when classes are dynamically loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsloadedclasses)*