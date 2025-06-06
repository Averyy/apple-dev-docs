# standard

**Framework**: Foundation  
**Kind**: property

Returns the shared defaults object.

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
class var standard: UserDefaults { get }
```

#### Return Value

The shared defaults object.

#### Discussion

If the shared defaults object doesn’t yet exist, it’s created with a search list containing the names of the following domains, in this order:

- For managed devices only, a domain containing defaults set by an administrator
- [`argumentDomain`](userdefaults/argumentdomain.md), consisting of defaults parsed from the application’s arguments
- For managed devices by an educational institution only, a domain containing defaults set in the iCloud key-value store
- A domain identified by the application’s bundle identifier
- [`globalDomain`](userdefaults/globaldomain.md), consisting of defaults meant to be seen by all applications
- [`registrationDomain`](userdefaults/registrationdomain.md), a set of temporary defaults whose values can be set by the application to ensure that searches will always be successful

The defaults are initialized for the current user. Subsequent modifications to the standard search list remain in effect even when this method is invoked again—the search list is guaranteed to be standard only the first time this method is invoked.

## See Also

- [Preferences and Settings Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UserDefaults/Introduction/Introduction.html#//apple_ref/doc/uid/10000059i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/standard)*