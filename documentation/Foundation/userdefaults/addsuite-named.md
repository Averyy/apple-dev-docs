# addSuite(named:)

**Framework**: Foundation  
**Kind**: method

Inserts the specified domain name into the receiver’s search list.

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
func addSuite(named suiteName: String)
```

#### Discussion

The `suiteName` domain is similar to a bundle identifier string, but isn’t necessarily tied to a particular application or bundle. A suite can be used to hold preferences that are shared between multiple applications.

The additional search lists of the `suiteName` domain are searched after the current domain, but before global defaults (that is, when a suite is added, the preferences subsystem first searches the app’s user preferences, then searches again as though it were an app with a bundle identifier equal to `suiteName`, and then finally searches the global preferences). Passing [`globalDomain`](userdefaults/globaldomain.md) or the current application’s bundle identifier is unsupported.

## Parameters

- `suiteName`: The domain name to insert.

## See Also

- [class var standard: UserDefaults](userdefaults/standard.md)
  Returns the shared defaults object.
- [func removeSuite(named: String)](userdefaults/removesuite(named:).md)
  Removes the specified domain name from the receiver’s search list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/addsuite(named:))*