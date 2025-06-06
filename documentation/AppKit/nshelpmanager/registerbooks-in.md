# registerBooks(in:)

**Framework**: AppKit  
**Kind**: method

Registers one or more help books in the given bundle.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func registerBooks(in bundle: Bundle) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if registration is successful, [`false`](https://developer.apple.com/documentation/swift/false) if the bundle doesn’t contain any help books or if registration fails.

#### Discussion

You use `registerBooksInBundle:` to register help books in, for example, a plug-in bundle. The `Info.plist` in the bundle should contain a help book directory path, which specifies one or more folders containing help books.

The main bundle is automatically registered by [`openHelpAnchor(_:inBook:)`](nshelpmanager/openhelpanchor(_:inbook:).md) and [`find(_:inBook:)`](nshelpmanager/find(_:inbook:).md).

## Parameters

- `bundle`: The bundle for additional help books. Books in the main bundle are automatically registered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshelpmanager/registerbooks(in:))*