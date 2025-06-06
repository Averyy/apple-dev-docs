# didLoadNotification

**Framework**: Foundation  
**Kind**: property

A notification that lets observers know when classes are dynamically loaded.

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
class let didLoadNotification: NSNotification.Name
```

#### Discussion

When a request is made to a bundle for a class ([`classNamed(_:)`](bundle/classnamed(_:).md) or [`principalClass`](bundle/principalclass.md)), the bundle dynamically loads the executable code file that contains the class implementation and all other class definitions contained in the file. After the module is loaded, the bundle posts the [`didLoadNotification`](bundle/didloadnotification.md).

The notification object is the [`Bundle`](bundle.md) instance that dynamically loads classes. The `userInfo` dictionary contains an [`NSLoadedClasses`](nsloadedclasses.md) key.

In a typical use of this notification, an object might want to enumerate the `userInfo` array to check if each loaded class conformed to a certain protocol (say, an protocol for a plug-and-play tool set); if a class does conform, the object would create an instance of that class and add the instance to another [`NSArray`](nsarray.md) object.

## See Also

- [func classNamed(String) -> AnyClass?](bundle/classnamed(_:).md)
  Returns the `Class` object for the specified name.
- [var principalClass: AnyClass?](bundle/principalclass.md)
  The bundle’s principal class.
- [let NSLoadedClasses: String](nsloadedclasses.md)
  A constant used as a key for the `userInfo` dictionary of a [`didLoadNotification`](bundle/didloadnotification.md) notification that corresponds to an array of names of each class that was loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/didloadnotification)*