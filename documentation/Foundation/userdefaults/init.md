# init()

**Framework**: Foundation  
**Kind**: init

Creates a new defaults object and initializes it with the app’s current settings.

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
convenience init()
```

#### Discussion

Use this method to create a new defaults object to manage the app’s settings. If you add a domain using the [`addSuite(named:)`](userdefaults/addsuite(named:).md) method, the returned object retrieves values in that domain in addition to the standard ones. Custom domains remain in the search list until you remove them or release the object. When you write setting values using this object, it writes them to the current app’s settings.

## See Also

- [class var standard: UserDefaults](userdefaults/standard.md)
  The shared defaults object for the current app.
- [init?(suiteName: String?)](userdefaults/init(suitename:).md)
  Creates a new defaults object and initializes it with the settings from the specified database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/init())*