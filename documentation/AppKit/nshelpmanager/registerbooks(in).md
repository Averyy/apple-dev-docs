# registerBooks(in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Registers one or more help books in the given bundle.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func registerBooks(in bundle: Bundle) -> Bool
```

```objc
- (BOOL) registerBooksInBundle:(NSBundle *) bundle;
```

## Return Value

[`true`](../../Swift/true.md) if registration is successful, [`false`](../../Swift/false.md) if the bundle doesn’t contain any help books or if registration fails.

## Discussion

You use `registerBooksInBundle:` to register help books in, for example, a plug-in bundle. The `Info.plist` in the bundle should contain a help book directory path, which specifies one or more folders containing help books.

The main bundle is automatically registered by [`openHelpAnchor(_:inBook:)`](./openhelpanchor%28_,inbook%29.md) and [`find(_:inBook:)`](./find%28_,inbook%29.md).

## Parameters

- `bundle`: The bundle for additional help books. Books in the main bundle are automatically registered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshelpmanager/registerbooks(in:))*