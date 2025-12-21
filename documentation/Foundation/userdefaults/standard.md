# standard

**Framework**: Foundation  
**Kind**: property

The shared defaults object for the current app.

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

The shared defaults object for the app.

#### Discussion

Each app maintains a single, shared defaults object for you to use in your code. The first time your app retrieves the value of this property, it creates the shared object and caches the result. Subsequent retrieval attempts return the cached object.

The shared object retrieves settings from all of the standard domains. If you add a domain using the [`addSuite(named:)`](userdefaults/addsuite(named:).md) method, the object retrieves values from that domain in addition to the standard ones. Custom domains remain in the search list until you remove them or the app exits. When you write settings using the shared object, it writes them to the current app’s settings.

## See Also

- [convenience init()](userdefaults/init.md)
  Creates a new defaults object and initializes it with the app’s current settings.
- [init?(suiteName: String?)](userdefaults/init(suitename:).md)
  Creates a new defaults object and initializes it with the settings from the specified database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/standard)*