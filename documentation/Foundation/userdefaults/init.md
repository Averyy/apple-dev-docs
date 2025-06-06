# init()

**Framework**: Foundation  
**Kind**: init

Creates a user defaults object initialized with the defaults for the app and current user.

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

This initializer is equivalent to passing `nil` to the [`init(suiteName:)`](userdefaults/init(suitename:).md) initializer.

Use this initializer only if you’re not using the shared [`standard`](userdefaults/standard.md) user defaults.

## See Also

- [class var standard: UserDefaults](userdefaults/standard.md)
  Returns the shared defaults object.
- [init?(suiteName: String?)](userdefaults/init(suitename:).md)
  Creates a user defaults object initialized with the defaults for the specified database name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/init())*